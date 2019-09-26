from django.db import models
from django.urls import reverse
# Create your models here.
# The 'products/' app job as an app will be to store products infomation in the backend of this site.
# The code below is the DB Model (or blueprint) for the DataBase.
"""
From djangoprojects.com:

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

The basics:
    Each model is a Python class that subclasses django.db.models.Model.
    Each attribute of the model represents a database field.
    With all of this, Django gives you an automatically-generated database-access API

After you typed up your model you will want to go 'admin.py' to register your model. For this project goto 'products/admin.py'
"""
class Product(models.Model): # 'models.Model' Means from the models module import the class Models (you can also import functions from modules but that's not the case here). We are using inheritence here. Product is inheriting the class properties and methods from models.Model
    # To know the fields and the required param to use for your project please refer to: https://docs.djangoproject.com/en/2.2/ref/models/fields/
    # Make it a habit to read the documentation. Use google or StackOverflow if the documentation is to hard to read.
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000) # 'decimal_places=2' e.g. .12,.56, etc. not like .2365 or anything passed two decimal places.
    summary     = models.TextField(blank=False, null=False) 
    featured    = models.BooleanField(default=False) # null=True, default=True
    """
        If you ever remake an entire DB model from scratch you may want 
        to consider deleting the DB (not always, avoid that if you can). 
        For this project you do that by deleting 'db.sqlite3'
        then 'python manage.py makemigrations', 
        'python manage.py migrate' (doing these two commands will create
        a new 'db.sqlite3'), and create a 
        superuser again using 'python manage.py createsuperuser'.

        Remember you must makemigration and migrate anytime you mess with the model or DB. 

        Check out Try DJANGO Tutorial - 11 - Change a Model.
        Refer to: https://www.youtube.com/watch?v=8tVoq291aZ8&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=11
        
        This is changing DB model without deleting it. Check out the './migrations/' after. No comment was added there.
    """

    """
        On 'Try DJANGO Tutorial - 9 - Create Product Objects in the Python Shell'
         the model before the current one above was simplistic and not good construction of
          DataBase Normization (this was done on purpose for simplisty sake). What will be
           written is how to do the commands using above's current fields. 

         Firstly, make sure you are in the same directory as 'manage.py'.
         Then type 'python manage.py shell'. You need to 'from products.models import Product' to
          manipuate the DB from the python shell using manage.py.

         Using 'Product.objects.all()' will show you all DB QuerySet stored. Remember you can
          still check your QuerySet and manipuate it using the Web GUI on 
          http://127.0.0.1:8000/admin/products/

         To create a record type like this: "Product.objects.create(title='Some title',
          price=123.12, summary='Some summary')". Noticed 'description = models.TextField
          (blank=True, null=True)', 'summary = models.TextField(blank=False, null=False)',
           and 'featured = models.BooleanField(default=False)'?

         In the description with the field param set to 'blank=True' and 'null=True' you do not
          have to set a text value (blank=True) and can be set to nothing or not using ''
           (null=True). In summary you must have some string value init or Python will not enter
            your code into the DB and the DB will also not accept it. 

         'Featured' is a field that was added later on after the Try DJANGO Tutorial - 9 video.
          To fix the problem python and the DB had since there was no '(blank=True, null=True)'
           the default value of 'Featured was set to False. You can add the optional params
            should you wish. Like so: "Product.objects.create(title='Some title', price=123.12,
             summary='Some summary', Featured=True, description='Some description')".
    """

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"