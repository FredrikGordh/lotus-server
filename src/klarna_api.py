import requests
from flask import Blueprint, request, jsonify


klarna_api_blueprint = Blueprint('cart_api', __name__)


KLARNA_API_URL = 'https://api.playground.klarna.com'
KLARNA_AUTH = ('your_username', 'your_password')


@klarna_api_blueprint.route(
        '/api/payments/klarna/create-order', methods=['POST'])
def create_klarna_order():
    data = request.get_json()
    order_amount = data.get('order_amount')
    order_lines = data.get('order_lines')
    response = requests.post(
        f'{KLARNA_API_URL}/checkout/v3/orders', auth=KLARNA_AUTH, json={
            'purchase_country': 'US',
            'purchase_currency': 'USD',
            'order_amount': order_amount,
            'order_tax_amount': 0,
            'order_lines': order_lines
        })
    return jsonify(response.json()), response.status_code


@klarna_api_blueprint.route('/api/payments/klarna/callback', methods=['POST'])
def klarna_callback():
    # data = request.get_json()
    # Handle Klarna callback data
    return jsonify({'message': 'Callback received'}), 200
