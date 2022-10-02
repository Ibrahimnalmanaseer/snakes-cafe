from logging.handlers import QueueListener

from order import display_order


introduction='''

***********************************************
***      Welcome to the Snake Cafe !        ***
***       Please see our menu below         ***
****                                       ****
****    To quit at any time,type 'quit'    ****
***********************************************
Appetizers
------------
Wings 
Cookies
Spring Rolls


Entrees
-----------
Salmon
Steak
Meat Tornado
A literal Garden


Desserts
-----------
Ice Cream 
Cake
Pie


Drinks
----------
Coffee
Tea
Unicorn Tears

********************************************
**       What would you like to Order ?   **
********************************************
'''
print (introduction)

close_order=False
order_list=[]
menu=['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
while close_order==False:

    customer_order=input('> ')
    if customer_order !='quit':
        
        if customer_order.title() in menu:
            display_order(customer_order,order_list)
            # order_list.append(customer_order)
            # order_dict = {i:order_list.count(i) for i in order_list}
            # for i in order_dict:
            #     print(f'*** {order_dict[i]} order of {i} have been added to your meal *** \n')
        else:
            print('Your order out of our menu !, Please try to order again')

    else:
        print ('your order have been canceled, Thank you for Visiting 😊')
        close_order=True
        


