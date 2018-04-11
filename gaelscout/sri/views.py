from django.shortcuts import render
# from matplotlib import pyplot as plt
# import seaborn as sns
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse, Http404
from teaminfo.models import Teams
from django.template import loader

# Create your views here.
def index(request):
    # sridata = pd.read_pickle("teamfuncs/sridata.pkl")
    # snsplot = sns.lmplot(x='OPR', y='Max Score', data=sridata, fit_reg=True)
    # plt.show()
    # return render(request, 'sri/index.html', {"plot": snsplot})
    return render(request, 'sri/index.html')
