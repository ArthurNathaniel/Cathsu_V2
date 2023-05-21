from django.db import models

# Create your models here.


class Document(models.Model):
    document_name = models.CharField(max_length=255)
    document_image = models.ImageField(upload_to="document_image")

    def __str__(self):
        return self.document_name

    
    # def __str__(self):
    #     return self.document_name
    # def __str__(self):
    #     return self.document_name
    
    # def __str__(self):
    #     return self .document_name
