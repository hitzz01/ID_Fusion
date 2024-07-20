from django.db import models

class ExtractedData(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    pan_number = models.CharField(max_length=10, null=True, blank=True)
    aadhaar_number = models.CharField(max_length=12, null=True, blank=True)
    age = models.IntegerField()
    qr_code_image = models.BinaryField()
    visitor_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    date_of_visiting = models.DateField()
    duration_of_visiting = models.CharField(max_length=50)
    document_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
