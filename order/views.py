from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from order.models import Order
# Create your views here.
#List
#detail


class DetailOrder(DetailView):
    model = Order
    template_name = 'order/detail.html'


class ListOrder(ListView):
    model = Order
    template_name = 'order/list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return super(ListOrder, self).get_queryset().filter(user=user, email=user.email)
