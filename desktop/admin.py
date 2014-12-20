# Registers the models with the admin interface

from django.contrib import admin
from desktop.models import User, Result, Glossary, Question, Answer, Lab

#admin.site.register(User)
admin.site.register(Result)
admin.site.register(Glossary)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Lab)
