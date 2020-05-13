from datetime import datetime


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ProcessViewNoneMiddleware.process_request(request)
        # ProcessViewNoneMiddleware.process_exception(request, exception=None)
        # ProcessViewNoneMiddleware.process_template_response(request, response=None)
        # ProcessViewNoneMiddleware.process_response(request, response=None)
        return self.get_response(request)


class ProcessViewNoneMiddleware(BaseMiddleware):
    def process_request(request):
        print("1. function name: process_request")
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("2. function name: process_view")
        print('----- Middleware view %s' % view_func.__name__)
        return None

    def process_exception(request, exception):
        print("3. function name: process_exception")
        return None

    def process_template_response(request, response):
        print("4. function name: process_template_response")
        return None

    def process_response(request, response):
        print("5. function name: process_response")
        return None
