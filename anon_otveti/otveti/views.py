from django.shortcuts import render, redirect
from .models import Answers
from .forms import Answersform
import library_cypher as cpss
import time
import sqlite3

allowed_ips = ["127.0.0.1"]


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def main(request):
    answs = Answers.objects.order_by("id").reverse()

    return render(request, "main.html", {"title": 'Ответы | Главная страница',
                                         'answs': answs,
                                         "ip_address": get_client_ip(request),
                                         "allowed_ips": allowed_ips})


def submits(request):
    answs = Answers.objects.order_by("id")
    if request.method == "POST":
        w = sqlite3.connect("db.sqlite3")
        p = w.cursor()
        p.execute(f"UPDATE otveti_answers set is_checked = 1 where id = {list(request.POST)[1]}")
        w.commit()
        w.close()

    return render(request, "submits.html", {"title": 'Подтверждение ответов',
                                            "anwers": answs,
                                            "ip_address": get_client_ip(request),
                                            "allowed_ips": allowed_ips})


def create(request):
    if request.method == "POST":
        forms = request.POST.copy()
        forms["date"], forms[
            "is_checked"] = f"{time.strftime('%d.%m.%Y г. %H:%M:%S', time.localtime(time.time()))}", False
        forms["krypto"], forms["author"] = cpss.cypher.incphkrypto(f"{get_client_ip(request)}", False, True)

        form = Answersform(forms)
        if form.is_valid():
            form.save()
            return redirect("create")

    form = Answersform()
    context = {
        "title": "Страница создания ответа",
        "form": form,
        "ip_address": get_client_ip(request),
        "date_now": f"{time.strftime('%d.%m.%Y г. %H:%M:%S', time.localtime(time.time()))}",
        "allowed_ips": allowed_ips
    }
    return render(request, "create.html", context)
