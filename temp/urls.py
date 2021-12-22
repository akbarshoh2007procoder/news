from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main),
    path('blog/', views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('single/',views.single,name="single")
]