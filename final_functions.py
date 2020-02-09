cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):
    # hier kommt dein Code hin
    print("Warenkorb gesamt: " + str(sum(l)))
    
list_sum(cart_prices)
       
       
def prices_list(name, price):
    # hier kommt dein Code hin, das "pass" kannst du durch deinen Code ersetzen
    prices = []
    for i in range(1,11):
        elem = '{} x {}: {}'.format(i, name, i*price)
        prices.append(elem)
    return prices

print(prices_list("Wunderkeks", 0.79))


shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    # hier kommt dein Code hin. 
    # Du darfst von innerhalb der Funktion direkt auf die Variable "shelf"
    # zugreifen, diese muss nicht als Parameter übergeben werden, da sie
    # schon außerhalb der Funktion existiert.
    for i, name in enumerate(shelf):
        if name == 'leer':
            shelf[i] = article
            break

add_shelf("Rubik's Cube")
print(shelf)
