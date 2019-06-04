# -*- coding:UTF-8 -*-

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from books.models import Publisher, Book, Author


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


class PublisherDetail(DetailView):
    #model = Publisher
    context_object_name = 'my_favorite_publishers'
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_list.html'


class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context
 
   
class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        object = super().get_object()
        object.last_accessed = timezone.now() # 更新每个作者的最后一个字段
        object.save()
        return object
