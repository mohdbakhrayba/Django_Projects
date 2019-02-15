from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

class Page(models.Model):
    name = models.CharField(max_length= 200)
    page_content=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date=models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category,blank=True ,related_name='pages')

    def __str__(self):
        return self.name

    def was_modified_recently(self):
        return self.last_update_date

    class Meta:
        ordering=('page_content',)

    def get_absolute_url(self):
        return reverse('page-detail', args=[str(self.id)])

class Comment(models.Model):
    name = models.CharField(max_length = 42)
    email = models.EmailField(max_length=75)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name