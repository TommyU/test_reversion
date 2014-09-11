test_reversion
==============

a test of django-reversion 1.8.4 (where reversion log's user get lost)

first:
  it's a test of django-reversion, which demonstate that its ability for rollback/recorery of data for admin site.

on the other hand:
  it's a demo which proves that the user/comment will get lost when data been updated from outside the admin site.
   
  for this purpose, just try the url: http://127.0.0.1/update/1  
  there is no need for anything like manage.py sync db because the database is already there.
  admin account and password: admin/1
