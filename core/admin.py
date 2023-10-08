from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import Video, Tag, Source

admin.site.register(Tag)
admin.site.register(Source)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'file',
        'tags_list',
        'review',
    ]

    # list_filter = ['']
    fields = [
        'file',
        'source',
        'tags',
        'review',
        'foo',
    ]

    # inlines = []
    # raw_id_fields = ['']
    readonly_fields = ['foo']
    # search_fields = ['']
    # ordering = ['']

    @admin.display
    def tags_list(self, obj: Video):
        tag_title_list = list(obj.tags.values_list('title', flat=True))
        return ', '.join(tag_title_list)

    @admin.display
    def foo(self, obj: Video):
        html = f'''
<video width="320" height="240" controls>
  <source src="{obj.file.url}" type="video/mp4">
  Your browser does not support the video tag.
</video>
{obj.file.url}
'''
        return mark_safe(html)
