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
        if user_obj:
            return redirect("/index/")
        else:
            return render(request,"login.html",{"error":"用户名或密码错误"})




class Index(View):
    def get(self,request):
        return  render(request,"index.html")