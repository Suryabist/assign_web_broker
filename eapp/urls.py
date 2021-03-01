from django.urls import path

from eapp.views import ProductListView, ProductDetailView, ProductOrderView

app_name = "eapp"
urlpatterns = [
    path('product/list', ProductListView.as_view(), name='productlist'),
    path('product/<int:pk>/order', ProductDetailView.as_view(), name='productdetail'),
    path('order/product/id/<int:pk>', ProductOrderView.as_view(), name='orderproduct')
]
