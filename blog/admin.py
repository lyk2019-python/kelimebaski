from django.contrib import admin

# Register your models here.
from blog.models import Gonderi, Yorum


@admin.register(Gonderi)
class GonderiAdmin(admin.ModelAdmin):
    list_display = ["baslik", "icerik_kisa", "olusturulma"]
    fields = ["baslik", "icerik", "olusturulma"]
    readonly_fields = ["icerik_kisa", "olusturulma"]
    list_filter = ["olusturulma"]

    def icerik_kisa(self, obj):
        return obj.icerik_kisa

    icerik_kisa.allow_tags = True
    icerik_kisa.short_description = "İçerik"


@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ["gonderi_baslik", "icerik_kisa", "olusturulma"]
    fields = ["gonderi", "icerik", "olusturulma"]
    readonly_fields = ["gonderi_baslik", "icerik_kisa", "olusturulma"]
    list_filter = ["olusturulma"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("gonderi")

    def gonderi_baslik(self, obj):
        return obj.gonderi.baslik

    gonderi_baslik.allow_tags = True
    gonderi_baslik.short_description = "Gönderi"

    def icerik_kisa(self, obj):
        return obj.icerik_kisa

    icerik_kisa.allow_tags = True
    icerik_kisa.short_description = "İçerik"
