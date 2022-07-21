from django.shortcuts import render
from .models import Response

def form(request):
    return render(request, 'form/form.html')

def response(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = address.POST['address']
        city = city.POST['city']
        postcode = postcode.POST['postcode']

        information = Response.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            postcode=postcode)

    return render(request, 'form/response.html')