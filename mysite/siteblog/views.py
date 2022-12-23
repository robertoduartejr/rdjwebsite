from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from taggit.models import Tag
from django.template.defaultfilters import slugify
from .forms import VisitorsPost

# Create your views here.
def home(request):
    if request.method == "POST":
        form = VisitorsPost()
        if form.is_valid():
            visitors_post = form.save()


        return redirect('home')



    projects = Project.objects.all()[:3]
    common_tags = Project.tags.most_common()[:4]
    return render(request, 'home.html', {'projects':projects,'common_tags': common_tags, 'hide':True})

def all_projects(request):
    projects = Project.objects.all()
    common_tags = Project.tags.most_common()[:4]

    return render(request, 'home.html', {'projects':projects,'common_tags': common_tags, 'hide':False})

def project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'project.html', {'project': project})



def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug) #get specific tag by its slug
    projects = Project.objects.filter(tags=tag)
    common_tags = Project.tags.most_common()[:4]
    return render(request, 'home.html', {'projects': projects, 'tag': tag, 'common_tags':common_tags})
