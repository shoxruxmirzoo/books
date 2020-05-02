from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('books', views.BooksViewSet)
router.register('lib-users', views.LibUserViewSet)
router.register('rented-books', views.RentBookViewSet)
