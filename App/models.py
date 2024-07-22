from django.db import models

class app(models.Model):
    PHONE_INTERVIEW_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    STATUS_CHOICES = [
        ('Rejected', 'Rejected'),
        ('Satisfactory', 'Satisfactory'),
        ('On Hold', 'On Hold'),
    ]

    INTERVIEW_STATUS_CHOICES = [
        ('Cleared', 'Cleared'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]

    FINAL_INTERVIEW_STATUS_CHOICES = [
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]

    Number = models.IntegerField(default = 1)
    JobRole = models.CharField(max_length=50)
    JobLoc = models.CharField(max_length=50, null=True, blank=True)
    Source = models.CharField(max_length=50, null=True, blank=True)
    JobTy = models.CharField(max_length=50, null=True, blank=True)
    Contact = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    phone_interview = models.CharField(max_length=3, choices=PHONE_INTERVIEW_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    first_interview = models.CharField(max_length=20, null=True, blank=True)
    first_interview_status = models.CharField(max_length=50, choices=INTERVIEW_STATUS_CHOICES, null=True, blank=True)
    second_interview = models.CharField(max_length=20, null=True, blank=True)
    second_interview_status = models.CharField(max_length=50, choices=INTERVIEW_STATUS_CHOICES, null=True, blank=True)
    final_interview = models.CharField(max_length=20, null=True, blank=True)
    final_interview_status = models.CharField(max_length=50, choices=FINAL_INTERVIEW_STATUS_CHOICES, null=True, blank=True)
    date_of_joining = models.CharField(max_length=20, null=True, blank=True)
    ctc = models.CharField(max_length=20, null=True, blank=True, default='0')

   

   
