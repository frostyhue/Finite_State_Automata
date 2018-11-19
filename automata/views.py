# The libraries that are used for the engine of the application.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Function used by the url file to redirect to the index's page.
def main(request):
    return render(request, 'index.html')
