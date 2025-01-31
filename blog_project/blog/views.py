from django.http.response import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from blog.models import Blog

def blog(requests):
    context = {
        "blogs" : Blog.objects.all()
    }
    
    return render(requests, "index.html", context)

def blog_detail(requests):
    return render(requests, "user_detail.html")

#### ŞU BLOGS SAYFASI İLE ANA SAYFAYI BİRBİRİNDEN AYIR.... SONRASINDA VERİTABANI İŞLEMLERİNE DEAM ET


"""
def blog_deneme(requestes):
    return HttpResponse("BLOG SAYFASI")

"""
"""
class Blog(ListView):
    print( HttpResponse("BLOG SAYFASI"))
"""