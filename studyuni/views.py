from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from . import models
from django.shortcuts import redirect
import time
from django.utils.safestring import mark_safe


def index(request):
    # return HttpResponse("Hello, world.123   ")
    aaa = 555
    context = {'aaa': aaa}
    return render(request, 'sydneyuni/index.html', context)


def login(request):
    context = {"state": " "}
    if request.method == 'GET':
        return render(request, 'sydneyuni/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = models.user.objects.get(username=username)
        if user.password == password:
            request.session['username'] = username
            # Redirect to a success page.
            return redirect('/select/')
        else:
            return render(request, 'sydneyuni/login.html')


def register(request):
    return render(request, 'sydneyuni/register.html')


def select(request):
    timetb = time.localtime()
    wk = time.strftime("%a", timetb)
    hour = int(time.strftime("%H", timetb))
    min = time.strftime("%M", timetb)
    if int(min) >= 30:
        hour = hour+1
    wk_str = wk+str(hour)+":00"
    print(wk_str)

    courses = models.course.objects.filter(starttime=wk_str)

    list1 = []

    for course in courses:
        start = course.starttime
        end = course.endtime
        timeline = start[3:]+" - "+end[3:]
        cid = course.id
        strdiv = mark_safe('<div class="mb2"><a class="act-but submit" href="' +
                           '/room?id='+str(cid)+'" style="color: #FFFFFF">'+course.cse+'</a></div>')
        ct = {"first": timeline, "second": strdiv}

        list1.append(ct)

    context = {"state": list1}

    return render(request, 'sydneyuni/select.html', context)


def room(request):
    if request.method == 'GET':
        cid = request.GET['id']
        cs = models.course.objects.get(id=cid)
        cn = cs.cse
        room = models.room.objects.get(cseid=cid)

        sess = str(request.session['username'])
        user = models.user.objects.get(username=sess)
        uid = user.id

        if room.site1 is None:
            room.site1 = user.id
        elif room.site2 is None:
            room.site2 = user.id
        elif room.site3 is None:
            room.site3 = user.id
        elif room.site4 is None:
            room.site4 = user.id
        elif room.site5 is None:
            room.site5 = user.id
        elif room.site6 is None:
            room.site6 = user.id
        elif room.site7 is None:
            room.site7 = user.id
        elif room.site8 is None:
            room.site8 = user.id
                

        cap = sess[0].capitalize()
        print(room)
        print(room.site2)

        list1=[430,540,660,770,890,1000,1120,1230]
        list2=[300,430,540,650,]

        divsit = mark_safe('<div id="person" class="circle-text" style="background-color:#f309e7; top: 430px; left: 540px;">'+cap+'</div>')
        context={"divr": divsit, "cname": cn}
        
        return render(request, 'sydneyuni/room.html', context)
    else:
        return render(request, 'sydneyuni/room.html')
