from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm

# Create your views here.
def home(request):
    data_despesas = {}
    data_despesas['despesas'] = Transacao.objects.all().filter(tipo='D')
    data_receitas = {}
    data_receitas['receitas'] = Transacao.objects.all().filter(tipo='R')
    
    

    return render(request, 'contas/home.html', data_despesas)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    data['form'] = form
    return render(request, 'contas/form.html', data)
