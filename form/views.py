from tkinter.font import names

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from form.forms import ContactForm


# Create your views here.

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Име: {name}\nEmail: {email}\nMessage: {message}"
            print(full_message)
            send_mail(
                subject="Контакт Порака",
                message=full_message,
                from_email=email,
                recipient_list=["nvlavceski542@gmail.com"],
                fail_silently=False,

            )
            return redirect("index")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form":form})

def index(request):
    return render(request, "index.html")

def success(request):
    return render(request,"success.html")