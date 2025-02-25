# catalog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Если пришёл запрос к относительному URL catalog/,
    # то запрос из корневого urls.py перенаправляется сюда, 
    # в файл catalog/urls.py;
    # и если в запросе после 'catalog/' ничего нет (пустая строка),
    # будет вызвана view-функция product_list() из файла catalog/views.py
    path('', views.index)]