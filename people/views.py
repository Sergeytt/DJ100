from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def hello(request):
#    return HttpResponse("Hello Django!")

def hello(request):
	return render(request, 'index.html')

#def hello_python(request, some):
#    return HttpResponse("Hello python!! " + some)

def hello_python(request):
	return render(request, 'python.html')

def http(request):
	print(request.path)
	print(request.method)
	print(request.POST)
	print(request.GET)
	response = render(request, 'http.html')
	print(response)
	return response

def sum_two(request, a, b):
	s = int(a) + int(b)
	print(a)
	print(b)
	return HttpResponse(s)

