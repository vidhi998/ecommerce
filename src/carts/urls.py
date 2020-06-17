from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.CartCreateView.as_view(), name='create_cart'),
    url(r'^view/$', views.CartDetailView.as_view(), name='cart_detail'),
    url(r'^checkout/$', views.CheckoutView.as_view(), name='cart_checkout'),
    url(r'^orders/', include('orders.urls')),
]