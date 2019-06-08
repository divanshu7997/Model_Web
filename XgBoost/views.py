from django.shortcuts import render
from collections import defaultdict
import pandas as pd
import os
from django.conf import settings
from django.http import HttpResponse
from joblib import load, dump
import numpy as np

ppat = 'D:/2/models/Model_Web/XgBoost/templates/XgBoost'
def home(request):
    return render(request, 'XgBoost/index.html')


def op1(request):
    if request.method=='POST':
        try:
            file = request.FILES['excel']
            df = pd.read_csv(file)
            clmn = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13',
           'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22', 'T23',
           'T24', 'T25', 'T26', 'T27', 'T28']
            rst_clmn = []
            for i in df.columns:
                if i not in clmn:
                    rst_clmn.append(i)
            df = df.drop(rst_clmn, axis = 1)
            val = load('XgBoost/Results/solution.joblib')
            df = df.as_matrix()
            pred = val['RandonForest@#'].predict(df)

            return render(request, 'XgBoost/index_o.html', {'con_recommendation': pred})
        except:
            return render(request, 'XgBoost/index_2.html')


def op2(request):
    return render(request, 'XgBoost/SmartControlsAssignment.html')