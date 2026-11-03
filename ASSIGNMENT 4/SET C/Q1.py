
from flask import Flask
app = Flask(__name__)
@app.route('/product/<int:product_id>')
def product(product_id):
    return f"""
    <h2>Product Details</h2>
    <p>Product ID: {product_id}</p>
    <p>Product Name: Laptop</p>
    <p>Price: Rs. 50000</p>
    """
if __name__ == '__main__':
    app.run(debug=True)
