from django.urls import path

from .views import Index2View, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('2/', Index2View.as_view(), name='index2'),
]
