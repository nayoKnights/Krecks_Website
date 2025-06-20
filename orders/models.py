from django.db import models
reference = models.CharField(max_length=12, unique=True, editable=False)
created_at = models.DateTimeField(auto_now_add=True)

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flavors/')

    def __str__(self):
        return self.name

class Order(models.Model):
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.flavor.name}"

