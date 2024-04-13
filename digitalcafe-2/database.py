products = {
    100: {"name":"Americano","price":125},
    200: {"name":"Brewed Coffee","price":100},
    300: {"name":"Cappuccino","price":120},
    400: {"name":"Espresso","price":120}
}


def get_product(code):
    return products[code]

def get_products():
    product_list = []

    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)

    return product_list

users = {
    "chums@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Matthew",
                         "last_name":"Uy"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales"},
    "gihoe@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Gio",
                         "last_name":"Hernandez"},
    "vic@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Vic",
                       "last_name":"Reventar"},
    "joe@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Joe",
                       "last_name":"Ilagan"},
}

def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None


