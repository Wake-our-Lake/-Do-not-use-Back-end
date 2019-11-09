from django.db import models
# from django.contrip.auth.models import User
# Create your models here.
from django.contrib.auth.models import User

ACTIVE_CHOICES = ((0, 'Male'), (2, 'Female'),)

ACTIVE = ((0,'Inactive'), (2, 'Active'),)
class Base(models.Model):
    
    """ Basic Fields """

    active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True



class Tasks(Base):
    task_description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.task_description





class Lakes(Base):

    lake_name = models.TextField(blank=True,null=True)
    lake_description = models.TextField(blank=True,null=True)
    latitude = models.CharField(blank=True,null=True,max_length=100)
    longitude = models.CharField(blank=True,null=True,max_length=100)
    gmaps_url = models.TextField(blank=True,null=True)
    whats_app_weblink = models.TextField(blank=True,null=True)
    state = models.CharField(blank=True,null=True,max_length=100)
    district = models.CharField(blank=True,null=True,max_length=100)
    current_water_level = models.IntegerField(blank=True,null=True)
    capacity_msqft = models.IntegerField(blank=True,null=True)
    catchment_area_sqkm = models.IntegerField(blank=True,null=True)
    full_tank_area = models.IntegerField(blank=True,null=True)
    area_of_water = models.IntegerField(blank=True,null=True)
    length_of_lake_bund = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name










class Users(Base):
    user = models.ForeignKey(User, blank=True, null=True)
    user_type = models.TextField(blank=True,null=True)
    full_name = models.TextField(blank=True,null=True)
    email = models.CharField(blank=True,null=True,unique=True,max_length=100)
    gender = models.PositiveIntegerField(
        choices=ACTIVE_CHOICES, blank=True, null=True)
    phone_no = models.TextField(blank=True,null=True)
    active_flag = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.full_name











class WOLActivites(Base):

    # lake = models.ForeignKey(Lakes, blank=True, null=True)
    user = models.ForeignKey(Users, blank=True, null=True)
    task = models.ForeignKey(Tasks, blank=True, null=True)
    current_water_level = models.IntegerField(blank=True,null=True,default=0)
    active_flag = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.current_water_level








