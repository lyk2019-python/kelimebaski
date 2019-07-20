from django.urls import path

from blog.views import listele, goruntule

urlpatterns = [
    path('', listele),
    path('gonderi/<int:gonderi_id>/', goruntule),
]
