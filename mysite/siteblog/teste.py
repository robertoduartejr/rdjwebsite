def provide_json(request, *args, **kwargs):
    print(kwargs)
    upper = kwargs.get('num_projects')
    lower = upper - 3
    slug = kwargs.get('slug')
    tag = get_object_or_404(Tag, slug=slug)  # get specific tag by its slug
    projects = Project.objects.filter(tags=tag)[lower:upper]

    if not projects: #se eu estiver na pagina principal, o filtro não vai achar nada, se não achar nada entro nesse if e devolvo tds os projetos
        print("testando se entrou aqui")
        projects = list(Project.objects.values())[lower:upper]
        projects_size = len(Project.objects.all())
        size = True if upper >= projects_size else False
        return JsonResponse({'data': projects, 'max': size}, safe=False)

    projects = list(Project.objects.filter(tags=tag).values())[lower:upper]
    projects_size = len(Project.objects.all())
    size = True if upper >= projects_size else False
    return JsonResponse({'data':projects, 'max': size}, safe=False)