

from django.forms import EmailInput, ModelForm

from person.models import Person


class formPerson(ModelForm):
    class Meta:
        model = Person
        # we are going to use all attribute of our model person
        fields = '__all__'
        # indicate the type of the entry
        # https://docs.djangoproject.com/en/4.0/ref/forms/widgets/
        widgets = {

            'email' : EmailInput(attrs={'type':'email'})
        }


