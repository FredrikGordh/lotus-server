from flask import Blueprint, request, jsonify

checkout_api_blueprint = Blueprint('cart_api', __name__)


@checkout_api_blueprint.route('/api/checkout/initiate', methods=['POST'])
def initiate_checkout():
    data = request.get_json()
    cart_id = data.get('cart_id')
    user_id = data.get('user_id')
    # TODO Add logic to initiate checkout
    return jsonify({
        'message': 'Checkout initiated',
        'cart_id': cart_id, 'user_id': user_id}), 200


@checkout_api_blueprint.route('/api/checkout/apply-discount', methods=['POST'])
def apply_discount():
    data = request.get_json()
    discount_code = data.get('discount_code')
    # TODO Add logic to apply discount code
    return jsonify({
        'message': 'Discount applied',
        'discount_code': discount_code}), 200
