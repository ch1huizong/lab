from django.urls import path

from .views import PublisherList, PublisherBookList, AuthorDetailView


urlpatterns = [
    path('publishers/', PublisherList.as_view()),
    path('books/<publisher>/', PublisherBookList.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
