from django.urls import path
from .import views
app_name='newuser'

urlpatterns = [
    path('home',views.home,name='home'),
    path('header',views.header,name='header'),
    path('enquire',views.enquire,name='enquire'),
    path('footer',views.footer,name='footer'),
    path('about',views.about,name='about'),
    path('placement',views.placement,name='placement'),
    path('blog',views.blog,name='blog')
    
]
