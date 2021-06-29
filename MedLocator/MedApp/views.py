from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, UpdateView, DetailView , CreateView
from .models import StoreItem ,StoreCategory
from .forms import StoreItemForm 
# Create your views here.


class CategoryView(ListView):
    model = StoreItem
    template_name = 'category.html'
    context_object_name = 'posts'


    def get_queryset(self):
        self.category = get_object_or_404(StoreCategory, pk= self.kwargs['pk'])
        return StoreItem.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        self.category = get_object_or_404(StoreCategory, pk= self.kwargs['pk'])
        context['category'] = self.category
        return context





class StoreListView(ListView):
    model = StoreItem
    template_name = 'home.html'

class StoreDetailView(DetailView):
    model = StoreItem
    template_name = 'item_detail.html'


class StoreEditView(UpdateView):
    model = StoreItem
    template_name = 'edit_item.html'
    # fields ='__all__'

class StoreAddView(CreateView):
    model = StoreItem
    template_name = 'add_item.html'
    # fields ='__all__'
    form_class = StoreItemForm
