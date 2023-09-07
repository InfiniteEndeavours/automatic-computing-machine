from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    # Called everytime an instance of class is created
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status = 200
        )
