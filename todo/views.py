#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Todo

class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = "latest_todo_list"

    def get_queryset(self):
        """
        Return the last ten published todo (not including those set to be
        published in the future).
        """
        return Todo.objects.filter(
            pubtime__lte=timezone.now()
        ).order_by('-pubtime')[:10]
