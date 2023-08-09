"""
[X]brands
[x]categories
[x]customers
[x]order_items
[]orders
[]products
[]staffs
[]stocks
[X]store

"""

class Store:
    def __init__(self,store_id,store_name,phone,email,street,city,state,zip_code):
        self.store_id=store_id
        self.store_name=store_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
class Brands:
    def __init__(self,brand_id,brand_name):
        self.brand_id=brand_id
        self.brand_name=brand_name


class categories:
    def __init__(self,category_id,category_name ):
        self.category_id=category_id
        self.category_name=category_name

class custumers :
    def __init__(self,customers_id,first_name,last_name,phone,email,street,city,zip_code,state):
        self.customers_id=customers_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code

class order_items:
    def __init__(self,order_id,item_id,product_id,quantity,list_price,discount):
        self.order_id=order_id
        self.item_id=item_id
        self.product_id=product_id
        self.quantity=quantity
        self.list_price=list_price
        self.discount=discount

class order:
    def __init__(order_id,customers_id,order_status,order_date,requiered_date,shipped_date,store_id,staff_id):
        self.order_id=order_id
           self.customers_id=customers_id
           self.order_status=order_status
           self.order_date=order_date
              self.order_id=order_id
                 self.order_id=order_id
