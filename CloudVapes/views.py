from django.conf import settings
from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail
import json
from django.http import JsonResponse


# Првична страница која ги прикажува сите продукти
def index(request):
    products = Product.objects.all()  # земи сите производи од базата
    return render(request, 'index.html', {'products': products})


# Функција која ја користи за да испрати емаил за нарачката
def send_order_email(order_data):
    subject = f"Нова нарачка: {order_data['product_name']}"
    message = f"Име и презиме: {order_data['full_name']}\n"
    message += f"Телефон: {order_data['phone']}\n"
    message += f"Адреса: {order_data['address']}\n"
    message += f"Град: {order_data['city']}\n"
    message += f"Производ: {order_data['product_name']}\n"
    message += f"Цена: {order_data['product_price']}\n"

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Твојот email
            ['cloudvape790@gmail.com'],  # email на кого ќе се испрати
            fail_silently=False,
        )
    except Exception as e:
        return JsonResponse({'message': f'Грешка при испраќање на емаил: {str(e)}'}, status=500)


# Функција за обработка на нарачката и испраќање емаил
def submit_order(request):
    if request.method == 'POST':
        try:
            # Парсирање на податоците од JSON телото на барањето
            data = json.loads(request.body)

            # Извлекување на податоци
            order_data = {
                'full_name': data.get('full_name'),
                'phone': data.get('phone'),
                'address': data.get('address'),
                'city': data.get('city'),
                'product_name': data.get('product_name'),
                'product_price': data.get('product_price'),
            }

            # Испраќање на емаил за нарачката
            send_order_email(order_data)

            # Ако нарачката е успешно испратена, врати успесна порака
            return JsonResponse({'message': 'Нарачката е успешно испратена!'}, status=200)

        except Exception as e:
            return JsonResponse({'message': f'Грешка при обработка на нарачката: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': 'Методот не е поддржан'}, status=400)
