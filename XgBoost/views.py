from django.shortcuts import render
from collections import defaultdict
import pandas as pd
import os
from django.conf import settings
from django.http import HttpResponse

ppat = 'D:/2/models/Model_Web/XgBoost/templates/XgBoost'
def home(request):
    return render(request, 'XgBoost/index.html')


def op1(request):
    if request.method=='POST':
        # try:
        file = request.FILES['excel']
        df = pd.read_excel(file)

        return render(request, 'XgBoost/index_o.html', {'con_recommendation': [1]*10})
        # except:
        #     return render(request, 'XgBoost/index_2.html')

# path = 'file:///K:/pras/django/Elucidata/api/Results/result2.xlsx'

import os, tempfile, zipfile
from wsgiref.util import FileWrapper
from django.conf import settings
import mimetypes

# f = 'D:/2/models/Model_Web/XgBoost/Results/'
f = 'XgBoost/'

def download_1(request):
    file_path= f+"op1_result.xlsx" # Select your path of file here.
    download_name ="op1_result1.xlsx"
    # if os.path.exists(file_path):
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    # else:
    #     print('Not Working')