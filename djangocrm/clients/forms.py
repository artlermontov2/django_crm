from django import forms
from .models import Client
from team.models import UserModel


class AddClientForm(forms.ModelForm):

    email = forms.CharField(required=False,
        label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'})
    )
    name = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'*Имя'})
    )
    description = forms.CharField(
        label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Комментарии'})
    )  
    phone = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'8-000-000-00-00'})
    )

    worker = forms.ModelChoiceField(
        label="Выберите сотрудника", queryset=UserModel.objects.none(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Имя Сотрудника'})
    ) 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddClientForm, self).__init__(*args, **kwargs)
        self.fields['worker'].queryset = UserModel.objects.filter(user_id=user)

    class Meta:
        model = Client
        fields = ['name', 'phone', 'email', 'description', 'worker']

