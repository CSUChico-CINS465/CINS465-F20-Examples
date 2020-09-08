from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, page=0):
    title = "My Title"
    content = list(range((page+1)*10))[page*10:page*10+10]
    # seen = True
    context = {
        "title":title,
        "body":content,
        "seen":True,
        "prev":page-1,
        "next":page+1
    }
    return render(request, "index.html", context=context)