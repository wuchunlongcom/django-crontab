
import os
from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin
from .models import Photo
from django.http.response import HttpResponseRedirect, HttpResponse

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )
   