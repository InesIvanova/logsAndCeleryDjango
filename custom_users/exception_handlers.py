import logging

from django.core.exceptions import ObjectDoesNotExist
from django.urls import Resolver404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.http import JsonResponse
from requests import ConnectionError



def page_not_found_handler(request, exception):
    logging.error("Wrong URL requested")
    return JsonResponse({
        'status_code': 404,
        'error': 'The page was not found'
    })


def global_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if isinstance(exc, ObjectDoesNotExist):



        return JsonResponse({
            'status_code': 404,
            'error': 'The '
        })

    # checks if the raised exception is of the type you want to handle
    if isinstance(exc, ConnectionError):
        # defines custom response data
        err_data = {'MSG_HEADER': 'some custom error messaging'}

        # logs detail data from the exception being handled
        logging.error(f"Original error detail and callstack: {exc}")
        # returns a JsonResponse
        return JsonResponse(err_data, safe=False, status=503)

    # returns response as handled normally by the framework
    return response