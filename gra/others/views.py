from django.shortcuts import render,redirect
from .models import legals_pannel,publications_pannel,contacts_pannel,locations_pannel

# Create your views here.


def legals(request):
    return render(request=request,
                  template_name="others/legals.html",
                  context={"leg_pannel": legals_pannel.objects.all()})


def publications(request):
    return render(request=request,
                  template_name="others/publications.html",
                  context={"pub_pannel": publications_pannel.objects.all})




def offices(request):
    return render(request=request,
                  template_name="others/offices.html",
                  context={"loc_pannel": locations_pannel.objects.all})



def contacts(request):
    return render(request=request,
                  template_name="others/contacts.html",
                  context={"cont_pannel": contacts_pannel.objects.all})