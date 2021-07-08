from django import forms
from .models import products

class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['product_id','product_category','product_name','product_image','product_stock','product_price','sale_price','description']

class updateProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['product_image','product_stock','product_price','sale_price','description']