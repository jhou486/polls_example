from django.contrib import admin
from polls.models import Question, Choice, User, Person


# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']})]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')

class PersonAdmin(admin.ModelAdmin) :
    list_display = ('name', 'text')


admin.site.register(Person, PersonAdmin)

admin.site.register(User, UserAdmin)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

