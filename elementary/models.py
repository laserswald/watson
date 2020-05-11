from django.db import models
from django.contrib.auth.models import User

class FirstAndLastNameAsString:
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name;

class Guardian(FirstAndLastNameAsString, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dependents = models.ManyToManyField("Student")

class Teacher(FirstAndLastNameAsString, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # events = Event[]
    # subjects = Subject[]
    # wishes = Wish[]
    # messages = Message[]
    def get_full_name(self):
        return self.user.first_name+" "+self.user.last_name;

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # subjects = Attendance[]
    # grades = Grade[]

    def __str__(self):
        return self.first_name+" "+self.last_name;

    def assignments(self):
        return Assignment.objects.filter(subject__students__student = self.id)


## Grading
class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="subjects")
    name = models.CharField(max_length=50)
    # students = Attendance[]

    def __str__(self):
        return self.teacher.user.last_name + ": " + self.name

class Event(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="events")
    date = models.DateField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, related_name="assignments")
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, related_name="subjects")
    subject = models.ForeignKey(Subject, related_name="students")

    def __str__(self):
        return self.subject.__str__() + ": " + self.student.__str__()

class Grade(models.Model):
    student = models.ForeignKey(Student, related_name="grades")
    assignment = models.ForeignKey(Assignment, related_name="submissions")
    grade = models.IntegerField()

## Wish lists

class Wish(models.Model):
    wisher = models.ForeignKey(Teacher, related_name="wishes")
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class WishResponse(models.Model):
    responder = models.ForeignKey(Guardian, related_name="wish_responses")
    wish = models.ForeignKey(Wish, related_name="responses")
    body = models.TextField()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_msgs")
    recipients = models.ManyToManyField(User, related_name="recieved_msgs")
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.subject

    def get_sender_name(self):
        return self.sender.first_name+" "+self.sender.last_name;

