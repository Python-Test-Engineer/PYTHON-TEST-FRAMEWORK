import requests
import json

response = requests.get(
    "http://216.10.245.166/Library/GetBook.php",
    params={"AuthorName": "Rahul Shetty"},
)
# print(response.text)
# print(type(response.text))
dict_response = json.loads(response.text)
# print(dict_response[0]["isbn"])
print("FIRST BOOK", dict_response[0])
json_response = response.json()
# print(type(json_response))
# print(json_response[0]["isbn"])
# assert response.status_code == 200
# print(response.headers)
assert response.headers["Content-Type"] == "application/json;charset=UTF-8"
# Retrieve the book details with ISBN RGHCC
for actualBook in json_response:
    if actualBook["isbn"] == "A1b":
        print("ACTUAL BOOK", actualBook)
        break

expectedBook = {
    "book_name": "Postman Course",
    "isbn": "A1b'",
    "aisle": "1",
}
print("EXPECTED BOOK", expectedBook)
print("==================")
print(actualBook["book_name"], expectedBook["book_name"])
assert actualBook["book_name"] == expectedBook["book_name"]
