books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
good_books_list = []
sum_of_pages = 0
good_books = 0
for book in books:
    sum_of_pages += book["pages"]
    if book["rating"] >= 8:
        print (book["title"])
        good_books += 1
        good_books_list.append(book["title"])

print(good_books_list)
print("\n".join(good_books_list))
print(f'Gustav precetl {sum_of_pages} stran.')
print(f'Aspon 8 bodu dal Gustav {good_books} kniham.')