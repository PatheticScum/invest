import imp
from operator import index
from django.urls import path
from .views import AddprojectListView, about_copy, allProjects_RU, allProjects, blog_details, blogs, case_details, cases, service_details, services, contact, aboutKR, about, Project, Default_Rus, production, About_RU, Blog_details_RU, Blogs_RU, Cases_RU, Case_details_RU, Contact_RU,  Production_RU, Services_RU, Service_details_RU, IT, IT_RU, commerce, commerce_RU, energy, energy_RU, PlaceOfBirth, PlaceOfBirth_RU, applicants_RU, applicants
urlpatterns = [
    path('' ,AddprojectListView.as_view(), name= 'home'),
    path('about/', about, name='about'),
    path('about_copy/', about_copy, name='about_copy'),
    path('services/', services, name='services'),
    path('service_details', service_details, name='service_details'),
    path('cases/', cases, name='cases'),
    path('case_details/', case_details, name='case_details'),
    path('blogs/', blogs, name='blogs'),
    path('blog_details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    # path('главное/', Default_Rus, name='default_rus'),
    path('Project/', Project, name='project'),

    

    #РУССКИЙ ЯЗЫК
    path('Главная/', Default_Rus, name='home_ru'),
    path('О нас/', About_RU, name='about_ru'),
    # path('about_copy/', about_copy, name='about_copy_ru'),
    path('Сервисы/', Services_RU, name='services_ru'),
    path('Сервисф Деталь', Service_details_RU, name='service_details_ru'),
    path('Кейсы/', Cases_RU, name='cases_ru'),
    path('Кейсы Деталь/', Case_details_RU, name='case_details_ru'),
    path('Блог/', Blogs_RU, name='blogs_ru'),
    path('Блог Детали/', Blog_details_RU, name='blog_details_ru'),
    path('Контакты/', Contact_RU, name='contact_ru'),
    path('Главное/', Default_Rus, name='default_ru'),
    # path('Project/', Project, name='project'),
    path('Производство/', Production_RU, name='production_ru'),


    #ПРОЕКТЫ 
    path('Производство/', Production_RU, name='production_ru'),
    path('IT_РУ/', IT_RU, name='IT_ru'),
    path('Коммерция/', commerce_RU, name='commerce_ru'),
    path('Энергетика/', energy_RU, name='energy_ru'),
    path('Месторождения/', PlaceOfBirth_RU, name='place_ru'),
    path('Все/', allProjects_RU, name='all_ru'),


    #PRODUCTIONS
    path('production/', production, name='production'),
    path('IT/', IT, name='IT'),
    path('commerce/', commerce, name='commerce'),
    path('energy/', energy, name='energy'),
    path('PlaceOfBirth/', PlaceOfBirth, name='place'),
    path('All/projects/', allProjects, name='all'),



    path('applicants', applicants, name='applicants'),
    path('applicants/ru', applicants_RU, name='applicants_ru'),

    path('kr', aboutKR, name='kr'),
    
]
