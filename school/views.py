from django.shortcuts import render
from .models import ExamScore
#from django.http import HttpResponse

# Create your views here.
def homepage(request):
    text = {'text':'Hello lockdoor !!!!'}
    return render(request, 'school/home.html',text)

def about(request):
    return render(request, 'school/about.html')

def contactus(request):
    return render(request, 'school/contactus.html')

def showscore(request):
    score = ExamScore.objects.all()
    context = {'score':score}
    return render(request, 'school/showscore.html', context)