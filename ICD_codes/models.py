from django.db import models

class MainCode(models.Model):
    ICD_main_code = models.CharField("ICD Main Code", max_length=20, primary_key=True)
    description = models.TextField("Description")

    def __str__(self):
        return self.ICD_main_code

class SubCode(models.Model):
    ICD_main_code = models.ForeignKey(MainCode, on_delete=models.CASCADE, verbose_name="ICD Main Code")
    ICD_sub_code = models.CharField("ICD Sub Code", max_length=20, primary_key=True)
    description = models.TextField("Description")

    def __str__(self):
        return self.ICD_sub_code
