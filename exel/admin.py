from django.contrib import admin
from .models import *

#admin.site.unregister(User)
admin.site.register(Dmp)
admin.site.register(Report)
admin.site.register(Brief_pattern)
admin.site.register(Report_common)
admin.site.register(Media_plan)
#admin.site.register(User)
