from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Community
 
# Create your views here.
 
def Import_Excel_Pandas(request):

    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        impexceldata = pd.read_excel(filename)
        dbframe = impexceldata
        for dbframe in dbframe.itertuples():
            obj = Community.objects.create(Name=dbframe.Name, Type=dbframe.Type, Parish=dbframe.Parish,
                                            ParishCode=dbframe.ParishCode, Longitude=dbframe.Longitude,
                                            Latitude=dbframe.Latitude)

            obj.save()
            print(dbframe)

        messages.add_message(request, messages.INFO, 'Form submitted successfully.')

        return render(request, 'GEOs.html', {
                'uploaded_file_url': uploaded_file_url
            })

    return render(request, 'GEOs.html',{})