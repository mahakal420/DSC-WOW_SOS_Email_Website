from django import forms
from .models import *

class UploadMessageForm(forms.Form):
    messageOfNeedy = forms.CharField(max_length = 400,
                               widget = forms.TextInput(attrs = {
                                   'name':'messageofneedy',
                               }))

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = NeedyPerson
        fields = ['photoOfNeedy']
        
class UploadPhoneForm(forms.Form):
    phoneOfNeedy = forms.IntegerField(
                                   widget = forms.NumberInput(attrs = {
                                   'name':'phoneofneedy',
                               }))
        
class UploadAudioForm(forms.Form):
    class Meta:
        model = NeedyPerson
        fields = ['audioOfNeedy']
        
class UploadHelpForm(forms.Form):
     helpdata = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":60}))
        
