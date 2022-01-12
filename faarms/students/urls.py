from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls.conf import include, re_path
from .import views
urlpatterns = [
    url(r'^info$',views.info,name='info'),
    url(r'^urlextractor$' ,views.urlextractor,name='urlextractor'),
    path('details/<int:rollnumber>/<str:name>',views.academics,name="academics"),
    path('update/<int:rollnumber>',views.UpdateStudent,name="update"),
    url(r'^SearchStudent$',views.SearchStudent,name="search"),
    path('delete/<int:rollnumber>',views.DeleteStudent,name="delete"),
    url(r'^CreateStudent$',views.CreateStudent,name='create'),
    url(r'^register$',views.register,name='register'),
    url(r'',views.login_view,name='login'),
    url(r'^logout$',views.logout_view,name='logout'),
]


urlpatterns+=staticfiles_urlpatterns()

