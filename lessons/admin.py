from django.contrib import admin
from lessons.models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student_id')

    list_display_links = ('id', 'title')

    search_fields = ('title', 'student_id')

    list_filter = ('student_id',)

    list_per_page = 20