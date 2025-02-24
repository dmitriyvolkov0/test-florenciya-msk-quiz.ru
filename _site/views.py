from django.shortcuts import render


def index(request):
    data = {
        'title': 'Восстановить зубы по системе «Всё на 4-х имплантах» в Москве: этапы, стоимость, гарантии на импланты и протезы',
        'description': 'Сколько стоит несъёмное протезирование зубов на 4 имплантах в Москве. Рассчитайте стоимость лечения и получите в подарок: КТ-снимок, бесплатную консультацию имплантолога и бесплатные профосмотры после имплантации в течение 3-х лет',
        'phone': '+7 (495) 347-77-07',
        'phone_moderate': '+7 (900) 765-43-21',
        'address': {
            'city': 'г.&nbsp;Нижний Новгород',
            'street': 'ул. Белинского, д. 58/60, пом. 35'
        },
        'address_moderate': {
            'city': 'г.&nbsp;Нижний Новгород',
            'street': 'ул. Белинского, д. 58/60, пом. 35'
        },
        'work_time': 'Ежедневно 9:00-21:30',
        'is_moderate': False
    }

    return render(request, 'index.html', {'data': data})


def success(request):
    return render(request, 'success.html')


def not_found(request):
    return render(request, '404.html')