

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('search',views.search,name='search'),
    path('showcart',views.showcart,name='showcart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile')
    
]
