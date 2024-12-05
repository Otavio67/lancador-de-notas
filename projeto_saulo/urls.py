from django.contrib import admin
from django.urls import path
from app_principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('tabela/', views.tabela_alunos, name='tabela_alunos'),
    path('recuperacao/', views.recuperacao, name='recuperacao'),
    path('aprovados/', views.aprovados, name='aprovados'), 
]
