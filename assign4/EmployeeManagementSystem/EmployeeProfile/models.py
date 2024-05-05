from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class JobDescription(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    cnic = models.IntegerField()
    dateofjoining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    jobdescription = models.ForeignKey(JobDescription, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
