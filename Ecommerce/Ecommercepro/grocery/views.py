from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import JsonResponse
import json
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,CreateView,HttpResponseRedirect
from .models import item,order,orderitem,Customer,HouseHold_item_category,Kitchen_item_category,Shipping,Profile,Registered_shop

from .forms import itemForm

class HomeView(ListView):
    model = item
    template_name = 'index.html'


class ItemDetailView(DetailView):
    model = item
    template_name = 'product.html'


def home(request):
    monthlyorderitem = orderitem.objects.all()
    for i in monthlyorderitem:
        sliceddate = i.date_ordered.strftime("%d-%b-%Y ")
        dddd = sliceddate[3:12]
        month = "Jun-2020"
        if dddd == month:
            print(dddd)
    if request.user.is_authenticated:
       city = request.user.profile.city
       context = {
           'items': item.objects.all(),
           'kitchencategory': Kitchen_item_category.objects.all(),
           'householdcategory': HouseHold_item_category.objects.all(),
           'offeritem': item.objects.all(),
           'shops': Registered_shop.objects.filter(city=city)
       }

       return render(request, 'grocery/index.html', context)

    else :
        context = {
        'items': item.objects.all(),
        'kitchencategory':Kitchen_item_category.objects.all(),
        'householdcategory': HouseHold_item_category.objects.all(),
        'offeritem': item.objects.all(),

        }

        return render(request,'grocery/index.html',context)

def about(request):

    return render(request,'grocery/about.html')

def help(request):

    return render(request,'grocery/help.html')

def payment(request):

    return render(request,'grocery/payment.html')

def contact(request):

    return render(request,'grocery/contact.html')

def privacy(request):

    return render(request,'grocery/privacy.html')

def faqs(request):

    return render(request,'grocery/faqs.html')



def productshopnow(request):
    items = item.objects.all()
    return render(request,'grocery/product.html', {'items':items})


@login_required
def registershopnow(request):

    return render(request,'grocery/registershop.html')



def product(request,pk):
    items = item.objects.filter(Kitchen_category_id=pk)
    return render(request,'grocery/product.html', {'items':items})



def product2(request):

    return render(request,'grocery/product2.html')


def product(request):

    return render(request,'grocery/product.html')

def single(request,pk):
    single_item = item.objects.filter(id = pk)

    return render(request,'grocery/single.html',{'item_single':single_item})

def special_offeer_single(request,pk):
    single_item = item.objects.filter(id = pk)

    return render(request,'grocery/single.html',{'item_single':single_item})



def calander(request):

    return render(request,'grocery/calander.html')

def homepg_single(request,pk):
    single_item = item.objects.filter(id = pk)

    return render(request,'grocery/single.html',{'item_single':single_item})


def single2(request):

    return render(request,'grocery/single2.html')


def terms(request):

    return render(request,'grocery/terms.html')


def profileview(request):
    user_profile = Profile.objects.filter(user = request.user).first()
    my_shop = Registered_shop.objects.filter(user = request.user)
    print(user_profile)
    context = {'proflintro':user_profile,'my_shop':my_shop}
    return render(request,'grocery/profile.html',context)

@login_required
def Myshop(request,pk):

    my_shop = Registered_shop.objects.filter(id = pk)
    items = item.objects.filter(shop_id = pk),
    context = {'myshop':my_shop,
               'items':item.objects.filter(shop_id = pk),
               'shopId':pk
               }

    return render(request,'grocery/Myshop.html',context)



@login_required
def myorder(request):

    myorderitem = orderitem.objects.all()

    context = {'MYORDER':myorderitem}

    return render(request,'grocery/Myorder.html',context)



def uploadproduct(request,pk):
    data = {'shop_id': pk}
    form = itemForm(request.POST or None, request.FILES or None, data)
    if form.is_valid():
        new = form.save(commit=False)
        new.shop_id = pk
        new.save()
        return redirect("/grocery/profile")
    context = {'form': form}
    return render(request,'grocery/uploadProduct.html',context)

def MyDashboard(request,pk):
   data = orderitem.objects.filter(shop_id=pk,payment_status=True)
   context ={'data':data,

             }
   return render(request,'grocery/Mydashboard.html',context)

def shippinfo(request,pk):
   data = Shipping.objects.filter(order_id=pk)
   context ={'data':data,

             }
   return render(request,'grocery/shippinfo.html',context)



@method_decorator(login_required, name ="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = {'profile_pic','name','phone_no','address','city','pin_no','state'}

class Registered_shopUpdateView(UpdateView):
    model = Registered_shop
    fields = {'shop_img', 'shop_name','Retailer_name', 'phone_no', 'shop_address', 'city', 'pin_no', 'state'}


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created =order.objects.get_or_create(cutomer=customer,ordered_complete = False)
        items = Order.orderitem_set.all()
        cartItems = order.get_cart_items
        return render(request, 'grocery/cart.html', {'items': items, 'Order':Order,'cartItems':cartItems})

    else:
        items=[]
        Order = {'get_cart_items':0,'get_cart_total':0}

        return render(request,'grocery/cart.html',{'items':items})




def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created =order.objects.get_or_create(cutomer=customer,ordered_complete = False)
        items = Order.orderitem_set.all()
        cartItems = order.get_cart_items

        return render(request, 'grocery/checkout.html', {'items': items,'Order':Order,'cartItems':cartItems})

    else:
        items=[]
        Order = {'get_cart_items':0,'get_cart_total':0}

        return render(request,'grocery/checkout.html',{'items':items,'Order':Order})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = item.objects.get(id=productId)
    findstok = item.objects.filter(id=productId)
    for i in findstok:
        stok = i.stock
        print(stok)
        if stok < 1 :
            item.objects.filter(id=productId).delete()

    Order, created = order.objects.get_or_create(cutomer=customer, ordered_complete=False)

    orderItem, created = orderitem.objects.get_or_create(order=Order, item_ordered=product,shop_id=product.shop_id)

    if action == 'add':
       orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
       orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if action == 'delete':
        orderItem.delete()

    if orderItem.quantity <= 0:
       orderItem.delete()

    return JsonResponse('Item was added to the cart', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created = order.objects.get_or_create(cutomer=customer, ordered_complete=False)
        total = float(data['form']['total'])
        Order.transaction_id = transaction_id

        if total == Order.get_cart_total:
            Order.ordered_complete = True
            Order.save()

        if Order.shipping == True and Order.ordered_complete == True:
           orderitem.objects.filter(order_id=Order.id).update(payment_status=True)
           updatestock = orderitem.objects.filter(order_id=Order.id)
           for i in updatestock:
               itemid = i.item_ordered.id
               stok=i.item_ordered.stock
               stocky=i.quantity
               rem = stok-stocky
               item.objects.filter(id =itemid).update(stock=stok-stocky)
               if rem < 1:
                   item.objects.filter(id=itemid).delete()

           Shipping.objects.create(
           cutomer=customer,
           order=Order,
           address=data['shipping']['address'],
           phone_no=data['shipping']['number'],
           Landmark=data['shipping']['landmark'],
           city=data['shipping']['city'],
           state=data['shipping']['state'],
           pin_no=data['shipping']['pincode']
           )

    return JsonResponse('Payment submitted..', safe=False)


def registershop(request):

    data = json.loads(request.body)
    print(data)
    if request.user.is_authenticated:
           shopkeeper = request.user
           Registered_shop.objects.create(
           user=shopkeeper,
           shop_address=data['shopInfo']['address'],
           Retailer_name=data['shopInfo']['retailername'],
           shop_name=data['shopInfo']['shopname'],
           phone_no=data['shopInfo']['number'],
           Landmark=data['shopInfo']['landmark'],
           city=data['shopInfo']['city'],
           state=data['shopInfo']['state'],
           pin_no=data['shopInfo']['pincode']
        )

    return JsonResponse('Shop Register Form submitted..', safe=False)




