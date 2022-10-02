
def display_order(order,orderlist):
    
    orderlist.append(order)
    orderdic = {i:orderlist.count(i) for i in orderlist}
    for i in orderdic:
        print(f'*** {orderdic[i]} order of {i} have been added to your meal *** \n')