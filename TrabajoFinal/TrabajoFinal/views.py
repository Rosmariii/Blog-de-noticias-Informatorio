from django.shortcuts import render


def nosotros(request):
	return render(request,"nosotros.html")

#def login(request):
#	return render(request,"login.html")

def base(request):
	return render(request,"base.html")