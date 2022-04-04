class Book:

    def __init__(self, name, pages, price):
        self.name = name
        self.pages = pages
        self.price = price
    
    def __str__(self):
        return f"Kniha s nazvem \"{self.name}\" ma {self.pages} stran a stoji {self.price} Kc."
         

    def discount(self, percentage_discount):
        self.price = self.price * ((100 - percentage_discount)/100)

prvni_kniha = Book("Zert", 256, 100)
print(prvni_kniha)
prvni_kniha.discount(30)
print(prvni_kniha)