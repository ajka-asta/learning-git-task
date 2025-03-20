print("Zadanie 1")
print("Lista zakupów")
shopping_dict = {
    "piekarnia" : ["chleb", "bułki", "pączek", "precel"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for shop, products in shopping_dict.items():
    products = [product.capitalize () for product in products]
    print(f"Idę do {shop.capitalize()} i kupuję tam: {products}.")
total = sum(len(products) for products in shopping_dict.values())
print("W sumie kupuję", total, "produktów.")
print()
print("brak pomysłu na commit")
print("drugi commit")
print("zrobimy jeszcze jeden commit")
print("Specjalne pozdrowienia dla Patryka!")
