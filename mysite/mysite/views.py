# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render_to_response

#def here(request):
	#return HttpResponse('媽，我在這!')

def	index(request):
	return render_to_response('index.html', locals())



