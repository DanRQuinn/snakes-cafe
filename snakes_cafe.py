
menu =   """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **    
***********************************"""

print(menu)


def order():
    orders = {}
    while True:
        order = input(">")
        if order == "quit":
            break
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
        print(f"\n** Thanks for ordering! {orders[order]} order(s) of {order} will be right up! **\n")
    print("Exiting")

if __name__ == "__main__":
    order()
