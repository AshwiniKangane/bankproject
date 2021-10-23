from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm
from django.contrib import messages


from bankapp.forms import S_Details
from bankapp.forms import SdForm
from bankapp.forms import Attendance
from bankapp.forms import AttendanceForm
from bankapp.forms import S_Documents
from bankapp.forms import S_DocumentsForm
from bankapp.forms import Leave
from bankapp.forms import LeaveForm
from bankapp.forms import Holiday
from bankapp.forms import HolidayForm
from bankapp.forms import C_Details
from bankapp.forms import C_DetailsForm
from bankapp.forms import C_Documents
from bankapp.forms import C_DocumentsForm
from bankapp.forms import AccForm
from bankapp.forms import Passbooks1
from bankapp.forms import PassbookForm

# Create your views here.                                                                     

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				#login(request)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logout(request):
	#logout(request)
	return redirect('/')

def index(request):#//////////////////////////////////////////////////////////////////////////////
	return render (request,"index.html")

def home(request):
	return render(request,"home.html")

def show(request):
	sd = S_Details.objects.all()
	return render(request,"show.html",{'sd':sd})

def create(request):
	context = {}
	#add dictionary during initialization
	form = SdForm(request.POST or None)
	if form.is_valid():#it will check data is there or not
		form.save()
		return redirect('/show')

	context['form']= form
	return render(request,"create.html",context)


def update(request,id):
	context = {}
	obj = get_object_or_404(S_Details, id = id)
	form = SdForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/show')
	context["form"] = form
	return render(request,"update.html",context)

def delete(request,id):
	context = {}
	obj = get_object_or_404(S_Details, id = id)

	if request.method=='POST':
		obj.delete()
		return redirect('/show')
	return render(request,"delete.html",context)

#///////////////////////////////////////////////////////////////////////////////////////////////////

def attendance(request):
	at = Attendance.objects.all()
	return render(request,"attendance.html",{'at':at})

def atcreate(request):
	context = {}
	#add dictionary during initialization
	form = AttendanceForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/attendance')

	context['form']= form
	return render(request,"atcreate.html",context)

def atupdate(request,staff_id):
	context = {}
	obj = get_object_or_404(Attendance, staff_id = staff_id)
	form = AttendanceForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/attendance')
	context["form"] = form
	return render(request,"atupdate.html",context)

def atdelete(request,staff_id):
	context = {}
	obj = get_object_or_404(Attendance, staff_id = staff_id)

	if request.method=='POST':
		obj.delete()
		return redirect('/attendance')
	return render(request,"atdelete.html",context)

#////////////////////////////////////////////////////////////////////////////////////////////////////

def s_documents(request):
	sdoc = S_Documents.objects.all()
	return render(request,"s_documents.html",{'sdoc':sdoc})

def sdoccreate(request):
	context = {}
	form = S_DocumentsForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/s_documents')
	context["form"] = form
	return render(request,"sdoccreate.html",context)

def sdocupdate(request,emp_id):
	context = {}
	obj = get_object_or_404(S_Documents, emp_id = emp_id)
	form = S_DocumentsForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/s_documents')
	context["form"] = form
	return render(request,"sdocupdate.html",context)

def sdocdelete(request,emp_id):
	context = {}
	obj = get_object_or_404(S_Documents, emp_id = emp_id)

	if request.method=='POST':
		obj.delete()
		return redirect('/s_documents')
	return render(request,"sdocdelete.html",context)

#////////////////////////////////////////////////////////////////////////////////////

def leave(request):
	sl = Leave.objects.all()
	return render(request,"leave.html",{'sl':sl})


def leavecreate(request):
	context = {}
	form = LeaveForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/leave')
	context["form"] = form
	return render(request,"leavecreate.html",context)

def leaveupdate(request,id):
	context = {}
	obj = get_object_or_404(Leave, id = id)
	form = LeaveForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/leave')
	context["form"] = form
	return render(request,"leaveupdate.html",context)

def leavedelete(request,id):
	context = {}
	obj = get_object_or_404(Leave, id = id)

	if request.method=='POST':
		obj.delete()
		return redirect('/leave')
	return render(request,"leavedelete.html",context)

#///////////////////////////////////////////////////////////////////////////////////////////////////////

def holiday(request):
	holi = Holiday.objects.all()
	return render(request,"holiday.html",{'holi':holi})

def holidaycreate(request):
	context = {}
	form = HolidayForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/holiday')
	context["form"] = form
	return render(request,"holidaycreate.html",context)

def holidayupdate(request,id):
	context = {}
	obj = get_object_or_404(Holiday, id = id)
	form = HolidayForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/holiday')
	context["form"] = form
	return render(request,"holidayupdate.html",context)

def holidaydelete(request,id):
	context = {}
	obj = get_object_or_404(Holiday, id = id)

	if request.method=='POST':
		obj.delete()
		return redirect('/holiday')
	return render(request,"holidaydelete.html",context)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////


def service(request):
	return render(request,"service.html")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

def c_details(request):
	cd = C_Details.objects.all()
	return render(request,"c_details.html",{'cd':cd})

def c_create(request):
	context = {}
	form = C_DetailsForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/c_details')
	context["form"] = form
	return render(request,"c_create.html",context)

def c_update(request,id):
	context = {}
	obj = get_object_or_404(C_Details, id = id)
	form = C_DetailsForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/c_details')
	context["form"] = form
	return render(request,"c_update.html",context)

def c_delete(request,id):
	context = {}
	obj = get_object_or_404(C_Details, id = id)

	if request.method=='POST':
		obj.delete()
		return redirect('/c_details')
	return render(request,"c_delete.html",context)

#///////////////////////////////////////////////////////////////////////////////////////////////

def c_documents(request):
	cdoc = C_Documents.objects.all()
	return render(request,"c_documents.html",{'cdoc':cdoc})


def c_doccreate(request):
	context = {}
	form = C_DocumentsForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/c_documents')
	context["form"] = form
	return render(request,"c_doccreate.html",context)

def c_docupdate(request,cust_id):
	context = {}
	obj = get_object_or_404(C_Documents, cust_id = cust_id)
	form = C_DocumentsForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/c_documents')
	context["form"] = form
	return render(request,"c_docupdate.html",context)

def c_docdelete(request,cust_id):
	context = {}
	obj = get_object_or_404(C_Documents, cust_id = cust_id)

	if request.method=='POST':
		obj.delete()
		return redirect('/c_documents')
	return render(request,"c_docdelete.html",context)

#/////////////////////////////////////////////////////////////////////////////////////////////
def accounts(request):
	acc = Acct1.objects.all()
	return render(request,"accounts.html",{"acc":acc})

def accreate(request):
	context = {}
	form = AccForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/accounts')
	context["form"] = form
	return render(request,"accreate.html",context)

	
def acupdate(request,id):
	context={}
	obj = get_object_or_404(Acct1,id = id)
	form = AccForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect('/accounts')
	context["form"] = form
	return render(request,"acupdate.html",context)

def acdelete(request,id):
	context={}
	obj = get_object_or_404(Acct1,id=id)

	if request.method=='POST':
		obj.delete()
		return redirect('/accounts')
	return render(request,"acdelete.html",context)

#////////////////////////////////////////////////////////////////////////////////////////////////

def about(request):
	return render(request,"about.html")

#///////////////////////////////////////////////////////////////////////////////////////////////

def contact(request):
	return render(request,"contact.html")

#/////////////////////////////////////////////////////////////////////////////////////////////////

def passbook(request):#for read operation
	pb = Passbooks1.objects.all()
	return render(request,"passbook.html",{'pb':pb})

def pbcreate(request):# for create opearation
	context = {}
	#add dictionary during initialization
	form = PassbookForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/passbook')

	context['form']= form
	return render(request,"pbcreate.html",context)


def pbupdate(request,id):
	context = {}
	obj = get_object_or_404(Passbooks1, id = id)
	form = PassbookForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect('/passbook')
	context["form"] = form
	return render(request,"pbupdate.html",context)

def pbdelete(request,id):
	context = {}
	obj = get_object_or_404(Passbooks1, id = id)

	if request.method=='POST':
		obj.delete()
		return redirect('/passbook')
	return render(request,"pbdelete.html",context)

#//////////////////////////////////////////////////////////////////////////
def withdraw(request):
	if request.method=='POST':
		id=request.POST.get('account_id')
		amount=request.POST.get('withdraw')
		obj=get_object_or_404(Acct1,id=id)
		bal=obj.balance
		tot=int(bal)-int(amount)
		obj.balance=tot
		obj.save()
		return redirect('/accounts')
	
	return render(request,"withdraw.html")

#////////////////////////////////////////////////////////////////////////////
def deposit(request):
	if request.method=='POST':
		id=request.POST.get('account_id')
		amount=request.POST.get('deposit')
		obj=get_object_or_404(Acct1,id=id)
		bal=obj.balance
		tot=int(bal)+int(amount)
		obj.balance=tot
		obj.save()
		return redirect('/accounts')
	
	return render(request,"deposit.html")
