from django.shortcuts import render


def runoob(request):
    name = "菜鸟教程"
    return render(request, "runoob.html", {"name": name})
