from django.shortcuts import render
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
    return render(request, 'agriScanApp/dashboard.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('agriScanApp:home')
            else:
                return render(request, 'agriScanApp/login.html', {'form': form, 'error_message': "You don't have an account! Please create one."})
    else:
        form = LoginForm()

    return render(request, 'agriScanApp/login.html', {'form': form})

@csrf_protect
def registration(request):
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

            login(request, user)  # Automatically log in the user after registration
            return redirect('agriScanApp:home')  # Redirect to the home page or another success page
    else: 
        form = RegistrationForm()

    return render(request, 'agriScanApp/registration.html', {'form': form})

@login_required
def get_user_details(request):
    user = request.user
    data = {
        'name': user.name,
        'username': user.username,
        'email': user.email,
        
    }
    return JsonResponse(data)


def charts(request):
    return render(request,'agriScanApp/charts.html')


def chartsView(request):
   chart_data = [
    {'label': 'Apple___Apple_scab', 'value': 10},
    {'label': 'Apple___Black_rot', 'value': 15},
    {'label': 'Apple___Cedar_apple_rust', 'value': 8},
    {'label': 'healthy', 'value': 20},
    {'label': 'Soybean___healthy', 'value': 27},
    {'label': 'Squash___Powdery_mildew', 'value': 10},
    {'label': 'Strawberry___healthy', 'value': 26},
    {'label': 'Strawberry___Leaf_scorch', 'value': 7},
    {'label': 'Tomato___Bacterial_spot', 'value': 13},
    {'label': 'Tomato___Early_blight', 'value': 16},
    {'label': 'Tomato___healthy', 'value': 30},
    {'label': 'Tomato___Late_blight', 'value': 14},
    {'label': 'Tomato___Leaf_Mold', 'value': 8},
    {'label': 'Tomato___Septoria_leaf_spot', 'value': 12},
    {'label': 'Tomato___Spider_mites Two-spotted_spider_mite', 'value': 9},
    {'label': 'Tomato___Target_Spot', 'value': 11},
    {'label': 'Tomato___Tomato_mosaic_virus', 'value': 6},
    {'label': 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'value': 7}]
   labels = [data['label'] for data in chart_data]
   values = [data['value'] for data in chart_data]
   
   chart_data2 = [
    {'label1': 'January', 'value': 15},
    {'label1': 'February', 'value': 28},
    {'label1': 'March', 'value': 32},
    {'label1': 'April', 'value': 19},
    {'label1': 'May', 'value': 45},
    {'label1': 'June', 'value': 60},
    {'label1': 'July', 'value': 55},
    {'label1': 'August', 'value': 72},
    {'label1': 'September', 'value': 85},
    {'label1': 'October', 'value': 62},
    {'label1': 'November', 'value': 45},
    {'label1': 'December', 'value': 30},]
   values1 = [data['value'] for data in chart_data2]
   chart_data3 = [
    {'label1': 'January', 'value': 5},
    {'label1': 'February', 'value': 18},
    {'label1': 'March', 'value': 31},
    {'label1': 'April', 'value': 29},
    {'label1': 'May', 'value': 50},
    {'label1': 'June', 'value': 30},
    {'label1': 'July', 'value': 15},
    {'label1': 'August', 'value': 62},
    {'label1': 'September', 'value': 55},
    {'label1': 'October', 'value': 12},
    {'label1': 'November', 'value': 85},
    {'label1': 'December', 'value': 50},]
   labels1 = [data['label1'] for data in chart_data2]
   values3 = [data['value'] for data in chart_data3]
   return render(request, 'agriScanApp/charts.html',  {
        'labels': labels,
        'data': values,
        'labels1':labels1,
        'data1':values1,
        'data2':values3
    })