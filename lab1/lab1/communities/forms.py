from django import forms 
from . import models 

class Createcommunities(forms.ModelForm): 
    class Meta: 
        model = models.Communities
        fields = ['name','description','slug','avatar','free']