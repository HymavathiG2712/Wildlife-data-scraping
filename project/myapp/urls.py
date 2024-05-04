from django.urls import path
from . import views

# urlpatterns = [
#     path('display/', views.display_results, name='display_results'),
# ]



urlpatterns = [
    path('search/', views.search_results, name='search_results')
]
