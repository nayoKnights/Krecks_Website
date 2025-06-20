from django.shortcuts import render, redirect, get_object_or_404
from .models import Flavor, Order
from .forms import OrderForm
import requests
import urllib.parse
from django.contrib.auth.models import User



# Dummy function to simulate SMS sending
# Replace with your real API later
def send_sms(phone_number, message):
    api_key = "YWlOYVpSVGNPSVFSRE10SlVITUk"
    sender_id = "Krecks"
    base_url = "https://sms.arkesel.com/sms/api"
    encoded_message = urllib.parse.quote(message)
    url = f"{base_url}?action=send-sms&api_key={api_key}&to={phone_number}&from={sender_id}&sms={encoded_message}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("SMS sent:", response.text)
    except requests.RequestException as e:
        print("SMS failed:", e)



def home(request):
      # TEMPORARY SUPERUSER CREATION
    if not User.objects.filter(username='krecks').exists():
        User.objects.create_superuser('krecks', 'nayoemc2@gmail.com', 'vandross')
    flavors = Flavor.objects.all()
    return render(request, 'orders/home.html', {'flavors': flavors})

def order_view(request, flavor_id):
    flavor = get_object_or_404(Flavor, pk=flavor_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            message = f"Great choice!\nYour order of {order.quantity} x {order.flavor.name} is on the way.\nThank you for patronizing Krecks."
            send_sms(order.phone_number, message)

            return render(request, 'orders/success.html', {'order': order})
    else:
        form = OrderForm(initial={'flavor': flavor})
    return render(request, 'orders/order.html', {'form': form, 'flavor': flavor})
