from django.shortcuts import render
from django.http import HttpResponse, Http404
from teaminfo.models import Teams
from django.template import loader
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.db.models
# Create your views here.
def index(request):
    # data=pd.read_pickle("teamfuncs/sridata.pkl")
    # for num, opr, mscr in zip(data["Team Number"], data["OPR"], data["Max Score"]):
    #      opr_per = stats.percentileofscore(data["OPR"], opr)
    #      mscr_per = stats.percentileofscore(data["Max Score"], mscr)
    #      t = Teams(team_number=num, team_opr=opr, team_mscore=mscr, team_opr_quantile=opr_per, team_mscore_quantile=mscr_per)
    #      t.save()

    # http://materializecss.com/pagination.html
    team_list = Teams.objects.all()

    paginator = Paginator(team_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        team_list = paginator.get_page(page)
    except PageNotAnInteger:
        team_list = paginator.page(1)
    except EmptyPage:
        team_list = paginator.page(paginator.num_pages)
    context = {
        'team_list': team_list,
    }

    if request.method == 'POST':
        filter = request.POST.get('filter')
        context['filter'] = filter
        return render(request, 'teaminfo/index.html', context)


    return render(request, 'teaminfo/index.html', context)



def detail(request, team_number):
    try:
        team_num = Teams.objects.get(team_number=team_number)
    except Teams.DoesNotExist:
        return render(request, 'teaminfo/404.html')
    opr = team_num.team_opr
    mscore = team_num.team_mscore
    opr_per = team_num.team_opr_quantile
    mscore_per = team_num.team_mscore_quantile

    context = {
        'team_number': team_number,
        'opr': opr,
        'mscore': mscore,
        'opr_per': opr_per,
        'mscore_per': mscore_per,
    }
    return render(request, 'teaminfo/detail.html', context)

def division(request):
    context = {
        'data' : 'data',
    }
    return render(request, 'teaminfo/division.html', context)

    # context = {
    #     'this':'that',
    # }
    # return render(request, 'teaminfo/division.html', context)

def vote(request):
    return HttpResponse("You're voting on team")
