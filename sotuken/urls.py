from django.urls import path
from sotuken import views

urlpatterns = [
    path('',views.kakikomi, name='kakikomi'),
]