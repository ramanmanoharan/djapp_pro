from django.db import models

# Create your models here.
class Metadatas(models.Model):
	# location = models.TextField()
	title = models.TextField()
	keyword = models.TextField()
	description = models.TextField()
	logo = models.ImageField(upload_to='images/', null=True)



	def __str__(self):
		return str(self.id)
		


	class Meta:
		verbose_name= 'Metadatas'
		verbose_name_plural= 'Metadata'


class ContactDetails(models.Model):
	# location = models.TextField()
	title = models.CharField(max_length= 50)
	description = models.TextField()
	button = models.CharField(max_length= 50)
	image = models.ImageField(upload_to='images/', null=True)



	def __str__(self):
		return str(self.id)



	class Meta:
		verbose_name= 'ContactDetails'
		verbose_name_plural= 'ContactDetail'


class ContactMessage(models.Model):
	name = models.CharField(max_length= 50)
	email = models.CharField(max_length= 50)
	phone = models.CharField(max_length= 50)
	message = models.TextField()


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ContactMessages'
		verbose_name_plural ='ContactMessage'


class Footer(models.Model):
	background = models.ImageField(upload_to='images/', null=True)
	title = models.CharField(max_length=50)
	shorttitle = models.CharField(max_length=50)
	copyright = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Footers'
		verbose_name_plural ='Footer'

#work model

class Work(models.Model):
	title = models.CharField(max_length=50)
	shorttitle = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/', null=True)
	postedby = models.CharField(max_length=50)


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Works'
		verbose_name_plural ='Work'


class Whoweare(models.Model):
	title = models.CharField(max_length= 50)
	shorttitle = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/', null=True)
	message = models.TextField()


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Whoweares'
		verbose_name_plural ='Whoweare'


class Blog(models.Model):
	title = models.CharField(max_length=50)
	shorttitle = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/', null=True)
	postedby = models.CharField(max_length=50)
	postdate = models.CharField(max_length=50)


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Blogs'
		verbose_name_plural ='Blog'

class About(models.Model):
	title = models.CharField(max_length=50)
	shorttitle = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/', null=True)
	shortimage = models.ImageField(upload_to='images/', null=True)



	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Abouts'
		verbose_name_plural ='About'



class Profile(models.Model):
	Name = models.CharField(max_length=50)
	Fathername = models.CharField(max_length=50)
	Address = models.TextField()
	#Skills = models.TextField()
	Education = models.TextField()
	#Designation = models.CharField(max_length=100)
	Experience = models.TextField()
	DOB = models.DateField()
	#Mail = models.CharField(max_length=100)
	#Phone = models.CharField(max_length=100)
	Linkdin = models.CharField(max_length=100)
	Facebook = models.CharField(max_length=100)
	Github = models.CharField(max_length=100)
	Portfolio = models.TextField()
	Resume = models.ImageField(upload_to='images/', null=True)
	image = models.ImageField(upload_to='images/', null=True)
	



	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Profiles'
		verbose_name_plural ='Profile'

class Resume(models.Model):
	Name = models.CharField(max_length=50)
	Fathername = models.CharField(max_length=50)
	Address = models.TextField()
	Skills = models.TextField()
	Education = models.TextField()
	Designation = models.CharField(max_length=100)
	Experience = models.TextField()
	DOB = models.DateField()
	Mail = models.CharField(max_length=100)
	Phone = models.CharField(max_length=100)
	Linkdin = models.CharField(max_length=100)
	Facebook = models.CharField(max_length=100)
	Github = models.CharField(max_length=100)
	Portfolio = models.TextField()
	Resume = models.ImageField(upload_to='images/', null=True)
	image = models.ImageField(upload_to='images/', null=True)
	



	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Resumes'
		verbose_name_plural ='Resume'

