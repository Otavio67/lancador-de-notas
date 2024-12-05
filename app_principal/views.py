from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno
import re  # Para validação do RA

# View para a página principal (home)
def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ra = request.POST.get('ra')
        nota1 = float(request.POST.get('nota1'))
        nota2 = float(request.POST.get('nota2'))
        nota3 = float(request.POST.get('nota3'))
        nota4 = float(request.POST.get('nota4'))

        # Validação do RA (deve ter 7 caracteres e ser somente números)
        if len(ra) != 7 or not ra.isdigit():
            return render(request, 'home.html', {
                'alunos': Aluno.objects.all(),
                'mensagem_erro': 'O RA deve ter 7 caracteres e ser composto apenas por números.'
            })

        # Validação das notas (deve estar no intervalo de 0 a 10)
        if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10) or not (0 <= nota3 <= 10) or not (0 <= nota4 <= 10):
            return render(request, 'home.html', {
                'alunos': Aluno.objects.all(),
                'mensagem_erro': 'As notas devem estar no intervalo de 0 a 10.'
            })

        # Verificar se o RA já existe
        if Aluno.objects.filter(ra=ra).exists():
            return render(request, 'home.html', {
                'alunos': Aluno.objects.all(),
                'mensagem_erro': 'Não pode haver dois alunos com o mesmo RA.'
            })

        # Cálculo da média e status
        media = (nota1 * 0.4) + (nota2 * 0.4) + (nota3 * 0.1) + (nota4 * 0.1)
        status = 'Aprovado' if media >= 6 else 'Reprovado'

        # Criar e salvar o aluno
        aluno = Aluno(nome=nome, ra=ra, nota1=nota1, nota2=nota2, nota3=nota3, nota4=nota4, media=media, status=status)
        aluno.save()

        # Mensagem de sucesso
        return render(request, 'home.html', {
            'alunos': Aluno.objects.all(),
            'mensagem_sucesso': True,
        })
    
    return render(request, 'home.html', {'alunos': Aluno.objects.all()})

# Tabela de alunos
def tabela_alunos(request):
    alunos = Aluno.objects.all()  # Recupera todos os alunos
    return render(request, 'tabela_alunos.html', {'alunos': alunos})

# Lista de alunos reprovados
def recuperacao(request):
    alunos_reprovados = Aluno.objects.filter(media__lt=6).order_by('nome')  # Filtra os reprovados
    return render(request, 'recuperacao.html', {'alunos_reprovados': alunos_reprovados})

# Lista de alunos aprovados
def aprovados(request):
    alunos_aprovados = Aluno.objects.filter(media__gte=6).order_by('nome')  # Filtra os aprovados (média >= 6)
    return render(request, 'aprovados.html', {'alunos_aprovados': alunos_aprovados})
