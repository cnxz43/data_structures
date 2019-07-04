# -*- coding:utf-8 -*-
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://zabbixserver.example.com")

# Enable HTTP auth
zapi.session.auth = ("http user", "http password")

# Disable SSL certificate verification
zapi.session.verify = False

# Specify a timeout (in seconds)
zapi.timeout = 5.1

# Login (in case of HTTP Auth, only the username is needed, the password, if passed, will be ignored)
zapi.login("http user", "http password")