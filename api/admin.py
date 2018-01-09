from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User, Persona, Tag, Tutorial, Illustration

class TutorialTagsInline(admin.TabularInline):
    model = Tag.tutorials.through

class TutorialIllustrationsInline(admin.TabularInline):
    model = Illustration

class TutorialAdmin(admin.ModelAdmin):
    inlines = (TutorialTagsInline, TutorialIllustrationsInline,)

admin.site.register(Persona)
admin.site.register(Tag)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Illustration)
admin.site.register(User, UserAdmin)

# Register your models here.
