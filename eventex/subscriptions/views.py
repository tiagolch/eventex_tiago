from django.contrib import messages
from django.core import mail
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        #form.full_clean() #Sanitiza os dados
        if form.is_valid(): # troca full_clean pelo is_valid para certificar que os campos estejam validos

        # context = dict(name = 'Tiago Chaves', cpf = '0123456789',
        #                email = 'tiago@teste.com', phone = '21-96460-6703')   ### context usado para teste 
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data) # substituido context por cleaned_data fornecendo os dados ja sanitizados
            mail.send_mail('Confirmação de inscrição',
                        body,
                        'contato@eventex.com.br',
                        ['contato@eventex.com.br', form.cleaned_data['email']])
            messages.success(request, 'Inscrição realizada com sucesso')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html', {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)









