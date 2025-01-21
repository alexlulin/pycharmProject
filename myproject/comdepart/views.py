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
        return render(request, "depart_add.html")
    #通过页面post 方式获取 title
    title=request.POST.get("title")
    #保存到数据库
    models.Department.objects.create(title=title)
    #重定向回部门列表
    return redirect("/depart/list/")

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

def user_list(request):
    """人员列表"""
    queryset=models.UserInfo.objects.all()
    for obj in queryset:
        print(obj.id,obj.name,obj.age,obj.password,obj.create_time.strftime("%Y-%m-%d"),obj.get_gender_display(),obj.depart_id.title)
    return render(request,'user_list.html',{"queryset":queryset})

def user_add(request):
    """人员新增 （原始方法）"""
    if request.method == "GET":
        context={
            'gender_choices':models.UserInfo.gender_choices,
            'depart_list':models.Department.objects.all()
        }
        return render(request,"user_add.html",context)
    elif request.method == "POST":
    # 获取用户提交的数据
        #id=request.POST.get("id")
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        age=request.POST.get("age")
        ac=request.POST.get("ac")
        ctime=request.POST.get("ctime")
        gd=request.POST.get("gd")
        dp=request.POST.get("dp")
        models.UserInfo.objects.create(id=id,name=user,password=pwd,age=age,account=ac,create_time=ctime,gender=gd,depart_id=dp)
        return redirect("/user/list/")