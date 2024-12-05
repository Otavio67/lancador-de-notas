from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=7, unique=True)  
    nota1 = models.FloatField()  
    nota2 = models.FloatField()  
    nota3 = models.FloatField()  
    nota4 = models.FloatField()  
    media = models.FloatField(editable=False)  
    status = models.CharField(max_length=10, editable=False)  

    def save(self, *args, **kwargs):

        self.media = (self.nota1 * 0.4 + self.nota2 * 0.4 + self.nota3 * 0.1 + self.nota4 * 0.1)
        
        self.status = 'Aprovado' if self.media >= 6 else 'Reprovado'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.ra})"
