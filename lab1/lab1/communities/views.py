from django.shortcuts import render, redirect
from .models import Communities
from django.contrib.auth.decorators import login_required
from . import forms 

@login_required(login_url="/users/login/")
def communities_new(request):
    if request.method == 'POST': 
        form = forms.Createcommunities(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return redirect('communities:list')
    else:
        form = forms.Createcommunities()
    return render(request, 'communities/communities_new.html', { 'form': form })


def communities_list(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communities_page(request, slug):
    communities = Communities.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'communities': communities})
# Create your views here.
