from django.db import models
from django.contrib.auth.models import User


class UserPersonalModel(models.Model):


    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)   
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


def __str__(self):
    return self.firstname, self.lastname, self.age,self.address,self.phone,self.city,self.state,self.country




from django.db import models
from django.utils import timezone

TEAM_MAPPING = {
    'Chennai Super Kings': 0,
    'Delhi Capitals': 1,
    'Gujarat Titans': 2,
    'Kolkata Knight Riders': 3,
    'Lucknow Super Giants': 4,
    'Mumbai Indians': 5,
    'Punjab Kings': 6,
    'Rajasthan Royals': 7,
    'Royal Challengers Bangalore': 8,
    'Sunrisers Hyderabad': 9
}

class UserPredictModel(models.Model):
    batting_team = models.IntegerField()  # store number
    bowling_team = models.IntegerField()  # store number
    venue = models.CharField(max_length=150)
    pitch_condition = models.CharField(max_length=50)
    temperature = models.FloatField()
    humidity = models.FloatField()
    overs_completed = models.FloatField()
    runs_scored = models.IntegerField()
    wickets_lost = models.IntegerField()
    run_rate = models.FloatField()
    last_5_overs_runs = models.IntegerField()
    striker_strike_rate = models.FloatField()
    non_striker_strike_rate = models.FloatField()
    partnership_runs = models.IntegerField()
    boundaries_hit = models.IntegerField()
    extras_conceded = models.IntegerField()
    Label = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
