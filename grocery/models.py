from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator

# Create your models here.
CATEGORY_CHOICES =(('kitchen','kitchen'),
                    ('babywear','babywear'),
                    ('soaps','soaps'),
                    ('handlooms','handlooms'),
                    ('household','household'),
                    ('sweets','sweets'),
                    ('choclate','choclate'),

                   )

LABEL_CHOICES = (
    ('New','primary'),
    ('offer','secondary'),
    ('discount','danger')
)

class Shop_categories(models.Model):
    Category_Shop = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.Category_Shop


class Registered_shop(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    Shop_category = models.ForeignKey(to=Shop_categories,on_delete=CASCADE,null=True,blank=True)
    shop_name = models.CharField(max_length=200, null=False)
    Retailer_name = models.CharField(max_length=200,null=False)
    shop_address  =models.TextField(null=False)
    shop_img = models.ImageField(upload_to='shopimg', null=True, blank=True)
    Landmark = models.TextField(null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    pin_no = models.IntegerField(null=False)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=12)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name

    @property
    def shop_imgURL(self):
        try:
            url = self.shop_img.url
        except:
            url = ' '
        return url


class Member_As(models.Model):
    member = models.CharField(max_length=100,default='Customer')
    def __str__(self):
       return self.member

class Profile(models.Model):
    shop = models.ForeignKey(to=Registered_shop,on_delete=CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    member = models.ForeignKey(to=Member_As, on_delete=CASCADE, default=1,null=True, blank=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    pin_no = models.IntegerField(null=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=15,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profilepic',null=True,blank=True)

    def __str__(self):
       return "%s (%s)" %(self.user,self.member)

    @property
    def profile_picURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ' '
        return url


class Category(models.Model):
    item_category_name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    def __str__(self):
        return self.item_category_name

class Kitchen_item_category(models.Model):
    item_category = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.item_category


class HouseHold_item_category(models.Model):
    item_category = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.item_category



class Customer(models.Model):
    user =models.OneToOneField(to=User, on_delete=CASCADE, null=True, blank=True,)
    name =models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.name

class item(models.Model):
    shop = models.ForeignKey(to=Registered_shop, on_delete=CASCADE,null=True,blank=True)
    special_offer = models.BooleanField(default=False,null=True,blank=True)
    category = models.ForeignKey(to=Category,related_name='items',on_delete=CASCADE,null=True,blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    item_name = models.CharField(max_length=100)
    decription = models.TextField(blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default = None)
    item_img = models.ImageField(upload_to='upload',null=True,blank=True)
    discount_price = models.FloatField(blank =True,null= True)
    Kitchen_category = models.ForeignKey(to=Kitchen_item_category,on_delete=models.SET_NULL, null=True, blank=True)
    Household_category = models.ForeignKey(to=HouseHold_item_category, on_delete=models.SET_NULL, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=15)
    digital = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ['-created_date']
        index_together=(('id','slug'),)
    def __str__(self):
        return self.item_name
    @property
    def item_imgURL(self):
        try:
            url = self.item_img.url
        except:
            url = ' '
        return url


class top_product_item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    item_img = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title
    @property
    def item_imgURL(self):
        try:
            url=self.item_img.url
        except:
            url = ' '
        return url



class Special_Offer_item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    item_img = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title
    @property
    def item_imgURL(self):
        try:
            url=self.item_img.url
        except:
            url = ' '
        return url




class order(models.Model):

    cutomer = models.ForeignKey(to=Customer, on_delete=CASCADE, null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True ,null=True)
    ordered_complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100 ,default=' ')
    def __str__(self):
        return str(self.cutomer)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.item_ordered.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class Shipping(models.Model):
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=12,null=True,blank=True)
    cutomer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(to=order, on_delete=models.SET_NULL, null=True)
    address =models.TextField(null=False)
    Landmark = models.TextField(null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    pin_no = models.IntegerField(default=815353)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cutomer.name




class orderitem(models.Model):

    payment_status = models.BooleanField(default=False)
    shippAddress = models.ForeignKey(to=Shipping,on_delete=CASCADE,null=True,blank=True)
    shop = models.ForeignKey(to=Registered_shop, on_delete=CASCADE,null=True,blank=True)
    item_ordered = models.ForeignKey(to=item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=order, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.item_ordered.item_name

    @property
    def get_total(self):
        total = self.item_ordered.price * self.quantity
        return total



