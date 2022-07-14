import requests
import json


# 1
# Получение списка авторов
authors_list = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors").json()
print(authors_list)
# Получение конкретного автора по его id
authors_list = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/21").json()
print(authors_list)
# Добавить новую книгу
new_book = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books", "'id:' 200")
# Добавить нового пользователя
new_user = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors", "'id:' 613")
# Обновить данные для книги под номером 10
with open('book10.json') as json_read:
    data10 = json.load(json_read)
update_book_10 = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Books/10", data10)
# Удалить пользователя под номером 4
user4 = requests.delete("https://fakerestapi.azurewebsites.net/api/v1/Authors/4")
