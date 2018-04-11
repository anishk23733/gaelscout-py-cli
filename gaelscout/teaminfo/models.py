from django.db import models
import numpy as np
import pandas as pd
import pickle
# Create your models here.
class worldsTeams(models.Model):
    names = models.CharField(max_length=200)
    events = models.CharField(max_length=200)
    ranks = models.DecimalField(max_digits=10, decimal_places=2)
    wlts = models.CharField(max_length=200)
    wpsps = models.CharField(max_length=200)
    mscores = models.DecimalField(max_digits=10, decimal_places=2)
    oprs = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.team_number
# data = pd.read_pickle('static/divisiondata/teamList.pkl')
# for i in data:
#     w = worldsTeams(names=)
#     w.save

class Teams(models.Model):
    team_number = models.CharField(max_length=200)
    team_opr = models.DecimalField(max_digits=10, decimal_places=2)
    team_mscore = models.DecimalField(max_digits=10, decimal_places=2)
    team_opr_quantile = models.DecimalField(max_digits=10, decimal_places=2)
    team_mscore_quantile = models.DecimalField(max_digits=10, decimal_places=2)
    # pub_date = models.DateTimeField('date published')
    def __str__(self):
            return self.team_number
    class Meta:
        ordering = ["-team_opr_quantile"]
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Team, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#             return self.question_text
