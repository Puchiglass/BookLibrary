from django.http import HttpResponse
from django.shortcuts import render


def tmp(request):
    return HttpResponse('Hello world')