from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HeartDiagnosesForm
# Import the modules for the ML model
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from .models import DiagosticFeatures
import os
from django.conf import settings

def predictor(input_data=None):
    # load the datasets into a dataframe 
    file_path = os.path.join(settings.BASE_DIR, 'diagnoses_app', 'data', 'dataset.csv')
    dataset = pd.read_csv(file_path)

    # Seperate the dataset into features and target
    X = dataset.drop(columns='Heart Disease', axis=1)
    y = dataset['Heart Disease']

    # Initialize the scaler 
    scaler = StandardScaler()

    # Standardize the features 
    X = scaler.fit_transform(X)

    # Split the dataset into training and testing 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

    # Initialize the classifier 
    classifier = SVC(kernel='linear')

    # Train the model using training data 
    classifier.fit(X_train, y_train)

    # Take data from clinician
    user_input_data = input_data

    # Convert the input supposedly list object to a numpy array
    list_data_as_array = np.asarray(user_input_data)

    # Reshape data for single instance prediction
    reshaped_data_list = list_data_as_array.reshape(1, -1)

    # Tranform data into a standard data
    std_data = scaler.transform(reshaped_data_list)

    # Feed the data into the trained model for prediction
    the_predicted_outcome = classifier.predict(std_data)
    return the_predicted_outcome

queryset = dict(DiagosticFeatures.objects.values().last())
the_list = []
for key, value in queryset.items():
    the_list.append(value)

prediction = predictor(the_list[1:])

# Create your views here.
def welcome(request):
    if request.method=="POST":
        form = HeartDiagnosesForm(request.POST or None)
        if form.is_valid():
            form.save()
            print(request.POST)
        return redirect('welcome')
    else:
        queryset = dict(DiagosticFeatures.objects.values().last())
        the_list = []
        for key, value in queryset.items():
            the_list.append(value)

        prediction = predictor(the_list[1:])
        return render(request, template_name="base.html", context={"forms": HeartDiagnosesForm, "prediction": prediction
                                                                   })
