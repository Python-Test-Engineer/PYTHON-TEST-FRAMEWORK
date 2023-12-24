import datetime

from django.shortcuts import HttpResponse, render

# Create your views here.


# def bank_homepage(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


def bank_homepage(request):
    """homepage view"""

    return render(request, "bank/index.html")
