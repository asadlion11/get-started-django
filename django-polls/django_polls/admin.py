from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

class ChoinInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    
    # fieldsets is the title input form layout that is above the input
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoinInline]
    
    # how to display the Question list in admin site
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # filterig question in admin site
    # Django knows to give appropriate filter options based on the field type
    list_filter = ["pub_date"]
    #seacrhing
    search_fields = ["question_text"]
    
    #  Now’s also a good time to note that change lists give you free pagination. The default is to display 100 items per page
    
    
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
