from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    return render(request, "hello/index.html")

# def bymongolian(request):
#     return HttpResponse("Сайн байна уу")

# def bychinese(request):
#     return HttpResponse("你好")

# def greetings(request, language):
#     if "mongolian" in language:
#         return HttpResponse("Сайн байна уу")
#     elif "chinese" in language:
#         return HttpResponse("你好")
#     else:
#         return HttpResponse("Hello")
    
def greetings(request, language):
    if "english" in language:
        return render(request, "hello/greetings.html", 
                      {"value": "Hello, Hello, Hello", 
                       "type": "English", 
                       "items": ["one", "two", "three"]})
    