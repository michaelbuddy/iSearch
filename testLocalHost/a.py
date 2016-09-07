#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.shortcuts import render
import time

def hello(request):
    return HttpResponse("Hello world！ This is my first trial. ")
def current_time(request):
	return HttpResponse("Current time is:" + time.strftime('%Y-%m-%d %H:%M:%S'))
def test_html(request):
	#return render_to_response("test.html",context_instance=RequestContext(request)) 
	return render_to_response("test.html",locals()) 
def user_info(request):
    name = 'zbw'
    age = 24
    #t = get_template('user_info.html')
    #html = t.render(Context(locals()))
    #return HttpResponse(html)
    return render_to_response('user_info.html',locals())	
def user_info1(request):
    name = 'zbw'
    age = 24
    return render_to_response('user_info1.html',locals())
def product_info(request):
    productName = '青霉素'
    #return render_to_response('product_info.html',locals())	    
    return render_to_response('product_info.html',{'productName':productName})
def search(request):    
    return render_to_response('search.html',locals())