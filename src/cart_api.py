from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(message='Hello, World!')


@app.route('/api/cart', methods=['GET'])
def get_cart_items():
    # user_id = request.args.get('user_id')
    # TODO Add logic to get cart items from your database
    cart_items = []  # Example data
    return jsonify({'cart_items': cart_items}), 200


# Adds items to shopping cart
@app.route('/api/cart/add', methods=['POST'])
def add_item_to_cart():
    # Logic to create a new item
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')

    # Here you would typically interact with your database to add the item
    # to the user's cart
    # For demonstration, we'll just return the data received
    response = {
        'item_id': item_id,
        'quantity': quantity,
        'message': 'Item added to cart successfully!'
    }

    # Validate and process the data
    # Save the item to the database or any other storage

    return jsonify(response, message='Item created successfully', ), 200


# Updates items in shopping cart
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Logic to update a specific item by ID
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')
    # TODO Add logic to update items from the database
    return jsonify({
        'message': 'Item quantity updated',
        'item_id': item_id,
        'quantity': quantity}), 200


# Deletes items from shopping cart
@app.route('/api/cart/remove', methods=['DELETE'])
def delete_item(item_id):
    # Logic to delete a specific item by ID from the
    # database or any other source
    data = request.get_json()
    item_id = data.get('item_id')
    # TODO Add logic to delete the item from the database
    return jsonify({
        'message': 'Item removed from cart',
        'item_id': item_id}), 200


if __name__ == '__main__':
    app.run(debug=True)
