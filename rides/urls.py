from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('form', views.form, name='form'),
    path('create', views.create, name='create'),
    path('ai', views.ai, name='ai'),
    path('ai_interaction', views.ai_interaction, name='ai_interaction'),

]
