# -*- coding: utf-8 -*-
import pandas as pd

def order_status(row, orders):
    if row.order_number in orders.keys():
        if row.status == "PENDING":
            orders[row.order_number] = row.status
        elif row.status == "SHIPPED":
            if orders[row.order_number] == "SHIPPED" or orders[row.order_number] == "CANCELLED":
                orders[row.order_number] = row.status
            elif orders[row.order_number] == "PENDING":
                orders[row.order_number] = "PENDING"
    else:
        orders[row.order_number] = row.status
    return orders

def main():
    df = pd.read_csv('datasets/data_customer_order_status.csv') 
    orders = {}
    df.apply(lambda x: order_status(x, orders), axis=1)
    results = pd.DataFrame(orders.items(), columns=['order_number', 'status'])
    print(results)
    
if __name__ == "__main__":
    main()