from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import *

# Налаштування бази даних
db = SqliteDatabase('products.db')

class Product(Model):
    name = CharField()
    price = FloatField()

    class Meta:
        database = db

# Створення таблиці, якщо її немає
db.connect()
db.create_tables([Product])

app = Flask(__name__)
app.secret_key = '123'  # Ключ для flash-повідомлень

@app.route('/')
def index():
    # Отримуємо всі товари з бази для таблиці
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
    product = Product.get_or_none(Product.id == product_id)
    if product:
        name = product.name
        product.delete_instance()  # Видалення з SQL
        flash(f"Товар {name} видалено!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)