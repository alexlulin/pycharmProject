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
    #if request.method == "POST":
    #name=models.Department.objects.get("title")
    #models.Department.objects.create(title=name)
     #   return render(request,"depart_add.html")

    title=request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/add/")

def depart_del(request):
    """删除部门"""
    # 获取id
    nid=request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")

def depart_edit(request,nid):
    """编辑部门"""
    if request.method == "GET":
        row_object=models.Department.objects.filter(id=nid).first()
        #print(row_object.id,row_object.title)
        return render(request,"depart_edit.html",{"row_object":row_object})

    models.Department.objects.filter(id=nid).update(title=request.POST.get("title"))
    return redirect("/depart/list/")