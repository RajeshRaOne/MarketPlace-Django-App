from . import views
from django.urls import path

app_name = 'marketplace'
urlpatterns = [
    #products view 
    path('products/', views.items,name='products'),
    #view product details
    path('products/<int:product_id>', views.detail,name='detail'),
    #add products
    path('products/add/',views.create_item,name="create_item"),
    #update products
    path('products/update/<int:product_id>',views.update_item,name="update_item"),
    #delete products
    path('products/delete/<int:product_id>',views.delete_item,name="delete_item"),
    path('products/suggestions/',views.suggestions,name="suggestions"),
    path('products/friendsList/',views.friendsList,name="friendsList"),
]