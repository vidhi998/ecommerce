from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^address/$', views.AddressFormView.as_view(), name='address'),
    url(r'^address/add/$', views.UserAddressCreateView.as_view(), name='add_address'),
    url(r'^address/confirm/$', views.ConfirmOrderView.as_view(), name='confirm_order'),
    url(r'^orders/$', views.OrdersList.as_view(), name='order_list'),
]