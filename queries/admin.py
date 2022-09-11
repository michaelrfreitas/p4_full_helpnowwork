from django.contrib import admin
from .models import QuestionModel, AnswerModel

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'slug', 'user', 'category', 'created_on')
    search_fields = ['question', 'category', 'user']
    list_filter = ('category', 'created_on')
    prepopulated_fields = {'slug': ('question',)}


admin.site.register(AnswerModel)
