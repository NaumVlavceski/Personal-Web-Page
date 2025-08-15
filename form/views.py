
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from form.forms import ContactForm

import time

# Create your views here.

def contact(request):
    if request.method == "POST":
        last_sent = request.session.get("last_contact_time", 0)
        now = time.time()
        if now - last_sent < 30:
            return redirect("contact")

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Име: {name}\nEmail: {email}\nMessage: {message}"
            mail = EmailMessage(
                subject="Контакт Порака",
                body=full_message,
                from_email="nvlavceski542@gmail.com",
                to=["nvlavceski542@gmail.com"],
                reply_to=[email]
            )
            mail.send(fail_silently=False)

            # Запиши кога последно прати порака
            request.session["last_contact_time"] = now

            return redirect("index")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def index(request):
    return render(request, "index.html")
