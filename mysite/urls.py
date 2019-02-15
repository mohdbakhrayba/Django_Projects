"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from django.urls import include,path,include
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

admin.site.site_header = "My Sample Project"

urlpatterns = [

    path('',views.index , name='index'),
    #path('', views.home_view),
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
   # path('home/' ,views.special_case, name = 'home'),

    path('categories/', views.CategoryListView.as_view(), name ='categories'),
    path('categories/<int:pk>' , views.CategoryDetailView.as_view (), name='category-detail'),
    path('pages/<pk>' , views.PageDetailView.as_view(), name = 'page-detail'),

    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),

    path('pages/create/', views.PageCreate.as_view(), name='page_create'),
    path('pages/<int:pk>/update/', views.PageUpdate.as_view(), name='page_update'),

    path('category/',views.CategoryListView.as_view() , name ='category'),
    #path('category/<pk>' , views.CategoryDetailView.as_view , name='category-detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home') ,
    path("r'^search/",views.search_view , name = 'search'),
]
