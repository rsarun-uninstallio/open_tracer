"""
author: arun.rs
26th September 2018
"""
from datetime import datetime
from requests import request
from trace import trace_resource

def service(type, url, **kwargs):
    """
    :summary: Wrapper method that traces all the HTTP requests made
    :param type: Service type
    :param url: URL to connect to
    :param kwargs: Key word arguments
    :return: Response
    """
    if not 'headers' in kwargs:
        headers = {}
    #headers['trace_id'], headers['parent_id'], headers['child_id'] =
    status = True
    start_time = datetime.now()
    try:
        return request(type, url, **kwargs)
    except Exception as e:
        status = False
        raise
    finally:
        end_time = datetime.now()
        trace_resource(type, url, start_time, end_time, status)
