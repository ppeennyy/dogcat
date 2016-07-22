# -*- coding: utf-8 -*-
from django.http import HttpResponse

def here(request):
	return HttpResponse('媽，我在這!')


