from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from person.models import Person


def welcomefunction(request):
    number_of_persons_from_database = Person.objects.count()
    #allpersons = Person.objects.all()
    persons = Person.objects.order_by('id')
    #return render(request, 'welcome.html', {'no_persons': number_of_persons_from_database, 'allpersons': allpersons})
    return render(request, 'welcome.html', {'no_persons': number_of_persons_from_database, 'allpersons': persons})
    # return HttpResponse('Hello world from django')
    # messages = {'msg1': 'Value message 1', 'msg2': 'Value message 2'}
    # return render(request, 'welcome.html', messages)

# def saybye(request):
#   return HttpResponse('Saying bye from django')
