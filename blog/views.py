from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from blog.forms import YorumFormu
from blog.models import Gonderi, Yorum


def listele(request):
    return render(request, "blog/liste.html", {"blog_gonderileri": Gonderi.objects.all()})


def goruntule(request, gonderi_id):
    gonderi = get_object_or_404(Gonderi, id=gonderi_id)
    form = YorumFormu(request.POST)
    if request.method == "POST":
        last_comment_date = request.session.get("last_comment_date", datetime(1970, 1, 1, microsecond=1).isoformat())

        last_comment_date = datetime.strptime(last_comment_date, "%Y-%m-%dT%H:%M:%S.%f")
        now = datetime.now()
        if now - last_comment_date <= timedelta(seconds=30):
            form.add_error("icerik", f"En son {(now - last_comment_date).seconds} sn önce yorum atmışsınız, {30-(now - last_comment_date).seconds} beklemeniz gerekmektedir.")
        if form.is_valid():
            Yorum.objects.create(gonderi=gonderi, icerik=form.cleaned_data["icerik"])
            request.session["last_comment_date"] = datetime.now().isoformat()
    return render(request, "blog/goruntu.html",
                  {"blog_gonderisi": gonderi, "yorumlar": gonderi.yorumlar.all(), "form": form})
