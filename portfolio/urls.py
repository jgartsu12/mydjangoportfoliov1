"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import johngartsu.views
import companies.views
import projects.views
import blogs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', johngartsu.views.homepage, name='home'),
    path('companies/', companies.views.companypage, name='companies'),
    path('companies/<int:company_id>', companies.views.companydetail, name='company-detail'),
    path('projects/', projects.views.projectspage, name='projects'),
    path('projects/<int:project_id>', projects.views.projectdetail, name='project-detail'),
    path('blogs/', blogs.views.BlogList.as_view(), name='blogs'),
    path('<slug:slug>/', blogs.views.BlogDetail.as_view(), name='blog_detail'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)