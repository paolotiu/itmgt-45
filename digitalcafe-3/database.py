import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
order_management_db = myclient["order_management"]


def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list

def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code})

    return product



def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def create_order(order):
    orders_coll = order_management_db['orders']
    print("HELLO")
    print(orders_coll)
    orders_coll.insert_one(order)

def get_branch(branch_id):
    branches_coll = products_db['branches']
    branch = branches_coll.find_one({"branch_id":branch_id})
    return branch


def get_branches():
    branch_list = []

    branches_coll = products_db["branches"]

    for b in branches_coll.find({}):
        branch_list.append(b)

    return branch_list

def get_orders(username):
    orders_coll = order_management_db['orders']
    orders = []

    for o in orders_coll.find({"username":username}):
        orders.append(o)

    return orders
