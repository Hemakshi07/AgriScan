from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
import os
import cv2
import numpy as np
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from .ML import MLModel
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
@login_required
def home(request):
    accuracy = request.session.get('ml_accuracy', None)
    if accuracy is None:
        ml_model = MLModel()
        accuracy = ml_model.get_accuracy()
        request.session['ml_accuracy'] = accuracy

    context = {'accuracy': accuracy}
    return render(request, 'agriScanApp/home.html', context)

def dashboard(request):
    # context = {
    #     'about_us_data': {
    #         'title': 'About Us ',
    #         'content': 'Ensuring the quality and safety of agri-food products is a critical concern for both industry stakeholders and consumers.' 
    #                    'This website seeks to revolutionize the assessment of agri-food product quality by harnessing cutting-edge technology.'
    #                    ' In partnership with "Agriculture and Agri-Food Canada / Government of Canada," this website combines image recognition and data analysis techniques.'
    #                    ' The system can comprehensively evaluate various aspects of leaves, including appearance, texture, color, and structural integrity, to provide real-time and accurate assessments of leaves.',
    #     },
    #     'services_data': [
    #         {'title': ' Leaves Inspection and Testing', 'description': 'Conduct regular inspections of leaves at various stages.  '
    #                                                                  'Perform quality tests to ensure that leaves meet safety and quality standards.  '
    #                                                                  'heck for contaminants, pathogens, and adulterants.'},
    # }
    return render(request, 'agriScanApp/dashboard.html')

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

# def registration(request):
#     # form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             # Check if the username already exists
#             if User.objects.filter(username=username).exists():
#                 return render(request, 'agriScanApp/registration.html', {'form': form, 'error_message': 'Username already exists. Choose a different one.'})

#             # Continue with user creation if the username is unique
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             user = User.objects.create_user(username=username, password=password)
#             user.email = email
#             user.first_name = name
#             user.save()

#             # login(request, user)  # Automatically log in the user after registration
#             return redirect('agriScanApp:login')  # Redirect to the home page or another success page
#     else: 
#         form = RegistrationForm()

#     return render(request, 'agriScanApp/registration.html', {'form': form})

@csrf_protect
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

        ml_accuracy = request.session.get('ml_accuracy', None)
        ml_confusion_matrix = request.session.get('ml_confusion_matrix', None)

        if ml_accuracy is None or ml_confusion_matrix is None:
            ml_model = MLModel()
            y_true, y_pred = ml_model.evaluate_model()
            ml_accuracy = accuracy_score(y_true, y_pred)
            ml_confusion_matrix = confusion_matrix(y_true, y_pred)
            
            request.session['ml_accuracy'] = ml_accuracy
            request.session['ml_confusion_matrix'] = ml_confusion_matrix
            ml_model = MLModel()  # Initialize the ML model
            accuracy = ml_model.get_accuracy()

            # Plotting the Accuracy Graph
            labels = ["Random Forest"]
            values = [accuracy]
            plt.bar(labels, values)
            plt.ylim([0, 1])  # Set y-axis limit to 0-1 for accuracy percentage
            plt.title("Model Accuracy")
            plt.ylabel("Accuracy")
            accuracy_graph_path = 'agriScanApp/static/graph.png'
            plt.savefig('D:/finalProject/agriScan/agriScanApp/plantvillage dataset/graph.png')  # Save the plot as an image in the static folder
            plt.close()

            # Visualize the confusion matrix
            plt.figure(figsize=(10, 8))
            sns.heatmap(ml_confusion_matrix, annot=True, fmt='g', cmap='Blues', xticklabels=np.unique(y_true), yticklabels=np.unique(y_true))
            plt.title('Confusion Matrix')
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            confusion_matrix_path = 'D:/finalProject/agriScan/agriScanApp/static/confusion_matrix.png'
            plt.savefig(os.path.join('D:/finalProject/agriScan/agriScanApp/static', confusion_matrix_path))
            plt.close()

            context = {'accuracy': accuracy}
            # ml_model = MLModel()
            # accuracy = ml_model.get_accuracy()
            # request.session['ml_accuracy'] = accuracy

            login(request, user)  # Automatically log in the user after registration
            return redirect('agriScanApp:home')  # Redirect to the home page or another success page
    else: 
        form = RegistrationForm()

    return render(request, 'agriScanApp/registration.html', {'form': form})