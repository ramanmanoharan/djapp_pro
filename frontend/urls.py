from django.urls import path

from . import views
#handler404 = 'frontend.views.custom_page_not_found_view'
# handler500 = 'frontend.views.handler500'

urlpatterns = [
	path('#', views.index, name='index'),
    path('', views.index, name='index'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('blogdetails/<int:id>', views.blogdetails, name='blogdetails'),



]

