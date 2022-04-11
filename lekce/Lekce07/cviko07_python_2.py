import re

with open ("lekce/Lekce07/rady.txt", encoding="utf-8") as input:
    rady = input.read()

reg_expr = re.compile("https{0,1}:\S+\.[a-zA-Z]+")
urls = reg_expr.findall(rady)
for url in urls:
    print(url)