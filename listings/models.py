from django.db import models
from datetime import datetime
from agents.models import Agent


class Listing(models.Model):
    class ListingCategory(models.TextChoices):
        HOUSE = "House"
        APARTMENT = "Apartment"
        OFFICE = "Office"
        PG = "PG"
        HOSTEL = "Hostel"
        OTHER = "Other"

    class ListingType(models.TextChoices):
        RESIDENTIAL = "Residential"
        LAND = "Land"
        COMMERCIAL = "Commercial"

    class ListingCurrentStatus(models.TextChoices):
        UNDER_CONSTRUCTION = "Under-Construction"
        COMPLETED = "Completed"

    class ListingBuyStatus(models.TextChoices):
        SALE = "Sale"
        RENT = "Rent"

    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    building_area = models.IntegerField()
    listing_category = models.CharField(max_length=15, choices=ListingCategory.choices, default=ListingCategory.HOUSE)
    listing_type = models.CharField(max_length=15, choices=ListingType.choices, default=ListingType.RESIDENTIAL)
    listing_current_status = models.CharField(
        max_length=25, choices=ListingCurrentStatus.choices, default=ListingCurrentStatus.UNDER_CONSTRUCTION
    )
    listing_buy_status = models.CharField(
        max_length=15, choices=ListingBuyStatus.choices, default=ListingBuyStatus.SALE
    )
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
