from django.urls import path

from .views import (
    SuccessPaymentView, FailedPaymentView, GetItemView,
    CreateCheckoutSessionView, BuyItem
)


urlpatterns = [
    path('buy/<int:pk>', BuyItem.as_view(), name='buy_item'),
    path('item/<int:pk>', GetItemView.as_view(), name='get_item'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='stripe_session'),
    path('success/', SuccessPaymentView.as_view(), name='success'),
    path('cancel/', FailedPaymentView.as_view(), name='failure'),
]
