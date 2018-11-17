from django.http import HttpResponse
from django.shortcuts import render
from app25.forms import StudentForms


def showIndex(request):
    if request.method == "POST":
        sf= StudentForm(request.POST,request.FILES)
        if sf.is_valid():
            f = request.FILES('file')
            with open("app25/static/upload/"+f.name,"wb+")as des:
                for x in f.chunks():
                    des.write(x)
            return HttpResponse("File Uploaded")
        else:
             sf= StudentForm()
             return render(request,"index.html",{"form":sf})
