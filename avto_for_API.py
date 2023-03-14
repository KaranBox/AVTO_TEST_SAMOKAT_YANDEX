import requests #импорт библиотеки

order = {                         #данные
    "firstName": "Каран",
    "lastName": "Сахни",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 962 380 50 61",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Ревьюер поставь зачет))))",
    "color": [
        "BLACK"
    ]
}
resp = requests.post("https://11c9f974-462d-4d95-8ae6-448c3042236f.serverhub.praktikum-services.ru/api/v1/orders", json=order)  #содание запроса post(URL менять до запуска старый на новый,так как сервер не всегла работает
print(resp)

print("Статус код : " + str(resp.status_code))
assert 201 == resp.status_code
if resp.status_code == 201: #Проверка на код ответа равен 201
    print("Заказ успешно создан")
else:
    print("Провал")

print(resp.status_code)
print(resp.json())
resp.endcoding = 'utf-8'

# Сохранение  заказа
track=resp.json()["track"]

def get_order_track():  #3 Запрос на получение заказа по номеру заказа

    return requests.get("https://11c9f974-462d-4d95-8ae6-448c3042236f.serverhub.praktikum-services.ru/v1/orders/track?t=") #получение запроса GET(URL менять до запуска старый на новый,так как сервер не всегла работает.
resp=get_order_track()
track=="track?t"

print("Статус код : " + str(resp.status_code))
#3. Проверка на код ответа равен 200

if resp.status_code == 200:
    print("Заказ по номеру трека")
else:
    print("Провал")
    print(resp.json())
assert resp.status_code==200

