from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect

from polls.form import PersonForm
from polls.models import Question, Choice, User, Person
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:]
    context = {'latest_question_list': latest_question_list}

    # print(latest_question_list)
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/index.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
             })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('/')


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})



def register(request):   #회원가입
    if request.method == "GET":
        return render(request, 'uuser/register.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User(username=username, password=make_password(password))
        user.save()
        return redirect('/')
        # return render(request, 'uuser/register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'uuser/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            a = User.objects.get(username=username)
            if check_password(password, a.password):
                #비밀번호가 일치, 로그인 처리됨!
                return redirect('/')
                # return render(request, '/')

            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'


        return render(request, 'uuser/login.html', res_data)


# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return render(request, '/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'polls/index.html')



def form_test(request):
    person_list = Person.objects.order_by('-name')
    context = {'person_list': person_list}
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            obj = Person(name=form.data['name'], text=form.data['text'])
            obj.save()
            return render(request, 'polls/indexx.html', context)
        return HttpResponse('fail')
    elif request.method == 'GET':
        form = PersonForm()
        return render(request, 'uuser/form.html', {'form': form})
    else:
        pass

def person_test(request):
    person_list = Person.objects.order_by('-name')
    context = {'person_list': person_list}
    return render(request, 'polls/indexx.html', context)


def person_test_detail(request, pid):
    person = Person.objects.get(pk=pid)
    context = {'person': person}
    return render(request, 'polls/detaill.html', context)



from django.shortcuts import render

# Create your views here.