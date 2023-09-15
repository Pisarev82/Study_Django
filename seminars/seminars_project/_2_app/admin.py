from django.contrib import admin
from .models import Trow, Author, Article, Comment




@admin.action(description='Сбросить сортировку')
def reset(modeladmin, request, queryset):
    queryset.update(quantity=0)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'biography', 'birthday']
    list_filter = ['name', 'surname']
    search_fields = ['name']
    actions = ['reset']


class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['title', 'content', 'author', ]
    ordering = ['publication_date']
    search_fields = ['author']
    actions = ['reset']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Полный текст статьи и автор',
                'fields': ['content', 'author'],
            }
        )
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AutorAdmin)
admin.site.register(Article, ArticleAdmin)

