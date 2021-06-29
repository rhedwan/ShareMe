from django.urls import path
from .views import StoreListView, StoreEditView, StoreDetailView , StoreAddView , CategoryView

urlpatterns = [
    path('', StoreListView.as_view(), name='home'),
    path('edit_item/<int:pk>/', StoreEditView.as_view(), name='edit_item'),
    path('detail_item/<int:pk>/', StoreDetailView.as_view(), name='detail_item'),      
    path('add_post/', StoreAddView.as_view(), name='add_post'),
    path( 'category/<int:pk>/<slug:slug>/', CategoryView.as_view(), name='category'),
]