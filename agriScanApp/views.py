from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
@login_required
def home(request):
    return render(request,'agriScanApp/home.html')

def dashboard(request):
    # You can pass context data here if needed
    context = {
        'about_us_data': {
            'title': 'About Us ',
            'content': 'Ensuring the quality and safety of agri-food products is a critical concern for both industry stakeholders and consumers.' 
                       'This website seeks to revolutionize the assessment of agri-food product quality by harnessing cutting-edge technology.'
                       ' In partnership with "Agriculture and Agri-Food Canada / Government of Canada," this website combines image recognition and data analysis techniques.'
                       ' The system can comprehensively evaluate various aspects of leaves, including appearance, texture, color, and structural integrity, to provide real-time and accurate assessments of leaves.',
        },
        'services_data': [
            {'title': ' Leaves Inspection and Testing', 'description': 'Conduct regular inspections of leaves at various stages.  '
                                                                     'Perform quality tests to ensure that leaves meet safety and quality standards.  '
                                                                     'heck for contaminants, pathogens, and adulterants.'},
            # {'title': 'Data Analysis and Reporting:', 'description': 'Collect, analyze, and report data on quality and safety metrics.Use data to make informed decisions and improve processes.'},
            # Add more services as needed
        ],
        # 'contact_us_data':[
        #     {'title': ' Email', 'description': 'raval53@uwindsor.ca'},
        #     {'title': 'Conatct number:', 'description': '6474019762'},
        #     # Add more services as needed
        # ],
    }
    return render(request, 'agriScanApp/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # if user_type == 'Student':
                    # login(request, user)
                    # return redirect('SmartE_app:student_dashboard')  # Redirect to student dashboard
                # elif user_type == 'Professor':
                    # login(request, user)
                    # if user.groups.filter(name='Professor').exists():
                        # return redirect('SmartE_app:course_dashboard')  # Redirect to teacher dashboard
                    # else:
                        # return render(request, 'SmartE_app/login.html', {'form': form, 'error_message': 'Invalid User'})
                login(request, user)
                return redirect('agriScanApp:home')
            else:
                return render(request, 'agriScanApp/login.html', {'form': form, 'error_message': "You don't have an account! Please create one."})
    else:
        form = LoginForm()

    return render(request, 'agriScanApp/login.html', {'form': form})

def registration(request):
    # form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'agriScanApp/registration.html', {'form': form, 'error_message': 'Username already exists. Choose a different one.'})

            # Continue with user creation if the username is unique
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.first_name = name
            user.save()

            login(request, user)  # Automatically log in the user after registration
            return redirect('agriScanApp:home')  # Redirect to the home page or another success page
    else: 
        form = RegistrationForm()

    return render(request, 'agriScanApp/registration.html', {'form': form})

