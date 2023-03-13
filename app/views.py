from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'charishma','age':3}
    return render(request,'jinja_print.html',context=d)
