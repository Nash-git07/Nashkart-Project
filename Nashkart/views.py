
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder


def home(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/home.html', context)


def books(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	books = Book.objects.all()
	context = {'books':books, 'cartItems':cartItems}
	return render(request, 'store/books.html', context)	


def stores(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	stor = Store.objects.all()
	context = {'stor':stor, 'cartItems':cartItems}
	return render(request, 'store/stores.html', context)	


def electronics(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	elect = Electronic.objects.all()
	context = {'elect':elect, 'cartItems':cartItems}
	return render(request, 'store/electronics.html', context)	


def fruits(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	frui = Fruit.objects.all()
	context = {'frui':frui, 'cartItems':cartItems}
	return render(request, 'store/fruits.html', context)	


def vegetables(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	veg = Vegetable.objects.all()
	context = {'veg':veg, 'cartItems':cartItems}
	return render(request, 'store/vegetables.html', context)	


def fashions(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	fash = Fashion.objects.all()
	context = {'fash':fash, 'cartItems':cartItems}
	return render(request, 'store/fashions.html', context)	

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)

	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id


	if total == order.get_cart_total:
		order.complete = True
	order.save()

	details.objects.create(
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['country'],
		total=total,
		name=data['form']['name'],
	    email=data['form']['email'],
		order=order,
		modeofpay=data['shipping']['mode']

	)
	


	return JsonResponse('Payment submitted..', safe=False)


