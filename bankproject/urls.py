"""bankproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('show',views.show,name='show'),
    path('create',views.create,name='create'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    path('attendance',views.attendance,name='attendance'),
    path('atcreate',views.atcreate,name='atcreate'),
    path('atupdate/<staff_id>',views.atupdate,name='atupdate'),
    path('atdelete/<staff_id>',views.atdelete,name='atdelete'),
    path('s_documents',views.s_documents,name='s_documents'),
    path('sdoccreate',views.sdoccreate,name='sdoccreate'),
    path('sdocupdate/<emp_id>',views.sdocupdate,name='sdocupdate'),
    path('sdocdelete/<emp_id>',views.sdocdelete,name='sdocdelete'),
    path('leave',views.leave,name='leave'),
    path('leavecreate',views.leavecreate,name='leavecreate'),
    path('leaveupdate/<id>',views.leaveupdate,name='leaveupdate'),
    path('leavedelete/<id>',views.leavedelete,name='leavedelete'),
    path('holiday',views.holiday,name='holiday'),
    path('holidaycreate',views.holidaycreate,name='holidaycreate'),
    path('holidayupdate/<id>',views.holidayupdate,name='holidayupdate'),
    path('holidaydelete/<id>',views.holidaydelete,name='holidaydelete'),
    path('service',views.service,name='service'),
    path('c_details',views.c_details,name='c_details'),
    path('c_create',views.c_create,name='c_create'),
    path('c_update/<id>',views.c_update,name='c_update'),
    path('c_delete/<id>',views.c_delete,name='c_delete'),
    path('c_documents',views.c_documents,name='c_documents'),
    path('c_doccreate',views.c_doccreate,name='c_doccreate'),
    path('c_docupdate/<cust_id>',views.c_docupdate,name='c_docupdate'),
    path('c_docdelete/<cust_id>',views.c_docdelete,name='c_docdelete'),
    path('accounts',views.accounts,name='accounts'),
    path('accreate',views.accreate,name='accreate'),
    path('acupdate/<id>',views.acupdate,name='acupdate'),
    path('acdelete/<id>',views.acdelete,name='acdelete'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('passbook',views.passbook,name='passbook'),
    path('pbcreate',views.pbcreate,name='pbcreate'),
    path('pbupdate/<id>',views.pbupdate,name='pbupdate'),
    path('pbdelete/<id>',views.pbdelete,name='pbdelete'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('deposit',views.deposit,name='deposit'),


]
