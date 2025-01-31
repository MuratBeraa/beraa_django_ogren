# .../ --> main.html
# .../index/ --> main.html
# .../user_acc --> hesap.html

from django.urls import path
from .views import blog, blog_detail

urlpatterns = [
    path("",blog,name="main_page"),
    path("user_detail/",blog_detail,name="user_detail")
]