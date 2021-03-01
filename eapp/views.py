from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from eapp.forms import OrderForm
from eapp.models import Product
from eapp.tasks import new_order


class ProductListView(ListView):
    template_name = 'clienttemplates/packagelist.html'
    queryset = Product.objects.all().order_by('-id')
    context_object_name = 'itemlist'
    paginate_by = 6


class ProductDetailView(DetailView):
    template_name = 'clienttemplates/packagedetail.html'
    model = Product
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm
        return context


class ProductOrderView(CreateView, SuccessMessageMixin):
    template_name = 'clienttemplates/packagedetail.html'
    form_class = OrderForm
    success_message = "Thank You for ordering. Your order has been placed Successfully"

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']

        new_order.delay(name, phone)

        account_sid = 'AC3cbfa74e4e206083aa8763abca8ac344'
        auth_token = '1bfe85c8a97690da6dc26647ccf19eb7'
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(to="+977" + phone, from_="981927990", body="Dear CUstomer, Your order "
                                                                                        "has been successfully placed")
        except TwilioRestException as e:
            print(e)

        return super().form_valid(form)

    def get_success_url(self):
        return "/product/" + str(self.kwargs['pk']) + "/order"
