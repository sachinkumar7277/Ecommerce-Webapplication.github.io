from django.contrib import admin
from .models import item,orderitem,order,top_product_item,Shipping,Customer,Kitchen_item_category,Special_Offer_item,HouseHold_item_category,Category,Profile,Member_As,Registered_shop,Shop_categories
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class top_product_itemAdmin(ModelAdmin):
    list_display = ['title', 'price','discount_price']
    search_fields = ['title' ]

admin.site.register(top_product_item, top_product_itemAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['item_category_name', 'slug']
    search_fields = ['item_category_name']
    prepopulated_fields = {'slug':('item_category_name',)}
admin.site.register(Category, CategoryAdmin)

class Shop_categoriesAdmin(ModelAdmin):
    list_display = ['Category_Shop', 'slug']
    search_fields = ['Category_Shop']
    prepopulated_fields = {'slug':('Category_Shop',)}
admin.site.register(Shop_categories, Shop_categoriesAdmin)

class itemAdmin(ModelAdmin):
    list_display = ['item_name', 'price','discount_price','category','stock','slug','available','created_date','updated_date','special_offer']
    search_fields = ['item_name','category','updated_date','created_date','special_offer']
    list_editable = ['price','discount_price','available','stock','special_offer',]
    prepopulated_fields = {'slug':('item_name',)}
admin.site.register(item, itemAdmin)



class ShippingAdmin(ModelAdmin):
    list_display = ['cutomer', 'order','phone_no','address','Landmark','city']
    search_fields = ['cutomer','order','phone_no','address']

admin.site.register(Shipping,ShippingAdmin)
admin.site.register(Customer)



class orderAdmin(ModelAdmin):
    list_display = ['cutomer','transaction_id','ordered_complete','ordered_date']
    search_fields = ['transaction_id','cutomer','ordered_date']
admin.site.register(order,orderAdmin)

class orderitemAdmin(ModelAdmin):
    list_display = ['item_ordered','order','quantity','shop','payment_status']
    search_fields = ['order' ,'item_ordered','shop']
admin.site.register(orderitem,orderitemAdmin)

class Registered_shopAdmin(ModelAdmin):
    list_display = ['Retailer_name','shop_name','phone_no','shop_address','city']
    search_fields = ['Retailer_name','shop_name','phone_no']

admin.site.register(Registered_shop,Registered_shopAdmin)


class ProfileAdmin(ModelAdmin):
    list_display = ['name','shop','phone_no']
    search_fields = ['name','shop','phone_no']

admin.site.register(Profile,ProfileAdmin)

admin.site.register(Member_As)
admin.site.register(Kitchen_item_category)
admin.site.register(HouseHold_item_category)
admin.site.register(Special_Offer_item)
