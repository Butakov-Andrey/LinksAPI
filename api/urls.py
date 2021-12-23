from django.urls import path
from .views import VisitedDomains, VisitedLinks


urlpatterns = [
    path('visited_domains/', VisitedDomains.as_view()),
    path('visited_links', VisitedLinks.as_view()),
]
