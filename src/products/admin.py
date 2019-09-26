from django.contrib import admin

from .models import Product # In'.model' the '.' is known as a relative import. You are importing a 'model.py' from the same directory as this 'admin.py' which in this case is 'products/'. You are import the Product class you created in 'product/models.py'.

admin.site.register(Product) # You are registering your DB Model Product to Django's Admin site which is http://127.0.0.1:8000/admin. You can now add/delete/modify you Product records from there in http://127.0.0.1:8000/admin/products. Be sure in 'trydjango/settings.py' you include 'products/' in INSTALLED_APPS section.