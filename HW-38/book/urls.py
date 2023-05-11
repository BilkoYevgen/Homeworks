from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # path('books/', BookListView.as_view(), name='book_list'),
    # path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    # path('add-book/', create_book, name='book_create'),
    # path('booklist/', BookAPIView.as_view()),
    path('api/', include(router.urls)),
]