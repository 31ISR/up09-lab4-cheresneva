from django.shortcuts import render
from .models import Communities



def communities_list(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communities_page(request, slug):
    communities = Communities.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'communities': communities})
# Create your views here.
