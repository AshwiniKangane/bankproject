from django.db import models

# Create your models here.

#/////////////////////////////////////STAFF///////////////////////////////////////////

class S_Details(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	mobile_no=models.CharField(max_length=12)
	Gender=models.CharField(max_length=10)
	marital_status=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)

	def __str__(self):
		ret = self.name+','+self.address+','+self.mobile_no+','+self.Gender+','+self.marital_status+','+self.email
		return ret



class Attendance(models.Model):
	staff = models.OneToOneField(S_Details,on_delete=models.CASCADE,primary_key=True)
	date=models.DateField(max_length=50)
	day=models.CharField(max_length=30)
	intime=models.TimeField(max_length=30)
	outtime=models.TimeField(max_length=30)
	hours=models.CharField(max_length=30)
	status=models.CharField(max_length=50)

	
class S_Documents(models.Model):
    emp = models.OneToOneField(S_Details,on_delete=models.CASCADE,primary_key=True)
    aadhar=models.CharField(max_length=50)
    pan=models.CharField(max_length=30)
    voting_card=models.CharField(max_length=30)
    driving_license=models.CharField(max_length=30)


class Leave(models.Model):
	sta =models.ForeignKey(S_Details,on_delete=models.CASCADE)
	leave=models.CharField(max_length=30)
	reason=models.CharField(max_length=70)
	start_date=models.DateField(max_length=30)
	end_date=models.DateField(max_length=30)
	status=models.CharField(max_length=30)


class Holiday(models.Model):
	date=models.DateField(max_length=30)
	day=models.CharField(max_length=30)
	remarks=models.CharField(max_length=30)
	pattern=models.CharField(max_length=30)




#/////////////////////////////////////CUSTOMER/////////////////////////////////////////


class C_Details(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	mobile_no=models.CharField(max_length=12)
	Gender=models.CharField(max_length=10)
	marital_status=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)

	def __str__(self):
		ret = self.name+','+self.address+','+self.mobile_no+','+self.Gender+','+self.marital_status+','+self.email
		return ret


class C_Documents(models.Model):#delete action
    cust = models.OneToOneField(C_Details,on_delete=models.CASCADE,primary_key=True)
    aadhar=models.CharField(max_length=50)
    pan=models.CharField(max_length=30)
    voting_card=models.CharField(max_length=30)
    driving_license=models.CharField(max_length=30)


class Acct1(models.Model):
    c_a=models.ForeignKey(C_Details,on_delete=models.CASCADE)
    account_type=models.CharField(max_length=50)
    balance=models.IntegerField()
    investments=models.IntegerField()

class Passbooks1(models.Model):
    c_a_s=models.ForeignKey(C_Details,on_delete=models.CASCADE)
    date=models.DateField(max_length=30)
    details=models.CharField(max_length=100)
    cheque_no=models.CharField(max_length=50)
    debit=models.IntegerField()
    credit=models.IntegerField()
    balance=models.IntegerField()


#///////////////////////////////////////////////////////////////
