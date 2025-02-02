from django.http import HttpResponse
from django.template import loader
from members.models import Member


def members(request):
    paw_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'paw_members': paw_members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    paw_member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'paw_member': paw_member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
