########################################
########################################
def show_menu():
    '''
    show menu
    '''
    print('\n')
    print('Menu')
    print('========================================')
    print('0 -> Show all items')
    print('1 -> Add item')
    print('2 -> Remove item')
    print('3 -> Show item in shopping cart')
    print('4 -> Check out')
    print('5 -> Cancel')
    print('========================================')
########################################
########################################
def show_all_items(all_items):
    '''
    show all items
    '''
    print('\n')
    print('All items:')
    print('========================================')
    for i, item in enumerate(all_items):
        print('{}. {} ------${}'.format(i, item[0], item[1]))
    print('========================================')
########################################
########################################
def show_cart(cart):
    '''
    show all items in shopping cart
    '''
    print('\n')
    print('Items in shopping cart:')
    print('========================================')
    for i, item in enumerate(cart):
        print('{}. {} ------${}'.format(i, item[0], item[1]))
    print('========================================')
########################################
########################################
def add_to_cart(cart, all_items):
    '''
    name: item name to be added
    price: item price
    cart: a list storing (name, price) tuples
    '''
    n = len(all_items)
    show_all_items(all_items)
    valid_num = False
    while not valid_num:
        try:
            item_num = int(input('Enter the item you want to add: '))
            if item_num not in range(n):
                print('Invalid input. Please enter the item number!')
                continue
            else:
                valid_num = True
                cart.append(all_items[item_num])
                print('Item {} added.'.format(item_num))
        except:
            print('Invalid input. Please enter the item number!')
########################################
########################################
def remove_from_cart(cart):
    '''
    cart: a list as shopping cart is input
    '''
    if len(cart) == 0:
        print('Your shopping cart is empty!')
        return False
    n = len(cart)
    show_cart(cart)
    valid_num = False
    while not valid_num:
        try:
            item_num = int(input('Enter the item you want to remove: '))
            if item_num not in range(n):
                print('Invalid input. Please enter the item number!')
                continue
            else:
                valid_num = True
                del cart[item_num]
                print('Item {} removed.'.format(item_num))
        except:
            print('Invalid input. Please enter the item number!')
########################################
########################################
def check_out(cart):
    '''
    check out current cart: return the total price in cart
    '''
    if len(cart) == 0:
        print('Your cart is empty!')
        return True
    print('Items in your shopping cart: ')
    show_cart(cart)
    print('Checking out...')
    print('========================================')
    total_price = 0
    for item in cart:
        total_price += item[1]
    print('Your total is: ${}'.format(total_price))
    print('Thanks for shopping with us.')

    is_y_or_n = False
    while not is_y_or_n:
        try:
            y_or_n = str(input('Do you want to continue shopping? y or n: '))
            if y_or_n == 'n':
                is_y_or_n = True
                return False
            elif y_or_n == 'y':
                is_y_or_n = True
                return True
            else:
                print('Invalid input. Please enter y or n!')
        except:
            print('Invalid input. Please enter y or n!')
    #print('See you next time')
    #keep_shopping = False
########################################
########################################
def cancel():
    print('Transation cancelled!')
    is_y_or_n = False
    while not is_y_or_n:
        try:
            y_or_n = str(input('Do you want to continue shopping? y or n: '))
            if y_or_n == 'n':
                is_y_or_n = True
                return False
            elif y_or_n == 'y':
                is_y_or_n = True
                return True
            else:
                print('Invalid input. Please enter y or n!')
        except:
            print('Invalid input. Please enter y or n!')
    #keep_shopping = False

########################################
########################################
from IPython.display import clear_output

def start_shopping():

    all_items = (('Chip', 3.98),
            ('Beer', 6.99),
            ('Soda', 5.98),
            ('Chicken wing',11.99),
            ('Beef',15.99),
            ('Chocolate',5.02),
            ('Juice',6.98),
            ('Wine',15.98))

    shopping_cart = []
    keep_shopping = True
    user_option = None

    while keep_shopping:

        show_menu()

        valid_option = False
        while not valid_option:
            try:
                user_option = int(input('Choose a option from menu: '))
                if user_option not in range(6):
                    print('Please enter a valid option!')
                    continue
                else:
                    valid_option = True

            except:
                print('Please enter a valid option!')

        if user_option == 0:
            clear_output()
            show_all_items(all_items)
        elif user_option == 1:
            clear_output()
            add_to_cart(shopping_cart, all_items)
        elif user_option == 2:
            clear_output()
            remove_from_cart(shopping_cart)
        elif user_option == 3:
            clear_output()
            show_cart(shopping_cart)
        elif user_option == 4:
            clear_output()
            keep_shopping = check_out(shopping_cart)
            shopping_cart = []
        elif user_option == 5:
            clear_output()
            keep_shopping = cancel()
            shopping_cart = []
        else:
            clear_output()
            continue
    print('See you next time!')

start_shopping()
