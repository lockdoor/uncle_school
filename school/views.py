from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text = {'text':'Hello lockdoor !!!!'}
    return render(request, 'school/home.html',text)

def about(request):
    return render(request, 'school/about.html')

def contactus(request):
    return render(request, 'school/contactus.html')
