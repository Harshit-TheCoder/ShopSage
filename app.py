from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/process_payment', methods=['POST'])
def payment():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    payment_mode = request.form.get('payment_mode') 

    upi_app = request.form.get('upi')  # Only valid if UPI selected
    upi_id = request.form.get('upi-id')
    card_bank = request.form.get('bank')  # Only valid if Card selected
    card_number = request.form.get('card-number')
    cvv = request.form.get('cvv')
    expiry = request.form.get('expiry')

    print("User Info:", name, email, address)
    print("Payment Mode:", payment_mode)

    if payment_mode == "upi":
        print("UPI App Selected:", upi_app, upi_id)
    elif payment_mode == "card":
        print("Card Bank:", card_bank)
        print("Card Details:", card_number, cvv, expiry)


    return redirect('/')
@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)