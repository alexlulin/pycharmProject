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
    #for obj in queryset:
    #    print(obj.id,obj.name,obj.age,obj.password,obj.create_time.strftime("%Y-%m-%d"),obj.get_gender_display(),obj.depart_id.title)
    return render(request,'user_list.html',{"queryset":queryset})

def user_add(request):
    """人员新增 （原始方法）"""
    if request.method == "GET":
        context={
            'gender_choices':models.UserInfo.gender_choices,
            'depart_list':models.Department.objects.all()
        }
        return render(request,"user_add.html",context)

    # 获取用户提交的数据
    #id=request.POST.get("id")
    name=request.POST.get("user")
    password=request.POST.get("pwd")
    age=request.POST.get("age")
    account=request.POST.get("ac")
    ctime=request.POST.get("ctime")
    gender=request.POST.get("gd")
    depart_id=request.POST.get("dp")
    depart_idz=models.Department.objects.get(id=depart_id)
    models.UserInfo.objects.create(name=name,password=password,age=age,account=account,create_time=ctime,gender=gender,depart_id=depart_idz)
    return redirect("/user/list/")

def user_del(request):
    """删除部门"""
    # 获取id
    '''
    nid=request.POST.get("id")
    user1=models.UserInfo.objects.filter(id=nid).first()
    queryset = user1.delete()
    for obj in queryset:
        print(obj.id,obj.name,obj.age,obj.password,obj.create_time.strftime("%Y-%m-%d"),obj.get_gender_display(),obj.depart_id.title)
    return redirect("/user/list/")
    '''
    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

def user_edit(request,nid):
    """编辑部门"""
    if request.method == "GET":
        row_object=models.UserInfo.objects.filter(id=nid).first()
        #print(row_object.id,row_object.title)
        return render(request,"user_edit.html",{"row_object":row_object})

    models.UserInfo.objects.filter(id=nid).update(title=request.POST.get("nid"))
    return redirect("/user/list/")