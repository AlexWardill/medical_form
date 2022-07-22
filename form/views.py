from django.shortcuts import render
from .models import Response
from nylas import APIClient

def form(request):
    return render(request, 'form/form.html')

# I know that this information should never be just dumped into the application in this way, 
# but I have left it here in order to try the email functionality.
# I looked into storing these as environment variables but didn't have enough time


# CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
# CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
# ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def response(request):
    # Store form data
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        postcode = request.POST['postcode']
        
        # Create new Response object and save to db.
        information = Response.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            postcode=postcode)

    # send email

    # encountered authorization errors

    # nylas = APIClient(
    #     CLIENT_ID,
    #     CLIENT_SECRET,
    #     ACCESS_TOKEN,
    # )
    # draft = nylas.drafts.create()
    # draft.subject = "Medical form submission receipt"
    # draft.body = "Thank you for registering your interest."

    # draft.to = [{'name': name, 'email': email}]

    # draft.send()

    return render(request, 'form/response.html')