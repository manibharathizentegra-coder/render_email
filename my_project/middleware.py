class AllowIframeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Allow iframe from anywhere (or restrict to Zoho Creator)
        response.headers['X-Frame-Options'] = 'ALLOWALL'
        return response
