from django.forms import ModelForm 
from shortapp.models import Database


class Submitform(ModelForm):

    class Meta:
        model = Database
        fields = '__all__'
