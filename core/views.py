from django.shortcuts import render, redirect, get_object_or_404
from .models import Chamado
from .forms import ChamadoForm
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def lista_chamados (request):
    status_filtro = request.GET.get('status')
    busca = request.GET.get('search')

    todos = Chamado.objects.all()
    total_abertos = todos.filter(status='aberto').count()
    total_progresso = todos.filter(status='progresso').count()
    total_concluido = todos.filter(status='concluido').count()


    chamados = Chamado.objects.all().order_by('-data_criacao')
    if status_filtro:
        chamados= chamados.filter(status=status_filtro)
    if busca:
        chamados = chamados.filter(cliente__icontains=busca)
    return render(request, 'index.html', {
        'chamados': chamados,
        'total_abertos': total_abertos,
        'total_progresso': total_progresso,
        'total_concluido': total_concluido,
    })


def novo_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chamado criado com sucesso! O técnico já pode visualizar.")
            return redirect('lista_chamados')
    else:
        form = ChamadoForm()
    
    return render(request, 'novo_chamado.html', {'form': form})

def editar_chamado(request, id):
    # 1. Busca o chamado pelo ID ou dá erro 404 se não existir
    chamado = get_object_or_404(Chamado, id=id)
    
    if request.method == 'POST':
        # 2. "instance=chamado" diz ao Django que estamos editando um existente, não criando um novo
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            messages.info(request, f'Chamado de {chamado.cliente} atualizado!')
            return redirect('lista_chamados')
    else:
        # 3. Carrega o formulário já preenchido com os dados do banco
        form = ChamadoForm(instance=chamado)
    
    return render(request, 'novo_chamado.html', {'form': form, 'editando': True})



def excluir_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id)
    # Primeiro guardamos o nome, depois deletamos
    nome_cliente = chamado.cliente 
    chamado.delete()
    
    messages.error(request, f"O chamado de {nome_cliente} foi removido do sistema.")
    return redirect('lista_chamados')


def detalhe_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id)
    return render(request,'detalhe_chamado.html', {'chamado': chamado})




def gerar_pdf_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id)
    
    # Criar a resposta do navegador como PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="OS_{chamado.id}.pdf"'
    
    # Criar o PDF
    p = canvas.Canvas(response, pagesize=A4)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "REDE BR TELECOM - ORDEM DE SERVIÇO")
    
    p.setFont("Helvetica", 12)
    p.drawString(100, 770, f"Protocolo: #{chamado.id}")
    p.drawString(100, 750, f"Cliente: {chamado.cliente}")
    p.drawString(100, 730, f"Data de Abertura: {chamado.data_criacao.strftime('%d/%m/%Y')}")
    p.drawString(100, 710, f"Status Atual: {chamado.get_status_display()}")
    
    p.line(100, 690, 500, 690) # Uma linha divisória
    
    p.drawString(100, 670, "Descrição do Problema:")
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(100, 650, chamado.descricao[:100]) # Mostra os primeiros 100 caracteres
    
    p.setFont("Helvetica", 12)
    p.drawString(100, 200, "_______________________________________")
    p.drawString(100, 185, "Assinatura do Cliente")
    
    p.showPage()
    p.save()
    return response