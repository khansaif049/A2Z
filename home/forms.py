from django import forms  
from home.models import Sta  
  
class StaFrom(forms.ModelForm):  
    class Meta:  
        model = Sta  
        fields = "__all__"  