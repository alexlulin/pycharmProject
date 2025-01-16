from django.shortcuts import render,redirect
from comdepart import models
# Create your views here.
def depart_list(request):
    """部门列表"""
    """从数据库中获取数据"""
    queryset=models.Department.objects.all()
    return render(request,"depart_list.html",{"queryset":queryset})

def depart_add(request):
    """添加部门"""
    if request.method == "GET":
    #name=models.Department.objects.get("title")
    #models.Department.objects.create(title=name)
        return render(request,"depart_add.html")

    title=request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/add/")