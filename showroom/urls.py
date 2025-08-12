from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('add/',views.add,name='add'),
    path('list/',views.bike_list,name='bike_list'),
]

#path('user/<int:user_id>/',views.user_p,name='user'),
#http://example.com/user/45/  #this is in your url
#In Dynamic url, it contain variable part means url 
#can change depend on user input or data.
#use in views of dynamic url.
#def Views(request,user_id):
#   post =Post.objects.get(id=user_id)
#   return 