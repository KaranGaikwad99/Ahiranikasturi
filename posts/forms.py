from django import forms
from django.forms import widgets
#from Contact_us import models
from .models import Contact_us, Registration

class Contact_usForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request', None)
        super (Contact_usForm,self ).__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(Contact_usForm, self).clean()
        
    class Meta:
        model = Contact_us
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
        ]
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control required'}),
            "last_name":widgets.TextInput(attrs={'class':'form-control required'}),
            'email':widgets.TextInput(attrs={'class':'form-control required'}),
            "subject":forms.TextInput(attrs={'class':'form-control required'}),
            "message":forms.TextInput(attrs={'class':'form-control required'}),
        }
        error_messages={
            'first_name':{
                'required':'Please Enter First Name'
            },
            'last_name':{
                'required':'Please Enter Last Name'
            },
            'email':{
                'required':'Please Enter Email'
            },
            'subject':{
                'required':'Please Enter Subject'
            },
            'message':{
                'required':'Please Enter Message'
            },  
        }

class Registration_Form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request', None)
        super (Registration_Form,self ).__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super(Registration_Form, self).clean()

    class Media:
        js = {
            'static/js/registration.js',            
        }

    class Meta:
        model = Registration
        fields = ["first_name","last_name","date_of_birth","address","contact_number","hieght","email","education","employment","about_you",]
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control required'}),
            "last_name":widgets.TextInput(attrs={'class':'form-control required'}),
            "date_of_birth":widgets.DateInput(format=('%d-%m-%Y'),attrs={'class':'form-control datepicker','autocomplete':'false'}),
            "address":widgets.TextInput(attrs={'class':'form-control required'}),
            "contact_number":widgets.TextInput(attrs={'class':'form-control required'}),
            "hieght":widgets.TextInput(attrs={'class':'form-control required'}),
            'email':widgets.TextInput(attrs={'class':'form-control required'}),
            "education":widgets.TextInput(attrs={'class':'form-control required'}),
            "employment":forms.TextInput(attrs={'class':'form-control required'}),
            "about_you":forms.TextInput(attrs={'class':'form-control required'}),
        }
        error_messages={
            'first_name':{
                'required':'Please Enter First Name'
            },
            'last_name':{
                'required':'Please Enter Last Name'
            },
            'date_of_birth':{
                'required':'Please Enter DOB'
            },
            'address':{
                'required':'Please Enter Address Details'
            },
            'contact_number':{
                'required':'Please Enter Contact Number'
            },
            'hieght':{
                'required':'Please Enter height'
            },
            'email':{
                'required':'Please Enter Email id'
            },
            'education':{
                'required':'Please Enter Education'
            },
            'employment':{
                'required':'Please Enter Employment'
            },
            'about_you':{
                'required':'Please Enter Your Details'
            },  
        }


















