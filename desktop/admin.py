# Registers the models with the admin interface

from django.contrib import admin
from desktop.models import User, Result, Glossary

#admin.site.register(User)
admin.site.register(Result)
admin.site.register(Glossary)