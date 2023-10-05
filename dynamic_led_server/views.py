from django.http import JsonResponse
from django.shortcuts import render,redirect
import datetime
import random
import pandas as pd

def index(request):    
    df = pd.DataFrame({'Column1': [1, 20, 3], 'Column2': ['A', 'B', 'C']})
    
    # Convert the DataFrame to HTML using Pandas' to_html method
    df_html = df.to_html(classes='table table-bordered table-striped table-container')    
    return render(request,'index.html',context={'df_html':df_html})

def load_rs232(request, width, height):
    return render(request,template_name='rs232.html',context={'width':width,'height':height})