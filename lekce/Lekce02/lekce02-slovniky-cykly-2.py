books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
# print(books[0]["sold"])

chosen_year = 2019
num_sold_books = 0

for book in books:
    if book["year"] == chosen_year: 
        num_sold_books += book["sold"]

print(f'Za rok {chosen_year} jsme prodali {num_sold_books} knih.') 