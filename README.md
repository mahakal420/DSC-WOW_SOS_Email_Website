# DSC-WOW_SOS_Email_Website
## TECH STACK USED
Django Stack: Django, python and SQLite3 as Database

## INSTALLATION
1. Install python for respective OS: [Click here]( https://www.python.org/downloads/)

2. Install pip for respective OS: [Click here]( https://www.makeuseof.com/tag/install-pip-for-python/)

3. Install Django for respective OS: [Click here](https://www.thecrazyprogrammer.com/2018/09/how-to-install-django.html)

## DO CHANGES IN CODE
Navigate to project folder where settings.py present and do following changes in code (present at the end of settings.py file)

Enter your email and password of gmail account from which mail has to be send
```
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

Note :

1. Allow EMAIL_HOST_USER to allow less secure apps to send mail(gmail account), since this website is on localhost now. You won't have to allow less secure apps to access EMAIL_HOST_USER once SSL certificate is enabled for this website.

2. Since this website is running on local server therefore there isn't SSL certificate for this website yet.

3. Reciever's email(gmail accounts) list is set in the code itself.

## STARTING LOCAL DEVELOPMENT SERVER

1. Open command prompt

2. Navigate to project folder where manage.py present

3. Run following command
```
 python manage.py runserver  
```

## RUN THE WEBSITE AS FOLLOWS
1. Open a browser.

2. Search for: 127.0.0.1:8000/enterphone

*You now have website running on your browser*
