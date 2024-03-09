from .forms import RideForm, NewRideForm


from django.shortcuts import render, redirect

from .models import Person

# relative import of forms
# from .forms import RideForm

# Create your views here.


def index(request):

  context = {}
  context["form"] = RideForm()


  if "stateSearch" in request.GET:
    context["inputExists"] = True
    stateSearch = request.GET["stateSearch"]
    citySearch = ""

    if "citySearch" in request.GET:
      citySearch = request.GET["citySearch"]
    
    context["people"] = Person.objects.filter(destination_city__icontains=citySearch, destination_state__icontains=stateSearch) | Person.objects.filter(origination__icontains=citySearch, destination_state__icontains=stateSearch)

  return render(request, "index_view.html", context)

def about(request):
    return render(request, "about.html")

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()
    return redirect("/rides")

def form(request):
  context = {}
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "form.html", context)

import os
from transformers import pipeline
from .models import Person

def ai(request):
    return render(request, "ai.html")

def ai_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        rides_data = Person.objects.all()

        system_message = f"You are trying to help folks get rides based on the data you have in your database: {rides_data}"
        

        # Combine system message and user input
        prompt = f"{system_message} {user_input} AI:"
        
        # Load the text generation pipeline with the desired model
        generator = pipeline("text-generation", model="openai-community/gpt2")
        
        # Generate text based on combined prompt
        ai_text = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        final_ai_text = ai_text.split("AI:")[-1].strip()

        return render(request, "ai.html", {'ai_text': final_ai_text})
    
    return render(request, "ai.html")
