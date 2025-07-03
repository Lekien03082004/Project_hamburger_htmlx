from django.db import models


# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name


class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(
        ItemList, related_name="Category_item", on_delete=models.CASCADE
    )
    Image = models.ImageField(upload_to="items")

    def __str__(self):
        return self.Item_name


class AboutUs(models.Model):
    Description = models.TextField(blank=False)


class FeedBack(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.User_name


class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()
    Total_persons = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
