from flask import Flask, redirect
from flask import render_template
from flask import session, url_for
from flask import request
import database as db
import authentication
import logging


app = Flask(__name__)

# Set the secret key to some random bytes. 
# Keep this really secret!
app.secret_key = b's@g@d@c0ff33!'


logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))

    return render_template('productdetails.html', code=code, product=product)

@app.route('/branches')
def branches():
    return render_template('branches.html', page="Branches")

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error)

@app.route('/auth', methods = ['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    app.logger.info('%s', is_successful)
    if(is_successful):
        session["user"] = user
        return redirect('/')
    else:
        return redirect(url_for('login', error="invalid"))

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')


@app.route('/addtocart')
def addtocart():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    item=dict()
    # A click to add a product translates to a 
    # quantity of 1 for now

    item["qty"] = 1
    item["code"] = code
    item["name"] = product["name"]
    item["subtotal"] = product["price"]*item["qty"]

    if(session.get("cart") is None):
        session["cart"]={}

    cart = session["cart"]
    cart[code]=item
    session["cart"]=cart
    return redirect('/cart')

@app.route('/updatecart', methods=['POST'])
def updatecart():
    cart = session["cart"]

    codes = request.form.getlist("code")
    qty = request.form.getlist("qty")


    print(codes)
    print(qty)
    for i in range(len(codes)):
        code = codes[i]
        cart[code]["qty"] = int(qty[i])
        cart[code]["subtotal"] = cart[code]["qty"] * db.get_product(int(code))["price"]

    session["cart"] = cart

    print(session["cart"])
    return redirect('/cart')

@app.route('/removefromcart')
def removefromcart():
    code = request.args.get('code', '')
    cart = session["cart"]
    cart.pop(code,None)
    session["cart"] = cart
    return redirect('/cart')


@app.route('/cart')
def cart():
    return render_template('cart.html')
