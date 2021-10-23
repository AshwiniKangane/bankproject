from django.contrib import admin
from.models import S_Details
from.models import Attendance
from.models import S_Documents
from.models import Leave
from.models import Holiday
from.models import C_Details
from.models import C_Documents
from.models import Acct1
from.models import Passbooks1


class S_DetailsAdmin(admin.ModelAdmin):
	list_display=['name','address','mobile_no','Gender','marital_status','email']

class AttendanceAdmin(admin.ModelAdmin):
	list_display=['staff','date','day','intime','outtime','hours','status']

class S_DocumentsAdmin(admin.ModelAdmin):
	list_display=['emp','aadhar','pan','voting_card','driving_license']

class LeaveAdmin(admin.ModelAdmin):
	list_display=['sta','leave','reason','start_date','end_date','status']

class HolidayAdmin(admin.ModelAdmin):
	list_display=['date','day','remarks','pattern']

class C_DetailsAdmin(admin.ModelAdmin):
	list_display=['name','address','mobile_no','Gender','marital_status','email']

class C_DocumentsAdmin(admin.ModelAdmin):
	list_display=['cust','aadhar','pan','voting_card','driving_license']

class Acct1Admin(admin.ModelAdmin):
	list_display=['c_a','account_type','balance','investments']

class Passbooks1Admin(admin.ModelAdmin):
	list_display=['c_a_s','date','details','cheque_no','debit','credit','balance']

admin.site.register(S_Details,S_DetailsAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(S_Documents,S_DocumentsAdmin)
admin.site.register(Leave,LeaveAdmin)
admin.site.register(Holiday,HolidayAdmin)
admin.site.register(C_Details,C_DetailsAdmin)
admin.site.register(C_Documents,C_DocumentsAdmin)
admin.site.register(Acct1,Acct1Admin)
admin.site.register(Passbooks1,Passbooks1Admin)

