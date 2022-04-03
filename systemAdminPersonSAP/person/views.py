from django.forms import modelform_factory
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
from person.models import Person
from person.forms import formPerson


def personDetail(request, id):
    #person = Person.objects.get(pk=id)
    person = get_object_or_404(Person, pk=id)
    return render(request, 'persons/detail.html', {'person': person})

# formPerson = modelform_factory(Person, exclude=[]) 

def newPerson(request):
  
    if request.method == 'POST':
          # to process our form
          shapePerson = formPerson(request.POST) # the data from our post is located here
          # before to insert in the data base, we need to validate 
          if shapePerson.is_valid():
              shapePerson.save()
              return redirect('index')
    else:
        shapePerson = formPerson()
        return render(request, 'persons/new.html', {'shapePerson': shapePerson})

    return render(request, 'persons/new.html', {'shapePerson': shapePerson})    



def editPerson(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
          # to process our form
          shapePerson = formPerson(request.POST, instance=person) # the data from our post is located here
          # before to insert in the data base, we need to validate 
          if shapePerson.is_valid():
              shapePerson.save()
              return redirect('index')
    else:
      
        shapePerson = formPerson(instance=person)
        

    return render(request, 'persons/edit.html', {'shapePerson': shapePerson})  

    



def deletePerson(request, id):
    person = get_object_or_404(Person, pk=id)
    if person:
        person.delete()
    return redirect('index')
 