from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import products,Friends,product_views
from .forms import productsForm, updateProductForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
import json
jsonDec = json.decoder.JSONDecoder()
from django.contrib.auth.models import User

# Create your views here.
@login_required
def items(request):
    # template = loader.get_template('marketplace/items.html')
    item_list = products.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'marketplace/items.html',context)


@login_required
def detail(request,product_id):

    product_detail = products.objects.get(product_id=product_id)

    #update in product_view table
    if product_detail.user_name.id != request.user.id:
        if product_views.objects.filter(user_id=request.user.id).exists():
            product_view_obj = product_views.objects.get(user_id=request.user.id)
            product_view_list =  jsonDec.decode(product_view_obj.views_list)
            if product_id not in product_view_list:
                product_view_list.append(product_id)
                product_view_obj.views_list = json.dumps(product_view_list)
                product_view_obj.save()
        else:
            data_list = []
            data_list.append(product_id)
            product_view_obj = product_views(user_id=request.user.id,views_list=json.dumps(data_list))
            product_view_obj.save()

    context = {
        'detail':product_detail,
    }
    return render(request,'marketplace/detail.html',context)

@login_required
def create_item(request):
    form = productsForm(request.POST or None)
    if form.is_valid():
        form.instance.user_name = request.user
        form.save()
        return redirect('marketplace:products')

    return render(request,'marketplace/add_items.html',{'form':form})


@login_required
def update_item(request,product_id):
    item = products.objects.get(product_id=product_id)
    form = updateProductForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('marketplace:products')

    return render(request,'marketplace/update_items.html',{'form':form,'item':item})

@login_required
def delete_item(request,product_id):
    item = products.objects.get(product_id=product_id)

    if request.method == 'POST':
        item.delete()
        return redirect('marketplace:products')

    return render(request,'marketplace/delete_items.html',{'item':item})

@login_required
def suggestions(request):

    user_id = request.user.id
    friends_obj = Friends.objects.get(user_id=user_id)

    friends_list = jsonDec.decode(friends_obj.friends_list)

    data_list = []
    for inc in friends_list:

        if User.objects.filter(id=inc).exists():
            user_date = User.objects.get(id = inc)
            
            if product_views.objects.filter(user_id=inc).exists():
                product_view_obj = product_views.objects.get(user_id=inc)
                product_view_list =  jsonDec.decode(product_view_obj.views_list)
                
                for inc_items in product_view_list:
                    item = products.objects.get(product_id=inc_items)
                    data_dict = {}
                    data_dict['name'] = item.product_name
                    data_dict['image'] = item.product_image
                    data_dict['sale_price'] = item.sale_price
                    data_dict['friend_name'] = user_date.username

                    if user_id != item.user_name.id:
                        data_list.append(data_dict)

    context = {
        'detail':data_list,
    }
    return render(request,'marketplace/suggestions.html',context)

@login_required
def friendsList(request):

    user_id = request.user.id
    friends_obj = Friends.objects.get(user_id=user_id)

    friends_list = jsonDec.decode(friends_obj.friends_list)

    data_list = []
    for inc in friends_list:

        if User.objects.filter(id=inc).exists():
            user_date = User.objects.get(id = inc)

            data_dict = {}
            data_dict['username'] = user_date.username
            data_dict['id'] = user_date.id

            data_list.append(data_dict)

    context = {
        'detail':data_list,
    }
    return render(request,'marketplace/friendslist.html',context)