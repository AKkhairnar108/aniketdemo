from django.contrib import admin
from .models import Bike
#admin.py used to costomize your models appear
#and behave in build-in django admin interface.
#this line tell to show Bike model in Admin panel.
admin.site.register(Bike)
#we also register mutiple models.
#
#we also customize our admin interface.
#class BookAdmin(admin.ModelAdmin):
#  list_display=('title','publish')
#  search_fields= ('title',)
#  list_filter = ('author',)
#admin.site.register(Book,BookAdmin)