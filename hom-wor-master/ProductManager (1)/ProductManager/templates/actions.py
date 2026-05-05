from models import Product

def delete_product_by_id(product_id):
    product = Product.get_or_none(Product.id == product_id)
    if product:
        name = product.name
        product.delete_instance()  # Видалення з SQL
        return name
    return None