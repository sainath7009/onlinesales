from django.db import models

class MerchentModel(models.Model):
    m_idno=models.IntegerField(primary_key=True)
    m_name=models.CharField(max_length=30)
    m_contact=models.IntegerField(unique=True)
    m_email=models.EmailField(unique=True)
    m_password=models.CharField(max_length=8)