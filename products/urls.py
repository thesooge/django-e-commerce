from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductLists.as_view(), name='product-list'),
    path('<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('comment/<int:pk>',views.ProductComments.as_view(), name='product-comment')
]
