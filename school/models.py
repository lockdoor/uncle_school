from django.db import models

# Create your models here.

class ExamScore(models.Model):
    allsubject = (  ('math', 'คณิตศาสตร์'),
                    ('sci', 'วิทยาศาสตร์'),
                    ('art', 'ศิลป'),
                    ('eng', 'ภาษาอังกฤษ'),
                    ('physics', 'ฟิสิกส์'),
                    ('bio', 'ชีววิทยา'))
    subject = models.CharField(max_length=100, choices=allsubject, default='math')
    student_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.student_name + ' - ' + self.subject + ' - ' + str(self.score)

