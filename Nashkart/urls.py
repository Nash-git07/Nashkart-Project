from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('books/',views.books, name="books"),
	path('stores/',views.stores, name="stores"),
	path('vegetables/',views.vegetables, name="vegetables"),
	path('fruits/',views.fruits, name="fruits"),
	path('electronics/',views.electronics, name="electronics"),
	path('fashions/',views.fashions, name="fashions"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]