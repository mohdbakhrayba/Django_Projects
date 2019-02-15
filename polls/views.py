from django.shortcuts import render

# Create your views here.
#from django.http import Http404
#from django.http import HttpResponse , HttpResponseRedirect
#from django.urls import reverse
#from django.views import generic
#from django.shortcuts import get_object_or_404 , render
#from .models import Choice, Question

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name= 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions,( not including thoses set
        to be published in the future"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
        # return HttpResponse("Youre voting on question %s " % question_id)
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didnt select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))






#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context,request))

# or you can use
# context = {'latest_question_list': latest_question_list}
# return render(request, 'polls/index.html',context)

# if you follow this pattern,you dont reqwuire loader and HttpResponse

#def detail(request, question_id):
  #  try:
   #     question = Question.objects.get(pk=question_id)
  #  except Question.DoesNotExist:
   #     raise Http404("Question does not exist")
   # return render(request, 'polls/detail.html' , {'question' : question})

#return HttpResponse("Youre looking at question %s. " % question_id)

#    question= get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html',{'question': question})

#def results(request, question_id):
   # response = "Youre looking at the results of question %s. "
   # return HttpResponse(response % question_id)
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', {'question': question})


