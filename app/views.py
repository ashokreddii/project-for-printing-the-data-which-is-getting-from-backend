from django.shortcuts import render


# Create your views here.
def jinja_print(request):
    d={'name':'ashok reddy','age':23}
    return render(request,'jinja_print.html',context=d)

