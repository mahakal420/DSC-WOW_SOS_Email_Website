from django.shortcuts import render, redirect
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os
import wave
#from sendmail import settings
def Modal(request):
    if request.method == "POST":
        form = UploadPhoneForm(request.POST)
        if form.is_valid():
            if not NeedyPerson.objects.filter(phoneOfNeedy = request.POST["phoneOfNeedy"]).exists():
                request.session["phoneOfNeedy"] = request.POST["phoneOfNeedy"]
                req = NeedyPerson(phoneOfNeedy = request.POST["phoneOfNeedy"])
                req.save()
            return render(request, 'homepage.html')

    else:
        form = UploadPhoneForm()
    return render(request, 'index.html', {'form': form})


def Contact(request):
    return render(request, 'contact.html')

def Safety(request):
    return render(request, 'safety.html')

def Home(request):
    return render(request, 'homepage.html')

def Help(request):
    if request.method == 'POST':
        form = UploadHelpForm(request.POST)
        if form.is_valid():
            req = HelpModel(phoneOfNeedy = request.session["phoneOfNeedy"], message = request.POST["helpdata"])
            req.save()

            reciever = "eng.arpit420@gmail.com"
            send_mail(
                'Query message by ' + str(request.session["phoneOfNeedy"]),request.POST["helpdata"],settings.EMAIL_HOST_USER,[reciever], fail_silently=False
            )

            return redirect('home')
    else:
        form = UploadHelpForm()

    return render(request, 'help.html', {'form': form})

def Message(request):
    if request.method == "POST":
        form = UploadMessageForm(request.POST)
        if form.is_valid():
            obj = NeedyPerson.objects.get(phoneOfNeedy = request.session["phoneOfNeedy"])
            obj.messageOfNeedy = request.POST["messageOfNeedy"]
            obj.save(update_fields=['messageOfNeedy'])
            reciever = "eng.arpit420@gmail.com"
            send_mail(
                'SAVE ' + str(request.session["phoneOfNeedy"]),request.POST["messageOfNeedy"],settings.EMAIL_HOST_USER,[reciever], fail_silently=False
            )
            return render(request, 'homepage.html')
    else:
        form = UploadMessageForm()
    return render(request, 'message.html', {'form': form})


def logo_data(extension, imagename):
    name = imagename  + extension
    path = settings.MEDIA_ROOT + '\\photoUploads\\' + name
    with open(os.path.normpath(path), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo


def Photo(request):
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST,  request.FILES)

        if form.is_valid():

            obj = NeedyPerson.objects.get(phoneOfNeedy = request.session["phoneOfNeedy"])
            obj.photoOfNeedy = request.FILES["photoOfNeedy"]
            obj.save(update_fields=['photoOfNeedy'])
            reciever = "eng.arpit420@gmail.com"
            message = EmailMultiAlternatives(
            subject="danger",
            body="Save me " + "\nphone no. is " + str(request.session["phoneOfNeedy"]),
            from_email=settings.EMAIL_HOST_USER,
            to=[reciever],

          )
            file_extension = os.path.splitext(request.FILES['photoOfNeedy'].name)[1]



            file_name = os.path.splitext(request.FILES['photoOfNeedy'].name)[0]


            message.attach(logo_data(file_extension, file_name))

            message.send(fail_silently=False)


            return render(request, 'homepage.html')
    else:
        form = UploadPhotoForm()
    return render(request, 'photo.html', {'form' : form})

@csrf_protect
def Audio(request):
    if request.method == "POST":
        audio_data = request.FILES['audio_data']
        reciever = "eng.arpit420@gmail.com"
        email = EmailMessage("save " + str(request.session["phoneOfNeedy"]), "", settings.EMAIL_HOST_USER, [reciever])

        email.content_subtype = "html"
        email.attach(audio_data.name, audio_data.read(), audio_data.content_type)
        email.send()
        obj = NeedyPerson.objects.get(phoneOfNeedy = request.session["phoneOfNeedy"])

        obj.audioOfNeedy = audio_data
        obj.save(update_fields=['audioOfNeedy'])

        return render(request, "homepage.html")
    else:
        return render(request, "audio.html")
