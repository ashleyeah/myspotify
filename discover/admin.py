from django.contrib import admin

from .models import Question, Choice


# Register your models here.

admin.site.site_header = "MySpotify Admin"
admin.site.site_title = "MySpotify Admin Area"
admin.site.index_title = "Welcome to the MySpotify admin area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
