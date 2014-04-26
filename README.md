# This is SexySignOn!!

SexySignOn is a sexy Single Sign On system based on nginx's LUA module and a 
django app called *multilogger* as the single sign on page.

To make it work, use the provisioning script.

This system consists of the following.

Multilogger has the following dependencies (met if provisioning with the
provided ansible script):

- python3.3 (add ppa:fkrull/deadsnakes)
- redis-server
- nginx-openresty (add ppa:miurahr/openresty)
- libpq-dev

Also install django-formulator as follows:

    pip install git+https://github.com/Cahersan/django-formulator.git

A postgres database is set during provision:

  * __username:__ username
  * __database name:__ multilogger
  * __password:__ password
