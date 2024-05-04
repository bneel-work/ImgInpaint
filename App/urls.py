from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name="homepage"),
    path('process-img', ProcessImg.as_view(), name="process-img"),
    path('view-result/<int:imgID>', ViewResult.as_view(), name="view-result"),
]
