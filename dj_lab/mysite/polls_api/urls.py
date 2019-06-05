from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from .views import (
    PollViewSet, ChoiceList, CreateVote, 
    UserCreate, LoginView,
)
                

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),

    path('swagger-docs/', schema_view),
    path('docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls