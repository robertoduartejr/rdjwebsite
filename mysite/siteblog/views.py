from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, VisitorsPost
from taggit.models import Tag
from django.template.defaultfilters import slugify
from .forms import Post
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            # print("entrou aqui")
            # content = form['content']
            # project = "central"
            # user = request.user
            # post = VisitorsPost.objects.create(content=content, project=project, user=user)
            # post.save_model()
            # print("entrou aqui2")
            # projects = Project.objects.all()[:3]
            # common_tags = Project.tags.most_common()[:4]
            # form = Post()
            post = form.save(commit=False)
            post.user = request.user
            post.project = None
            post = post.save()


            projects = Project.objects.all()[:3]
            common_tags = Project.tags.most_common()[:4]
            form = Post()

            posts = VisitorsPost.objects.all()
            return render(request, 'home.html',
                          {'projects': projects, 'common_tags': common_tags, 'hide': True, 'form': form,'posts':posts})


    projects = Project.objects.all()[:3]
    common_tags = Project.tags.most_common()[:4]
    posts = VisitorsPost.objects.all()
    form = Post()
    return render(request, 'home.html', {'projects':projects,'common_tags': common_tags, 'hide':True, 'form':form, 'posts':posts})

def provide_json(request, *args, **kwargs):
    print(kwargs)
    upper = kwargs.get('num_projects')
    lower = upper - 3
    projects = list(Project.objects.values())[lower:upper]
    projects_size = len(Project.objects.all())
    size = True if upper >= projects_size else False
    return JsonResponse({'data':projects, 'max': size}, safe=False)





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


# def post(request):
#     print("aqui simmmmm")
#     if request.method == "POST":
#         form = Post(request.POST)
#         print("aqui sim")
#         if form.is_valid():
#             print("entrou aqui")
#             content = form['content']
#             project = "central"
#             user = request.user
#             post = VisitorsPost.objects.create(content=content,project=project,user=user)
#             post.save()
#             print("entrou aqui2")
#             projects = Project.objects.all()[:3]
#             common_tags = Project.tags.most_common()[:4]
#             form = Post()
#             return render(request, 'home.html',
#                           {'projects': projects, 'common_tags': common_tags, 'hide': True, 'form': form})
#
#     projects = Project.objects.all()[:3]
#     common_tags = Project.tags.most_common()[:4]
#     form = Post()
#     print("vem direto aqui")
#     return render(request, 'home.html',
#                   {'projects': projects, 'common_tags': common_tags, 'hide': True, 'form': form})

