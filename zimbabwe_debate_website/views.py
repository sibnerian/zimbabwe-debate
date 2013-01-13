from django.shortcuts import render_to_response
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Context, loader
from django.http import HttpResponse
from zimbabwe_debate_website.models import Member, Sponsor

def index(request):
    return render_to_response('website/index.html')

def about(request):
    return render_to_response('website/about.html')

def members(request):
    members = Member.objects.all().order_by('name')
    """
    paginator = Paginator(members, 20)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    """
    t = loader.get_template('website/members.html')
    c = Context({
        'members': members,
    })
    return HttpResponse(t.render(c))

def sponsors(request):
    sponsors = Sponsor.objects.all().order_by('name')
    """
    paginator = Paginator(sponsors, 20)
    page = request.GET.get('page')
    try:
        sponsors = paginator.page(page)
    except PageNotAnInteger:
        sponsors = paginator.page(1)
    except EmptyPage:
        sponsors = paginator.page(paginator.num_pages)
    """
    t = loader.get_template('website/sponsors.html')
    c = Context({
        'sponsors': sponsors,
    })
    return HttpResponse(t.render(c))