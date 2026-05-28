from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('novo/', views.novo_chamado, name='novo_chamado'),
    path('editar/<int:id>/', views.editar_chamado, name='editar_chamado'),
    path('excluir/<int:id>/', views.excluir_chamado, name='excluir_chamado'),
    path('detalhe/<int:id>/', views.detalhe_chamado, name='detalhe_chamado'),
    path('chamado/<int:id>/pdf/', views.gerar_pdf_chamado, name='gerar_pdf_chamado'),
    ]