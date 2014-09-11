test_reversion
==============

a test of django-reversion 1.8.4 (where reversion log's user get lost)

<b>first:</b><br>
  it's a test of django-reversion, which demonstate that its ability for rollback/recorery of data for admin site.

<b>on the other hand:</b><br>

  it's a demo which proves that the user/comment of the reversion log will get lost when data been updated from outside the admin site.
   
  for this purpose, just try the url: http://127.0.0.1/update/1  
  there is no need for anything like manage.py sync db because the database is already there.
  admin account and password: admin/1
  
  my enviroment: windows 7 professional 64bit / django 1.6.5 / python 2.7.5 /django-reversion 1.8.4
