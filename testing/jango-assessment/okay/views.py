from django.shortcuts import render
from django.http import HttpResponse
from .forms import Keyin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse("hi")
@csrf_exempt
@login_required(login_url='/admin')
def keyin_score(request):
    if request.POST:
        form = Keyin(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.result = instance.score*20/100
            instance.save()
    return render(request,'view_scores_details.html', {'form': Keyin})

    