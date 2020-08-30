from django.shortcuts import render

def another(request):
    return render(request,'another/mytemplate.html')
