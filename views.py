from django.shortcuts import render
from django.views.generic import ListView
from requests import request
from .models import Addproject
from django.db.models import Q


# Create your views here.

class AddprojectListView(ListView):
    model = Addproject
    template_name = 'index.html'
    context_object_name = "projects"

    def get_queryset(self):
        queryset = Addproject.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = Addproject.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
        print(search)
        return queryset


def blogs(request):
    return render(request, 'blogs.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def about(request):
    return render(request, 'about.html')


def about_copy(request):
    return render(request, 'about_copy.html')


def cases(request):
    return render(request, 'cases.html')


def logistic(request):
    return render(request, 'logistic.html')


def services(request):
    return render(request, 'services.html')


def service_details(request):
    return render(request, 'service_details.html')


def index2(request):
    return render(request, 'index2.html')


def index3(request):
    return render(request, 'index3.html')


def index4(request):
    return render(request, 'index4.html')


def bindex5(request):
    return render(request, 'index5.html')


def index6(request):
    return render(request, 'index6.html')


def contact(request):
    return render(request, 'contact.html')


def Project(request):
    return render(request, 'Project.html')


def case_details(request):
    return render(request, 'case_details.html')


def index(request):
    return render(request, 'index.html')


# РУССКИЯ ЯЗЫК

def Default_Rus(request):
    return render(request, 'Default_Rus.html')


def About_RU(request):
    return render(request, 'About_RU.html')


def Services_RU(request):
    return render(request, 'Services_RU.html')


def Service_details_RU(request):
    return render(request, 'Service_details_RU.html')


def Case_details_RU(request):
    return render(request, 'Case_details_RU.html')


def Cases_RU(request):
    return render(request, 'Cases_RU.html')


def Blog_details_RU(request):
    return render(request, 'Blog_details_RU.html')


def Blogs_RU(request):
    return render(request, 'Blogs_RU.html')


def Contact_RU(request):
    return render(request, 'Contact_RU.html')


# Projects

def production(request):
    return render(request, 'production.html')


def IT(request):
    return render(request, 'IT.html')


def commerce(request):
    return render(request, 'commerce.html')


def energy(request):
    return render(request, 'energy.html')


def PlaceOfBirth(request):
    return render(request, 'PlaceOfBirth.html')


def allProjects(request):
    return render(request, 'allProjects.html')


# Проекты
def Production_RU(request):
    return render(request, 'Production_RU.html')


def IT_RU(request):
    return render(request, 'IT_RU.html')


def commerce_RU(request):
    return render(request, 'commerce_RU.html')


def energy_RU(request):
    return render(request, 'energy_RU.html')


def PlaceOfBirth_RU(request):
    return render(request, 'PlaceOfBirth_RU.html')


def allProjects_RU(request):
    return render(request, 'allProjects_RU.html')


def applicants_RU(request):
    return render(request, 'applicants_RU.html')


def applicants(request):
    return render(request, 'applicants.html')


def aboutKR(request):
    return render(request, 'aboutKR.html')
