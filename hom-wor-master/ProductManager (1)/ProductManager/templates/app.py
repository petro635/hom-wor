from flask import Flask, render_template, request, redirect, url_for, flash
from models import Product, init_db
import actions  # Імпортуємо наш новий файл

app = Flask(__name__)
app.secret_key = '123'

init_db()

@app.route('/')
def index():
    products = Product.select()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    if name and price:
        Product.create(name=name, price=price)
        flash(f"Товар {name} додано!", "success")
    return redirect(url_for('index'))

@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    name = actions.delete_product_by_id(product_id)
    if name:
        flash(f"Товар {name} видалено!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)