from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
def index(request):
    context = {
        'variable': 'Hi variable'
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        nameField = request.POST.get('name')
        emailField = request.POST.get('email')
        phoneField = request.POST.get('phoneno')
        textField = request.POST.get('text')
        
        contact = Contact(name = nameField, email = emailField,phone = phoneField,text = textField, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent!')
        
    return render(request, 'contact.html')
