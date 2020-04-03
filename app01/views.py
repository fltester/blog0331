from django.shortcuts import render,redirect
from django.views import View
from app01 import models
# Create your views here.


class Login(View):
    def get(self,request):
        return render(request,"login.html")


    def post(self,request):
        #获取表单提交的数据
        user = request.POST.get("username")
        pwd = request.POST.get("password")

        #和数据库的数据对比
        #models.UserInfo.objects.filter(username=user,password=pwd).exists()
        user_obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if user_obj:#用户登录成功
            #return redirect("/index")
            # result = redirect("/index/")
            # result.set_cookie("xxxxxx",user)#基于cookie认证：存放在浏览器上的键值对
            # return result

            #session控制登录
            #session是一种数据存储方式，将数据存放在服务端，django默认存在数据库，在settings文件中可以设置存放的位置
            request.session["user_name"] = user_obj.username #添加、设置session
            request.session["user_id"] = user_obj.pk
            print(user_obj.pk)
            return redirect("/index/")
        else:
            return render(request,"login.html",{"error":"用户名或密码错误"})



#通过类装饰器进行session验证登录
def auth(func):
    def inner(self,request,*args,**kwargs):
        print(dict(request.session))
        user = request.session.get("user_name")  # 读取session  #del request.session["user_name"]删除
        id = request.session.get("user_id")
        if not user:
            return redirect("/login/")

        return func(self,request,*args,**kwargs)
    return inner



class Index(View):
    @auth
    def get(self,request):
        #user = request.COOKIES.get("xxxxxx")
        return render(request, "index.html",)

