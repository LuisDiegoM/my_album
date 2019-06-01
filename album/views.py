from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category
from album.models import Photo
from django.views.generic import ListView,DetailView
from django.views.generic import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

#def first_view(request):
 #   return HttpResponse("<h1>Esta </h1> es la primera vista!<br><input type='text'> <br> <input type=button value=BOTON>")
#def selection_detail(request,selection_id):
 #   selection = Selection.objects.get(id=selection_id)# hace referencia a un select ... where 
  #  context = {'object': selection}
   # return render(request, 'album/selection_detail.html',context)

def first_view(request):
    return HttpResponse('Esta es mi primera vista')

def base(request):
   return render(request,'base.html')
    
'''def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category_list.html', context)'''

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)


def Photo(request):
    photo_list = Category.objects.all()
    context = {'object_list': photo_list}
    return render(request, 'album/photo_detail.html', context)
    
class CategoryListView(ListView):
 model = Category

class PhotoListView(ListView):
 model = Photo

class PhotoDetailView(DetailView):
 model = Photo

class PhotoUpdate(UpdateView):
   model = Photo

class PhotoCreate(CreateView):
   model = Photo

class PhotoDelete(DeleteView):
   model = Photo
   success_url = reverse_lazy('photo-list')
