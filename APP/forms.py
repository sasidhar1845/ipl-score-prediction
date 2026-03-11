from django import forms 
from . models import UserPersonalModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserPersonalForm(forms.ModelForm):
    
    class Meta:
        model = UserPersonalModel
        fields = '__all__'
        

from django import forms
from .models import UserPredictModel

TEAM_CHOICES = [
    (0, 'Chennai Super Kings'),
    (1, 'Delhi Capitals'),
    (2, 'Gujarat Titans'),
    (3, 'Kolkata Knight Riders'),
    (4, 'Lucknow Super Giants'),
    (5, 'Mumbai Indians'),
    (6, 'Punjab Kings'),
    (7, 'Rajasthan Royals'),
    (8, 'Royal Challengers Bangalore'),
    (9, 'Sunrisers Hyderabad'),
]

class UserPredictDataForm(forms.ModelForm):
    class Meta:
        model = UserPredictModel
        fields = [
            'batting_team', 'bowling_team', 'venue', 'pitch_condition',
            'temperature', 'humidity', 'overs_completed', 'runs_scored',
            'wickets_lost', 'run_rate', 'last_5_overs_runs', 'striker_strike_rate',
            'non_striker_strike_rate', 'partnership_runs', 'boundaries_hit',
            'extras_conceded'
        ]
        widgets = {
            'batting_team': forms.Select(choices=TEAM_CHOICES, attrs={'class': 'form-control'}),
            'bowling_team': forms.Select(choices=TEAM_CHOICES, attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stadium/Venue'}),
            'pitch_condition': forms.Select(choices=[
                ('Batting Friendly', 'Batting Friendly'),
                ('Bowling Friendly', 'Bowling Friendly'),
                ('Balanced', 'Balanced'),
                ('Spin Friendly', 'Spin Friendly'),
            ], attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Temperature (°C)'}),
            'humidity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Humidity (%)'}),
            'overs_completed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Overs Completed'}),
            'runs_scored': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Runs Scored'}),
            'wickets_lost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wickets Lost'}),
            'run_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current Run Rate'}),
            'last_5_overs_runs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Last 5 Overs Runs'}),
            'striker_strike_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Striker Strike Rate'}),
            'non_striker_strike_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Non-Striker Strike Rate'}),
            'partnership_runs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Partnership Runs'}),
            'boundaries_hit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Boundaries Hit'}),
            'extras_conceded': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Extras Conceded'}),
        }
