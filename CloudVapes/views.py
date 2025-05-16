from django.conf import settings
from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail
import json
from django.http import JsonResponse

# Првична страница која ги прикажува сите продукти
def index(request):
    products = Product.objects.all()
    sorted_products = sorted(products, key=lambda x: x.quantity, reverse=True)

    # Испратете ги во шаблонот
    return render(request, 'index.html', {'products': sorted_products})


# Функција која ја користи за да испрати емаил за нарачката
def send_order_email(order_data):
    subject = f"Нова нарачка: {order_data['product_name']}"
    message = f"Име и презиме: {order_data['full_name']}\n"
    message += f"Телефон: {order_data['phone']}\n"
    message += f"Адреса: {order_data['address']}\n"
    message += f"Град: {order_data['city']}\n"
    message += f"Вејп: {order_data['product_name']}\n"
    message += f"Цена: {order_data['product_price']}\n"
    message += f"Количина: {order_data['kolicina']}\n"
    message += f"Вкус: {order_data['flavor']}\n"  # Додавање на вкусот

    try:
        # Испраќање на емаил до администраторот
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

            # Проверка дали сите потребни податоци се присутни
            required_fields = ['full_name', 'phone', 'address', 'city', 'product_name', 'product_price', 'flavor']  # Додавање на 'flavor'
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return JsonResponse({'message': f'Недостасуваат следниве податоци: {", ".join(missing_fields)}'},
                                    status=400)

            # Проверка дали цената е валиден број
            try:
                product_price = float(data.get('product_price'))
                if product_price <= 0:
                    return JsonResponse({'message': 'Цената на производот мора да биде поголема од 0'}, status=400)
            except ValueError:
                return JsonResponse({'message': 'Цената на производот мора да биде валиден број'}, status=400)

            # Испраќање на емаил за нарачката
            send_order_email(data)

            return JsonResponse({'message': 'Нарачката е успешно испратена!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Грешка во форматот на податоците!'}, status=400)



def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"Име: {name}\nЕ-маил: {email}\n\nПорака:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],  # треба да го додадеш во settings.py
        )

        return render(request, 'contact.html', {'message_sent': True})

    return render(request, 'contact.html')
