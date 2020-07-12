from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Querstion, Choice

from django.http import Http404
from django.template import loader


# Create your views here.

def index(request):
    latest_question_list = Querstion.objects.order_by('-pub_date')
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)  # 一个快捷函数，载入模板，填充上下文，再返回由它生成的HttpResponse对象，是一个非常常用的操作流程。


def detail(request, question_id):
    # try:
    #     question = Querstion.objects.get(pk=question_id)
    # except Querstion.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Querstion, pk=question_id)  # 使用快捷函数
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Querstion, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Querstion, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # choice_set 因为Choice上由Question的外键,所以Question实例上会自动生成一个名为foo_set的字段,其中foo是具有该模型的外键字段的模型
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
