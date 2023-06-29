from django.http import HttpResponseForbidden

class IPWhitelistMiddleware:
    ALLOWED_IP = '127.0.0.1'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the IP address of the requester
        requester_ip = request.META.get('REMOTE_ADDR')

        # Check if the IP matches the allowed IP
        if requester_ip != self.ALLOWED_IP:
            return HttpResponseForbidden('Access denied.')

        return self.get_response(request)
