from django.urls import path
from .views import Items, VisitedLinks


urlpatterns = [
    path('items/', Items.as_view()),
    path('visited_links', VisitedLinks.as_view()),
]
