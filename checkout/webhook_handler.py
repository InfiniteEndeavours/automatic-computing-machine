from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    # Called everytime an instance of class is created
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        print(f'Unhandled Webhook Received: {event["type"]}')
        return HttpResponse(
            content=f'Unhandled Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent_succeeded webhook event """
        print(f'Payment Intent Succeeded Webhook Received: {event["type"]}')
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent_payment_failed webhook event """
        print(f'Payment Failed Webhook Received: {event["type"]}')
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
