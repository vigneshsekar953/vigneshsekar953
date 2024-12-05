from django.urls import path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.index,name='index1'),
    path('',views.index,name='index'),
    path('post/<int:post_id>',views.detail,name='detail1'),
    path('post/<str:slug>',views.detail,name='detail'),
    path('new_something_url',views.new_url_view,name='new_url'),
    path('old_url',views.old_url_redirect,name='old_url'),
    path('about',views.about_view,name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.blog_page, name='blog_page'),  # Your blog page

]