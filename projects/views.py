from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def projectspage(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects': projects})

def projectdetail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project-detail.html', {'project':project_detail})