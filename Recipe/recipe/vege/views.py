from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_des = data.get('recipe_des')
    
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_des = recipe_des,
        )
        
        return redirect('/')
        
    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    
    context = {'receipes':queryset}
        
    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')


def update_receipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_des = data.get('recipe_des')
        
        queryset.recipe_name = recipe_name,
        queryset.recipe_des = recipe_des,
        
        if  recipe_image:
            queryset.recipe_image =  recipe_image
        
        queryset.save()
        return redirect('/')
    context = {'receipes':queryset}
    return render(request,'update_receipes.html',context)