from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Images(models.Model):
    barcode = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    fish = models.CharField(max_length=255)  # Full name
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    post_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.barcode
