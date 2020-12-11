
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from home import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', views.CardList.as_view()),
    path('home', include('home.urls'))
]
