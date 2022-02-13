from django.urls import path

from . import views
from .views import addbus

urlpatterns = [
    path('SFE/',views.sfe,name="SFE"),
    path('SFE/test',views.test,name="test"),
    path('SFE/searchresult',views.searchresult,name="searchresult"),
    path('SFE/addbus',addbus.as_view(),name="ADDBUS"),
    path('SFE/scedule/<int:ID>',views.scedule,name="scedule"),
    path('SFE/searchresult/scedule/<int:ID>',views.scedule,name="scedule2"),

]