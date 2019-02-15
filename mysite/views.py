from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Category, Page
from django.template import loader

# learn how to import data from the db
from .models import Page

from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, timedelta

def index(request):

    num_pages = Page.objects.all().count()
    num_categories = Category.objects.all().count()
    recently_modified = Page.objects.order_by('-last_update_date')[:3]


    context = {
        'num_pages' : num_pages,
        'num_categories' : num_categories,
        'recently_modified' : recently_modified ,
    }
    return render(request, 'index.html',context=context)

class CategoryListView(generic.ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()  # Get 5 books containing the title war

class CategoryDetailView(generic.DetailView):
    model = Category

    def category_detail_view(request, primary_key):
        category = get_object_or_404(Category, pk=primary_key)
        return render(request, 'categories/category_detail.html', context={'category': category})


class PageDetailView(generic.DetailView):
    model = Page


    def page_detail_view(request, primary_key):
       page = Page.objects.all()
       return render(request,'pages/page_detail.html', context = { 'page' :page } )


class PageCreate(LoginRequiredMixin,CreateView):
    model = Page
    fields = '__all__'


class PageUpdate(LoginRequiredMixin,UpdateView):
    model = Page
    fields = '__all__'


def category_view(request):
    category = Category.objects.order_by('name')[:5]
    template = loader.get_template('category.html')
    context = {
        'category_list' : category
    }
    return HttpResponse(template.render(context,request))





class CategoryCreate(LoginRequiredMixin,CreateView):
    model = Category
    fields = '__all__'

class CategoryUpdate(LoginRequiredMixin,UpdateView):
    model = Category
    fields = '__all__'






def search_view(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton = request.GET.get('submit')

        # allpages = Page.objects.all()

        if query is not None:
            lookups = Q(name__icontains = query) | Q(page_content__icontains=query)

            results = Page.objects.filter(lookups).distinct()

            context={'results:results, '
                     'submitbutton' : submitbutton}

            return render(request, 'search_results.html', context)

        else:
            return render(request,'search_results.html'  )

    else:


     return render(request,'search_results.html' )

