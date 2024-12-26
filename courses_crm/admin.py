from django.contrib import admin

from .models import Course ,TitleHeading ,TitleHeadingDetail
# Register your models here.
admin.site.register(Course)
admin.site.register(TitleHeading)
admin.site.register(TitleHeadingDetail)