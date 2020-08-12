from django.urls import path
from django.conf.urls import url
from . import views
from .views import fait_csv, some_pdf, PdfExtraction

urlpatterns = [
    path('csv/', fait_csv, name='fait_csv'),
    path('pdf/<int:pk>/', some_pdf, name='some_pdf'),
    path('index.html', PdfExtraction, name='listearticles'),
]

