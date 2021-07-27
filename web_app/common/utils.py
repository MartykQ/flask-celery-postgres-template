"""
Utility functions shared between different modules
"""

import json
import logging

import requests


def response_wrapper(request_function):
    """ Simple response decorator

    Parameters
    ----------
    request_function : function
        a request function

    Returns
    -------
    response
        A request response
    """

    def wrapper(*args, **kwargs):
        response = request_function(*args, **kwargs)
        logging.info(response)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            logging.warning("Http Error:", http_error)
        except requests.exceptions.ConnectionError as connection_error:
            logging.warning("Error Connecting:", connection_error)
        except requests.exceptions.Timeout as timeout_error:
            logging.warning("Timeout Error:", timeout_error)
        except requests.exceptions.RequestException as request_exception:
            logging.warning("OOps: Something Else", request_exception)
        return response

    return wrapper


@response_wrapper
def make_get_request(url, headers=None):
    """Wrapper for requests.get"""
    return requests.get(url, headers=headers)


@response_wrapper
def make_post_request(url, payload, headers=None):
    """Wrapper for requests.post"""
    return requests.post(url, data=json.dumps(payload), headers=headers)


@response_wrapper
def make_delete_request(url, headers):
    """Wrapper for requests.delete"""
    return requests.delete(url, headers=headers)
