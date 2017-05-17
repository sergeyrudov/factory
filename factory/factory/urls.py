from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categories$', views.allcategories),
    url(r'^category-id-([0-9])', views.category),

]
