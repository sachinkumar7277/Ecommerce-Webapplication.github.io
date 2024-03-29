from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cart_view/', views.cart, name='about'),
    path('update_item/', views.updateItem, name="update_item"),
    path('upload_product/<int:pk>', views.uploadproduct, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),
    path('register_shop', views.registershop, name="update_item"),
    path('checkout', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('payment/', views.payment, name='payment'),
    path('privacy/', views.privacy, name='privacy'),
    path('profile/', views.profileview, name='profile'),
    path('calander/', views.calander, name='profile'),
    path('myorder/', views.myorder, name='home'),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url='/grocery/profile')),
    path('registered_shop/edit/<int:pk>', views.Registered_shopUpdateView.as_view(success_url='/grocery/profile')),
    path('Myshop/<int:pk>', views.Myshop, name='product'),
    path('Myshop_profile_view/<int:pk>', views.Myshop_profile_view, name='product'),
    path('MyDashboard/<int:pk>', views.MyDashboard, name='product'),
    path('shippinfo/<int:pk>', views.shippinfo, name='product' ),
    path('help/', views.help, name='help'),
    path('product_shop_now/', views.productshopnow, name='product'),
    path('Register_shop_now/', views.registershopnow, name='product'),
    path('product/<int:pk>', views.product, name='product'),
    path('product2/', views.product2, name='product'),
    path('product/', views.product, name='product'),
    path('single/<int:pk>', views.single, name='product'),
    path('special_offer_single/<int:pk>', views.special_offeer_single, name='product'),
    path('homepg_single/<int:pk>', views.homepg_single, name='product'),
    path('single2/', views.single2, name='product'),
    path('terms/', views.terms, name='product'),
    path('search_item/',views.search, name = "search"),
    path('', RedirectView.as_view(url='home/')),

]
