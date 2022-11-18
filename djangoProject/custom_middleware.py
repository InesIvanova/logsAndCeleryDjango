# Standard Library
import logging

# Local Library
import uuid
from threading import local


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        logging.info(f"Incoming request. Headers: {request.headers}. Method: {request.method}. Body: {request.body}")
        response = self.get_response(request)
        logging.info(f"Response. Status code: {response.status_code}. Data: {response.data}")
        return response




_locals = local()


class Correlation():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.META["X-Correlation-ID"] = str(uuid.uuid4())
        _locals.correlation_id = request.META["X-Correlation-ID"]
        response = self.get_response(request)
        return response


class CorrelationFilter(logging.Filter):

    def filter(self, record):
        if not hasattr(record, 'correlation_id'):
            record.correlation_id = ""
        if hasattr(_locals, 'correlation_id'):
            record.correlation_id = _locals.correlation_id
        return True