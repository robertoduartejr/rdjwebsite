import os.path

from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, VisitorsPost
from taggit.models import Tag
from django.template.defaultfilters import slugify
from .forms import Post
from django.http import JsonResponse, StreamingHttpResponse
from django.contrib.auth.models import User
from datetime import date
from wsgiref.util import FileWrapper
import mimetypes

# Create your views here.
def home(request):
    print(date.today())
    slug = "nao-existe" #slug qualquer pra fazer chamada
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


            common_tags = Project.tags.most_common()[:4]
            form = Post()

            posts = VisitorsPost.objects.all()
            return render(request, 'home.html',
                          {'common_tags': common_tags, 'hide': True, 'form': form,'posts':posts, 'slug':slug}) #envio um slug qualquer pra fazer chamada


    projects = Project.objects.all()[:3]
    common_tags = Project.tags.most_common()[:4]
    posts = VisitorsPost.objects.all()
    form = Post()
    return render(request, 'home.html', {'projects':projects,'common_tags': common_tags, 'hide':True, 'form':form, 'posts':posts, 'slug':slug}) #envio um slug qualquer pra fazer chamada

def downloadfile(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'CV - Roberto Duarte.pdf'
    thefile = base_dir + '\\static\\files\\' + filename
    filename = os.path.basename(thefile)
    chunck_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunck_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response


def provide_json(request, *args, **kwargs):
    print(kwargs)
    upper = kwargs.get('num_projects')
    lower = upper - 3
    slug = kwargs.get('slug')
    print("TEM Q CHEGAR AQUI")
    try: #utilizei o try pra proteger a pagina principal. Pagina principal n??o tem tag, ent??o a fun????o get object abaixo nao acharia nada e daria um erro.
        tag = get_object_or_404(Tag, slug=slug)  # get specific tag by its slug
        projects = Project.objects.filter(tags=tag)[lower:upper]
        print(projects,"OQ ROLA AQUI")

        projects = list(Project.objects.filter(tags=tag).values())[lower:upper]
        projects_size = len(Project.objects.all())
        size = True if upper >= projects_size else False
        return JsonResponse({'data':projects, 'max': size}, safe=False)

    except:
        print("testando se entrou aqui")
        projects = list(Project.objects.values())[lower:upper]
        projects_size = len(Project.objects.all())
        size = True if upper >= projects_size else False
        return JsonResponse({'data': projects, 'max': size}, safe=False)

def provide_json_posts(request, *args, **kwargs):
    print(kwargs)
    upper = kwargs.get('num_posts')
    lower = upper - 3
    slug = kwargs.get('slug')
    project = Project.objects.filter(slug=slug) #escondi no hidden do html uma slug que de fato n??o existe, pra caso eu esteja na pagina principal

    if not project: #se eu estiver na pagina principal, o filtro n??o vai achar nada, se n??o achar nada entro nesse if e devolvo tds os posts sem projeto vinculado
        print("testando se entrou aqui")
        posts = list(VisitorsPost.objects.filter(project__isnull=True).values())[lower:upper]
        posts_size = len(VisitorsPost.objects.filter(project__isnull=True))
        size = True if upper >= posts_size else False
        return JsonResponse({'data':posts, 'max': size}, safe=False)
    else:
        project = Project.objects.get(slug=slug)
        posts = list(VisitorsPost.objects.filter(project=project).values())[lower:upper]
        posts_size = len(VisitorsPost.objects.filter(project=project))
        size = True if upper >= posts_size else False
        print(kwargs.get('slug'))
        return JsonResponse({'data': posts, 'max': size}, safe=False)



def provide_json_users(request):
    users = list(User.objects.values('id','first_name','last_name'))
    return JsonResponse({'data': users}, safe=False)


def project(request, slug):
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post_project = Project.objects.get(slug=slug)
            post.project = post_project
            post = post.save()


            form = Post()
            posts = VisitorsPost.objects.filter(project=post_project)
            print(posts)
            project = Project.objects.get(slug=slug)
            return render(request, 'project.html',
                          {'project': project, 'form': form,'posts':posts})



    project = Project.objects.get(slug=slug)
    form = Post()
    post_project = Project.objects.get(slug=slug)
    posts = VisitorsPost.objects.filter(project=post_project)
    print(posts)
    return render(request, 'project.html', {'project': project, 'form': form,'posts':posts})


def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug) #get specific tag by its slug
    projects = Project.objects.filter(tags=tag)
    common_tags = Project.tags.most_common()[:4]
    print(slug)
    slug = slug
    form = Post()
    return render(request, 'home.html', {'projects': projects, 'tag': tag, 'common_tags':common_tags, 'slug':slug, 'form':form})


#functions to handle 404 and 500 errors
def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})


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

