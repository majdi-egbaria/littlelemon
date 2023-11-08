from django.db import models


class Booking(models.Model):
    Name = models.CharField(max_length=255, null=False)
    No_of_guests = models.SmallIntegerField(default=0)
    BookingDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name


class Menu(models.Model):
   Title = models.CharField(max_length=255, null=False)
   Price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
   Inventory = models.SmallIntegerField()

   def __str__(self):
      return self.Title
