from django import forms
from bankapp.models import S_Details
from bankapp.models import Attendance
from bankapp.models import S_Documents
from bankapp.models import Leave
from bankapp.models import Holiday
from bankapp.models import C_Details
from bankapp.models import C_Documents
from bankapp.models import Acct1
from bankapp.models import Passbooks1

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class SdForm(forms.ModelForm):
	class Meta:
		model = S_Details
		fields = "__all__"

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = "__all__"

class S_DocumentsForm(forms.ModelForm):
	class Meta:
		model = S_Documents
		fields = "__all__"

class LeaveForm(forms.ModelForm):
	class Meta:
		model = Leave
		fields = "__all__"

class HolidayForm(forms.ModelForm):
	class Meta:
		model = Holiday
		fields = "__all__"

class C_DetailsForm(forms.ModelForm):
	class Meta:
		model = C_Details
		fields = "__all__" 

class C_DocumentsForm(forms.ModelForm):
	class Meta:
		model = C_Documents
		fields = "__all__" 

class AccForm(forms.ModelForm):
	class Meta:
		model = Acct1
		fields = "__all__"

class PassbookForm(forms.ModelForm):
	class Meta:
		model = Passbooks1
		fields = "__all__"
