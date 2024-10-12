import requests
from django.shortcuts import render
from .models import VisitorInfo

def get_client_ip(request):
    # Get client IP address from request
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def track_visitor(request):
    ip = get_client_ip(request)

    # Use ipstack API to get location data (signup for a free API key at https://ipstack.com/)
    api_key = 'your_ipstack_api_key'
    url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    response = requests.get(url)
    location_data = response.json()

    # Save visitor data to the database
    visitor = VisitorInfo(
        ip_address=ip,
        city=location_data.get('city'),
        region=location_data.get('region_name'),
        country=location_data.get('country_name'),
        latitude=location_data.get('latitude'),
        longitude=location_data.get('longitude')
    )
    visitor.save()

    return render(request, 'tracker/visitor_info.html', {'visitor': visitor})
