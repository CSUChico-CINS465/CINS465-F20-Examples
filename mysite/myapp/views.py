from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save(request)
            suggestion_form = forms.SuggestionForm()
    else:
        suggestion_form = forms.SuggestionForm()
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list+=[temp_sugg]

    # comments = models.CommentModel.objects.all()
    context = {
        "title":"Suggestions",
        "suggestions":suggestion_list,
        "form":suggestion_form,
        # "comments":comments
    }
    return render(request, "index.html", context=context)

def page(request, page=0):
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
    return render(request, "page.html", context=context)