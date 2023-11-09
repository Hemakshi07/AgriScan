from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# def dashboard(request):
#     return render(request, 'agriScanApp/dashboard.html')
# context = {
#         'about_us_data': {
#             'title': 'About Us Title',
#             'content': 'About Us Content',
#         },
# def aboutus(request):
#     aboutus_data ='Ensuring the quality and safety of agri-food products is a critical concern for both industry stakeholders and consumers. The "Food Quality Assurance: Implementing Image Recognition and Data Analysis" project seeks to revolutionize the assessment of agri-food product quality by harnessing cutting-edge technology. In partnership with "Agriculture and Agri-Food Canada / Government of Canada," this collaborative project will develop an innovative system that combines image recognition and data analysis techniques. The system will comprehensively evaluate various aspects of agri-food products, including appearance, texture, color, and structural integrity, to provide real-time and accurate assessments of product quality. '
#     return render(request, 'agriScanApp/aboutus.html',aboutus_data)

# def contactus(request):
#     # contact_us_data = ContactUs.objects.first()
#     return render(request,'agriScanApp/contactus.html')

# def services(request):
#     # services_data = Service.objects.all()
#      return render(request,'agriScanApp/services.html')
# def login(request):
#     # services_data = Service.objects.all()
#      return render(request,'agriScanApp/login.html')

def dashboard(request):
    # You can pass context data here if needed
    context = {
        'about_us_data': {
            'title': 'About Us ',
            'content': 'Ensuring the quality and safety of agri-food products is a critical concern for both industry stakeholders and consumers.' 
                       'The "Food Quality Assurance: Implementing Image Recognition and Data Analysis" project seeks to revolutionize the assessment of agri-food product quality by harnessing cutting-edge technology.'
                       ' In partnership with "Agriculture and Agri-Food Canada / Government of Canada," this collaborative project will develop an innovative system that combines image recognition and data analysis techniques.'
                       ' The system will comprehensively evaluate various aspects of agri-food products, including appearance, texture, color, and structural integrity, to provide real-time and accurate assessments of product quality. ',
        },
        'services_data': [
            {'title': ' Food Inspection and Testing', 'description': 'Conduct regular inspections of food products at various stages of production.  '
                                                                     'Perform quality tests to ensure that food products meet safety and quality standards.  '
                                                                     'heck for contaminants, pathogens, and adulterants.'},
            # {'title': 'Data Analysis and Reporting:', 'description': 'Collect, analyze, and report data on quality and safety metrics.Use data to make informed decisions and improve processes.'},
            # Add more services as needed
        ],
        'contact_us_data':[
            {'title': ' Email', 'description': 'raval53@uwindsor.ca'},
            {'title': 'Conatct number:', 'description': '6474019762'},
            # Add more services as needed
        ],
    }
    return render(request, 'agriScanApp/dashboard.html', context)

def login_view(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user_type = form.cleaned_data['user_type']

    #         # Authenticate user
    #         user = authenticate(request, username=username, password=password)

    #         if user is not None:
                
    #             if user_type == 'Student':
    #                 login(request, user)
    #                 return redirect('agriScanApp:student_dashboard')  # Redirect to student dashboard
    #             elif user_type == 'Professor':
    #                 login(request, user)
    #                 if user.groups.filter(name='Professor').exists():
    #                     return redirect('agriScanApp:course_dashboard')  # Redirect to teacher dashboard
    #                 else:
    #                     return render(request, 'agriScanApp/login.html', {'form': form, 'error_message': 'Invalid User'})
    # else:
    #     form = LoginForm()

    return render(request, 'agriScanApp/login.html')

def registration(request):
    # if request.method == 'POST':
    #     # form = CustomUserCreationForm(request.POST)
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         sid = form.cleaned_data['sid']
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         membership_type = form.cleaned_data['membership_type']

    #         user = User.objects.create_user(username=username, password=password)
    #         user.email = email
    #         user.first_name = name
    #         user.save()

    #         return redirect('agriScanApp:login')  # Redirect to a success page
    # else:
    #     # form = CustomUserCreationForm()
    #     form = RegistrationForm()

    return render(request, 'agriScanApp/registration.html')

