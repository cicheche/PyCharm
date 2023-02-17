from django.contrib import admin
from django.db.models import F

from .models import *


# Register your models here.
class dataAdmin(admin.ModelAdmin):
    list_display = ("singer", "name", "id",
                    "s_time")

    # class Media:
    #     js = (
    #         '/static/admin/js/kindeditor/kindeditor-all-min.js',
    #         '/static/admin/js/kindeditor/config.js',
    #         '/static/admin/js/jquery-3.6.0.min.js',
    #         '/static/admin/js/site.js',
    #     )

    list_display_links = ["name"]
    list_filter = ["name", "singer"]
    # search_fields = ["Title", "Category"]
    # fields = [("Title", "Author"), "Abstract"]
    # fieldsets = (
    #     ("基本信息", {
    #         'fields': ['name', ('singer', 's_time')]
    #     }),
    #     ("交互信息", {
    #         'classes': ('collapse', "wide"),
    #         'fields': [("name", "s_time")],
    #     })
    # )
    readonly_fields = ("singer", "s_time", "name")

    # raw_id_fields = ["user"]

    def opt(self, obj):
        return obj.user.username

    def has_delete_permission(self, request, obj=None):
        return False

    opt.short_description = "操作员"

    list_per_page = 5


class commentAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "comment", "c_time")
    # search_fields = ["Title", "Types"]
    ordering = ["id"]
    raw_id_fields = ["id"]

    def opt(self, obj):
        return obj.user.username

    def has_delete_permission(self, request, obj=None):
        return False

    #
    def has_change_permission(self, request, obj=None):
        return False

    # def save_model(self, request, obj, form, change):
    #     if change == False:
    #         obj.user = request.user
    #         Article.object.filter(pk=obj.Article.id).update(Like_num=F("Like_num") + 1)
    #         Article.object.filter(pk=obj.Article.id).update(Against_num=F("Against_num") + 1)
    #         Article.object.filter(pk=obj.Article.id).update(Read_num=F("Read_num") + 1)
    #     super(LogInfoAdmin, self).save_model(request, obj, form, change)

    opt.short_description = "操作员"

    list_per_page = 5


# class CommentInfoAdmin(admin.ModelAdmin):
#     list_display = ("Title", "Content", "user", "C_time")
#     ordering = ["C_time"]
#     search_fields = ["Title", "Content"]
#     raw_id_fields = ["article"]
#     readonly_fields = ["user"]
#     fields = ["Title", "Content"]
#
#     def save_model(self, request, obj, form, change):
#         if change == False:
#             obj.user = request.user
#             Article.object.filter(pk=obj.Article.id).update(Reply_num=F("Reply_num") + 1)
#         super(CommentInfoAdmin, self).save_model(request, obj, form, change)
#
#     def opt(self, obj):
#         return obj.user.username
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     opt.short_description = "操作员"
#
#     list_per_page = 5


#
admin.site.register(Musicdata, dataAdmin)
admin.site.register(Comment, commentAdmin)
# admin.site.register(CommentInfo, CommentInfoAdmin)
admin.site.site_header = "酷我音乐系统"
admin.site.site_title = "酷我音乐系统"
