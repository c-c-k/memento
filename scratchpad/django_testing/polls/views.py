from django.shortcuts import (
    render, redirect, get_object_or_404)
from django.http import HttpResponse, HttpRequest
# from django.views import View

from .models import repopulate_polls, Choice, Question


def index(request):
    questions = Question.objects.order_by('-publication_date')[:3]
    context = {
        "questions": questions
    }
    return render(request, "polls/index.html", context=context)


def delete_question(request):
    question = get_object_or_404(Question, id=request.GET["question_id"])
    question.delete()
    return redirect("polls:index")


def delete_choice(request: HttpRequest):
    choice_id = request.GET["choice_id"]
    source = request.GET["source"]
    print(source)
    choice = get_object_or_404(Choice, id=choice_id)
    choice.delete()
    return redirect(source)


def repopulate(request):
    repopulate_polls()
    return redirect("polls:index")


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {"question": question}
    return render(request, "polls/results.html", context)


