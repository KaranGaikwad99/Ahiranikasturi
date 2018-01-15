from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Post, Gallery, Program
from .forms import Contact_usForm, Registration_Form

def HomePageView(request):
    prog_query=Program.objects.all().order_by('-id')[:2]
    post_query=Post.objects.all().order_by('-id')[:2]
    context={
            "prog_query":prog_query,
            "post_query":post_query,            
        }
    return render(request, "marathi/index.html", context)

def about_us(request):
    return render(request, "marathi/about_us.html")

def post_home(request):
    image_instanse=Gallery.objects.all().order_by('-id')[:6]
    queryset=Post.objects.all()#.order_by('-id')[:3]
    queryset1=Post.objects.filter().order_by('-id')[:6]
    paginator = Paginator(queryset, 2) # Show 2 Blog per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context={
            "image_instanse":image_instanse,
            "object_list":queryset,
            "object_tit":queryset1,            
        }
    return render(request, "marathi/blog.html", context)

def post_detail(request, id=None):
    image_instanse_d=Gallery.objects.all().order_by('-id')[:6]
    queryset2=Post.objects.filter().order_by('-id')[:6]
    instance=get_object_or_404(Post, id=id)
    context={
        "image_instanse_d":image_instanse_d,
        "title":instance.title,
        "instance":instance,
        "object_dtit":queryset2,
    }
    return render(request, "marathi/blog_detail.html", context)

def program(request):
    prog_image=Program.objects.all().order_by('-id')
    queryset=Program.objects.filter().order_by('-id')[:6]
    instance=Post.objects.all().order_by('-id')[:8]
    queryset1=Gallery.objects.filter().order_by('-id')[:8]

    paginator = Paginator(prog_image, 3)
    page = request.GET.get('page')
    try:
        prog_image = paginator.page(page)
    except PageNotAnInteger:
        prog_image = paginator.page(1)
    except EmptyPage:
        prog_image = paginator.page(paginator.num_pages)


    context={
            "prog_image":prog_image, 
            "queryset":queryset,
            "instance":instance,
            "queryset1":queryset1,    
        }
    return render(request, "marathi/program.html", context) 

def program_detail(request, id=None):
    prog_instance=get_object_or_404(Program, id=id)
    prog_d_ins=Program.objects.all().order_by('-id')[:6]
    gal_instanse=Gallery.objects.all().order_by('-id')[:6]
    pos_instanse=Post.objects.filter().order_by('-id')[:6]
    context={
        "title":prog_instance.title,
        "prog_instance":prog_instance,
        "prog_d_ins":prog_d_ins,
        "gal_instanse":gal_instanse,
        "pos_instanse":pos_instanse,
    }
    return render(request, "marathi/program_detail.html", context)


def gallery_home(request):
    queryset=Gallery.objects.all()#.order_by('-id')[:3]
    #queryset1=Gallery.objects.filter().order_by('-id')[:6]
    paginator = Paginator(queryset, 12)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context={
            "object_list":queryset,            
        }
    return render(request, "marathi/gallery.html", context)

def gallery_detail(request, id=None):
    instance=get_object_or_404(Gallery, id=id)
    context={
        "title":instance.title,
        "instance":instance,
    }
    return render(request, "marathi/gallery_detail.html", context)

def contact(request):
    form = Contact_usForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(contact)
    context = {
        "form": form,
    }
    return render(request, "marathi/contact.html",context) 

def registration(request):
    form = Registration_Form(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(registration)
    context = {
        "form": form,
    }
    return render(request, "marathi/registration.html",context) 


















