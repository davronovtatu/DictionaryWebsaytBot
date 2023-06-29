from django.urls import path
from .views import translate,listword,addwords

urlpatterns = [
    path('', translate, name='translate'),
    path('wordslist/', listword, name='listw'),
    path('add/',addwords,name='addd'),
]
