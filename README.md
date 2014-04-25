# This is SexySignOn!!

SexySignOn is a sexy Single Sign On system based on nginx's LUA module and a 
django app called *multilogger* as the single sign on page.

To make it work, use the provisioning script.

This system consists of the following.

Multilogger has the following dependencies (must check):
- python3.3 (add ppa:fkrull/deadsnakes)
- redis-server
- nginx-openresty (add ppa:miurahr/openresty)
- libpq-dev
