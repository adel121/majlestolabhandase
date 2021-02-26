from django.db import models

# Create your models here.







Discipline_Choices = (('common trunk','COMMON TRUNK'),('ge','GE'),('power','POWER'), ('telecom','TELECOM'), ('gc','GC'),('gm', 'GM'), ('gp', 'GP') )
Language_Choices = (('english','ENGLISH'), ('french','FRENCH'),('both','BOTH'))
class Class(models.Model):
	def getDiscipline(self):
		if self.Discipline == 'ge':
			return "Electrical Engineering"
		elif self.Discipline == 'gc':
			return "Civil Engineering"
		elif self.Discipline == 'gp':
			return 'Petrochemical Engineering'
		elif self.Discipline == 'gm':
			return 'Mechanical Engineering'
		elif self.Discipline == 'telecom':
			return 'Telecom'
		elif self.Discipline == 'power':
			return  "Power"
		else:
			return "Common Trunk"

	def __str__(self):
		if self.Language == "both":
			return self.getDiscipline() + " Sem-" + str(self.Semester)
		else:
			return self.getDiscipline() + " Sem-" + str(self.Semester) + " - " + self.Language
	Semester = models.IntegerField(default=1)
	Discipline = models.CharField(max_length=100, choices=Discipline_Choices,default="common trunk")
	Language = models.CharField(max_length=100, choices=Language_Choices,default="english")


class Course(models.Model):
	def __str__(self):
		return self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

class Video(models.Model):
	def __str__(self):
		return str(self.Course) + " " + str(self.Lecture_Number)
	Youtube = models.CharField(max_length=300, default="https://youtube.com")
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Date = models.DateTimeField('Date In', blank=False, null=True)
	Lecture_Number = models.FloatField(null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")

class Document(models.Model):
	def __str__(self):
		return str(self.Course) + "/" +self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Format = models.CharField(max_length=100,)
	Notes = models.CharField(max_length=100,)
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")
	