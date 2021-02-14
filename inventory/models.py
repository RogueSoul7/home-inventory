from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.name


class State(models.Model):
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=255, blank=True, null=True)
  country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name


class Address(models.Model):
  street_1 = models.CharField(max_length=255)
  street_2 = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
  zipcode = models.CharField(max_length=5)
  longitude = models.DecimalField(
      decimal_places=6, max_digits=8, blank=True, null=True)
  latitude = models.DecimalField(
      decimal_places=6, max_digits=8, blank=True, null=True)

  def __str__(self):
    return self.street_1


class Company(models.Model):
  name = models.CharField(max_length=255)
  address = models.ForeignKey(
      Address, on_delete=models.SET_NULL, blank=True, null=True)
  logo_url = models.URLField(max_length=200, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  type = models.CharField(max_length=255, blank=True, null=True)
  website = models.URLField(max_length=200, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

  def __str__(self):
    return self.name


class ItemType(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class ItemShape(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class ItemSize(models.Model):
  name = models.CharField(max_length=255)
  length = models.DecimalField(decimal_places=2, max_digits=7)
  width = models.DecimalField(decimal_places=2, max_digits=7)
  height = models.DecimalField(
      decimal_places=2, max_digits=7, blank=True, null=True)
  volume = models.DecimalField(
      decimal_places=2, max_digits=7, blank=True, null=True)
  shape = models.ForeignKey(
      ItemShape, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.name


class Item(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, blank=False, null=False)
  description = models.TextField(blank=True, null=True)
  sku = models.CharField(max_length=255, blank=True, null=True)
  sparks_joy = models.BooleanField(default=False)
  item_type = models.ForeignKey(
      ItemType, on_delete=models.SET_NULL, blank=True, null=True)
  size = models.ForeignKey(
      ItemSize, on_delete=models.SET_NULL, blank=True, null=True)
  company = models.ForeignKey(
      Company, on_delete=models.SET_NULL, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class InventoryLocation(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  image_url = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.name


class ItemInfo(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  purchase_date = models.DateField()
  expiration_date = models.DateField(blank=True, null=True)
  last_used = models.DateField()
  purchase_price = models.DecimalField(
      decimal_places=2, max_digits=7, blank=True, null=True)
  mrsp = models.DecimalField(
      decimal_places=2, max_digits=7, blank=True, null=True)
  inventory_location = models.ForeignKey(
      InventoryLocation, on_delete=models.SET_NULL, blank=True, null=True)
  company = models.ForeignKey(
      Company, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.item.name
