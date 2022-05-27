from django.urls import path
from REST.api.viewest import homeList, homeDetail

urlpatterns = [
    path('', homeList.as_view(), name='home_list'),
    path('<int:pk>/', homeDetail.as_view(), name='home_detail')
]