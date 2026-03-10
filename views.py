from django.shortcuts import render, redirect

from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib
from geopy.geocoders import Nominatim

def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request,'4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import base64
from io import BytesIO
from django.shortcuts import render
from .forms import UserPredictDataForm
from .models import UserPredictModel

# Load trained IPL prediction model
Model1 = joblib.load('APP/IPL2.pkl')

def model(request):
    if request.method == "POST":
        form = UserPredictDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Form Data:", data)

            # Extract features
            int_features = [
                data['batting_team'],
                data['bowling_team'],
                data['venue'],
                data['pitch_condition'],
                data['temperature'],
                data['humidity'],
                data['overs_completed'],
                data['runs_scored'],
                data['wickets_lost'],
                data['run_rate'],
                data['last_5_overs_runs'],
                data['striker_strike_rate'],
                data['non_striker_strike_rate'],
                data['partnership_runs'],
                data['boundaries_hit'],
                data['extras_conceded'],
            ]
            print("Input Features:", int_features)

            # Convert to numpy array for prediction
            final_features = np.array(int_features, dtype=object).reshape(1, -1)
            print("Final Features:", final_features)

            # Predict
            prediction = Model1.predict(final_features)
            output = prediction[0]
            print("Prediction Output:", output)

            # Save to database
            record = UserPredictModel(
                batting_team=data['batting_team'],
                bowling_team=data['bowling_team'],
                venue=data['venue'],
                pitch_condition=data['pitch_condition'],
                temperature=data['temperature'],
                humidity=data['humidity'],
                overs_completed=data['overs_completed'],
                runs_scored=data['runs_scored'],
                wickets_lost=data['wickets_lost'],
                run_rate=data['run_rate'],
                last_5_overs_runs=data['last_5_overs_runs'],
                striker_strike_rate=data['striker_strike_rate'],
                non_striker_strike_rate=data['non_striker_strike_rate'],
                partnership_runs=data['partnership_runs'],
                boundaries_hit=data['boundaries_hit'],
                extras_conceded=data['extras_conceded'],
                Label=output
            )
            record.save()

            # Create feature list for graph
            categories = [
                'temperature', 'humidity', 'overs_completed',
                'runs_scored', 'wickets_lost', 'run_rate',
                'last_5_overs_runs', 'striker_strike_rate',
                'non_striker_strike_rate', 'partnership_runs',
                'boundaries_hit', 'extras_conceded'
            ]
            numeric_values = [
                data['temperature'], data['humidity'], data['overs_completed'],
                data['runs_scored'], data['wickets_lost'], data['run_rate'],
                data['last_5_overs_runs'], data['striker_strike_rate'],
                data['non_striker_strike_rate'], data['partnership_runs'],
                data['boundaries_hit'], data['extras_conceded']
            ]

            # Plot result
            plt.figure(figsize=(10, 6))
            sns.barplot(x=categories, y=numeric_values, color='skyblue')
            plt.xticks(rotation=45, ha='right')
            plt.title(f'IPL Match Prediction: {output}', fontsize=14)
            plt.xlabel('Match Features')
            plt.ylabel('Values')

            buffer = BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            plt.close()

            return render(request, 'result.html', {
                'prediction_text': f'The Predicted Match Outcome / Score is: {output}',
                'plot_base64': plot_base64
            })
        else:
            print("Form Invalid:", form.errors)
    else:
        form = UserPredictDataForm()

    return render(request, 'model.html', {'form': form})









from APP.models import UserPredictModel
     
def Per_Database_10(request):
    models = UserPredictModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('/')
