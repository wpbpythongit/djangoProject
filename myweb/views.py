from django.shortcuts import render


def runoob(request):
    name = "θιΈζη¨"
    return render(request, "runoob.html", {"name": name})
