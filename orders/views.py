from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductInBasket

def basket_adding(request):
    return_dict = dict()
    print('3asel')
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, is_active=True,
                                                           product_id=product_id, defaults={'nmb': nmb})

    if not created:
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return_dict["products_total_nmb"] = products_in_basket.count()
    return_dict["products"] = list()
    for item in products_in_basket:
        temp = dict()
        temp["product_image"] = str(item.product.productimage_set.all()[0])
        temp["product_id"] = item.product_id
        temp["product_name"] = item.product.name
        temp["product_nmb"] = item.nmb
        temp["product_cost"] = item.total_price
        return_dict["products"].append(temp)

    return JsonResponse(return_dict)

def basket(request):
    return render(request, 'orders/basket.html', locals())

def changing_nmb_basket(request):
    return_dict = {}
    print('yeah')
    session_key = request.session.session_key
    data = request.POST
    toggle = data.get("toggle")
    product_id = data.get("product_id")
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product, created = ProductInBasket.objects.get_or_create(session_key=session_key, is_active=True, product_id=product_id)
    if not created:
        if toggle=='more change':
            product.nmb += 1
            product.save(force_update=True)
        else:
            product.nmb -= 1
            product.save(force_update=True)
    return_dict['products'] = list()
    for item in products_in_basket:
        temp = {}
        temp['nmb'] = item.nmb
        temp['product_id']=item.product.id
        temp['product_total_cost']=item.total_price
        return_dict['products'].append(temp)
    return JsonResponse(return_dict)

def deleting_product(request):
    return_dict = dict()
    data = request.POST
    session_key = request.session.session_key
    product_id = data['product_id']
    print(product_id)
    product_in_basket = ProductInBasket.objects.get(session_key=session_key, id=product_id, is_active=True)
    print(product_in_basket)
    product_in_basket.is_active = False
    product_in_basket.save(force_update=True)
    print(product_in_basket)
    return JsonResponse(return_dict)