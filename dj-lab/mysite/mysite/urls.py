from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bands/', include('bands.urls')),
    path('news/', include('news.urls')),

    path('polls/', include('polls.urls')),
    path('author-polls/', include('polls.urls', namespace='author-polls')),
    path('publisher-polls/', include('polls.urls', namespace='publisher-polls')),
    path('polls-api/', include('polls_api.urls')),

    path('books/', include('books.urls')),

    path('admin/', admin.site.urls),
]
