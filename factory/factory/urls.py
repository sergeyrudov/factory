from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.allcategories),
    url(r'^category/([0-9])', views.category),
    url(r'^factory/([0-9])',views.factory )

]
