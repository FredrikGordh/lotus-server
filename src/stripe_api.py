import stripe
from flask import Blueprint, request, jsonify


stripe_api_blueprint = Blueprint('cart_api', __name__)


stripe.api_key = 'your_stripe_secret_key'


@stripe_api_blueprint.route(
        '/api/payments/stripe/create-intent', methods=['POST'])
def create_stripe_payment_intent():
    data = request.get_json()
    amount = data.get('amount')
    currency = data.get('currency')
    cart_id = data.get('cart_id')
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        metadata={'cart_id': cart_id}
    )
    return jsonify({'client_secret': intent.client_secret}), 200


@stripe_api_blueprint.route('/api/payments/stripe/confirm', methods=['POST'])
def confirm_stripe_payment():
    data = request.get_json()
    payment_intent_id = data.get('payment_intent_id')
    intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    if intent.status == 'succeeded':
        return jsonify({'message': 'Payment successful'}), 200
    else:
        return jsonify({'message': 'Payment failed'}), 400
