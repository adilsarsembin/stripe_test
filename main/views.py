from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

import stripe
import environ

from .models import Item

# Create your views here.

env = environ.Env()
environ.Env.read_env()

stripe.api_key = env('STRIPE_KEY')
MY_DOMAIN = 'http://127.0.0.1:8000'


class GetItemView(View):
    model = Item
    template_name = 'main/item.html'

    def get(self, request, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        context = {'item': item}

        return render(request, self.template_name, context)

    


class CreateCheckoutSessionView(View):
    pass

class BuyItem(View):

    stripe_session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'{MY_DOMAIN}/success',
        cancel_url=f'{MY_DOMAIN}/cancel',
    )

    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'id': self.stripe_session.id
        })

    def post(self, request, *args, **kwargs):
        return redirect(self.stripe_session.url, code=303)


class SuccessPaymentView(TemplateView):
    template_name = 'main/success.html'


class FailedPaymentView(TemplateView):
    template_name = 'main/cancel.html'
