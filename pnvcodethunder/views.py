# I have made file
from django.http import HttpResponse
from django.shortcuts import render # using for templates

def index(request): # bydefault take argument request
    return render(request,'index.html')
    #return HttpResponse("hello p")  # return Http resposnce

def analyze(request):
    # get the text
    get_text = request.POST.get('text','default')
    # get checkbox value
    get_removpuc = request.POST.get('removepunc','off')
    get_capitalize = request.POST.get('uppercase','off')
    get_newline = request.POST.get('newlineremove','off')
    get_space = request.POST.get('extraspaceremove','off')
    # check if checkbox on 
    if get_removpuc=="on":
        punc_list = '''!~@#$%^&*()_-=+{[}]\|"';:`,<.>/?'''
        analyzed = ""
        for char in get_text:
            if char not in punc_list:
                analyzed += char
        params = {'purpose':'remove punctiuations',
                'analyze_text':analyzed,
                }
        get_text = analyzed
    if get_capitalize=="on":
        analyzed = ""
        for char in get_text:
            analyzed += char.upper()
        params = {'purpose':'Convert to Uppercase',
                'analyze_text':analyzed,
                }
        get_text = analyzed
    if get_newline=="on":
        analyzed=""
        for char in get_text:
            if char != "\n" and char != "\r":
                analyzed+=char
        params = {'purpose':'Remove New Line',
                'analyze_text':analyzed,
                }
        get_text = analyzed
    if get_space=="on":
        analyzed=""
        for index,char in enumerate(get_text):
            if not(get_text[index]==" " and get_text[index+1]==" "):
                analyzed+=char
        params = {'purpose':'Remove New Line',
                'analyze_text':analyzed,
                }
        get_text = analyzed
    if(get_removpuc!="on" and get_capitalize!="on" and get_newline!="on" and get_space!="on"):
        return HttpResponse("<script>window.alert('Do not select any checkbox: Please try again')</script>")
    return render(request,'analyze.html',params)
