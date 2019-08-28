# -*- coding: utf-8 -*-
"""
time:2019/8/28 18:56
"""
from django.shortcuts import render


# from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def count(request):
    total_count = len(request.GET["message"])
    input_message = request.GET["message"]
    words = {}
    for word in input_message:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return render(request, "count.html", {
        "total_count": total_count,
        "input_message": input_message,
        "words": words
    })
