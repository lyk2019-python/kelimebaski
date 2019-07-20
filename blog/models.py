from django.db import models


# Create your models here.
class Gonderi(models.Model):
    baslik = models.CharField(max_length=32, verbose_name="Başlık")
    icerik = models.TextField(verbose_name="İçerik")
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return f"<Gonderi baslik='{self.baslik}' icerik='{self.icerik_kisa}'>"


    @property
    def icerik_kisa(self):
        if len(self.icerik) > 50:
            return self.icerik[:47] + "..."
        else:
            return self.icerik
class Yorum(models.Model):
    gonderi = models.ForeignKey(Gonderi, on_delete=models.DO_NOTHING, related_name="yorumlar")
    icerik = models.TextField(max_length=280)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    @property
    def icerik_kisa(self):
        if len(self.icerik) > 50:
            return self.icerik[:47] + "..."
        else:
            return self.icerik


    def __str__(self):
        return f"<Yorum baslik='{self.gonderi.baslik}' icerik='{self.icerik_kisa}'>"