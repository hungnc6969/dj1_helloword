from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name = 'about'),
]
# when use class-based view, always add as_view() at the end of thr view name
