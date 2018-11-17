import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def createcsv(request):
    http=HttpResponse(content_type="text/csv")
    http['content-disposition']='attachment; filename="employee.csv"'
    wr = csv.writer(http)
    wr.writerow([101,"ravi","developer",12500.00])
    wr.writerow([102, "kumar", "developer", 18500.00])
    wr.writerow([103, "krish", "TL", 12600.00])
    return http