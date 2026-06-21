from django.contrib import admin
from .models import Profile, Info
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .admin_site import admin_site


admin.site.site_header = "پنل مدیریت سامانه"
admin.site.site_title = "مدیریت"
admin.site.index_title = "داشبورد مدیریت"

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    max_num = 1
    extra = 0
    verbose_name_plural = "پروفایل"

class InfoInline(admin.StackedInline):
    model = Info
    can_delete = False
    max_num = 1
    extra = 0
    verbose_name_plural = "مشخصات"

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, InfoInline)
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')


@admin.register(Profile, site=admin_site)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-registered_at',)
    list_display = ('id', 'user', 'num', 'registered_at')
    list_filter = ("id", "num","registered_at")
    search_fields = ('user__username', 'num')
    readonly_fields = ('registered_at',)


@admin.register(Info, site=admin_site)
class InfoAdmin(admin.ModelAdmin):
    list_select_related = ('user',)
    ordering = ('-id',)
    list_display = ("id", "user", "father_name", "national_num", "degree","province", "city")
    search_fields = ('user__username', 'national_num')
    list_filter = ('degree', 'sex', 'province')

    
    readonly_fields = (
        "photo_preview",
    )

    fieldsets = (
        ("اطلاعات شاخصی", {"fields": ("user", "father_name", "national_num", "sex", "birth_date", "degree", "email")}),
        ("مکانها", {"fields": ('birth_province', 'birth_city', 'province', 'city', 'location')}),
        ("تصاویر و مدارک", {"fields": ('degree_certification_file', 'photo_preview', 'photo', 'national_card', 'degree_certificate'), "classes": ('collapse')}),
    )

    def photo_preview(self, obj):
        if obj and obj.photo:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:10px;">',
                obj.photo.url
            )
        return "بدون تصویر"
    
    def degree_certification_file(self, obj):
        if obj and obj.degree_certificate:
            return format_html(
                '<a href="{}" target="_blank">مشاهده</a>',
                obj.degree_certificate.url
            )
        return "---"
    
    degree_certification_file.short_description = "فایل مدرک تحصیلی"
    photo_preview.short_description = "عکس"

admin_site.register(User, CustomUserAdmin)
