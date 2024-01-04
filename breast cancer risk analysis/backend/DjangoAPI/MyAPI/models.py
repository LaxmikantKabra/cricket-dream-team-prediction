from django.db import models

# Create your models here.
# class riskresult(models.Model):
#     GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female')
#     )
#     MARRIED_CHOICES = (
#         ('Married', 'Yes'),
#         ('Unmarried', 'No')
#     )
#     BREAST_PAIN = (
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )
#     COMORBODITIES = (
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )
#     FAMILY_HISTORY = (
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )
#     CONTRACEPTION_HISTORY = (
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )
#     MENOPAUSE_ENCOUNTERED = (
#         ('Yes', 'Yes'),
#         ('No', 'No')
#     )



#     firstName = models.CharField(max_length=15)
#     lastName = models.CharField(max_length=15)
#     age = models.IntegerField()
#     ageFirstChild = models.IntegerField(default=0)
#     menstrualAge = models.IntegerField()
#     menopausalAge = models.IntegerField(default=0)
#     numberOfChild = models.IntegerField(default=0)
#     breastPain = models.CharField(max_length=3, choices=BREAST_PAIN)
#     comorbodities = models.CharField(max_length=3, choices=COMORBODITIES)
#     familyHistory = models.CharField(max_length=3, choices=FAMILY_HISTORY)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#     contraceptionHistory = models.CharField(max_length=3, choices=CONTRACEPTION_HISTORY)
#     maritalStatus = models.CharField(max_length=9, choices=MARRIED_CHOICES)
#     menopauseEncountered = models.CharField(max_length=3, choices=MENOPAUSE_ENCOUNTERED)

#     def __str__(self):
#         return self.firstName
