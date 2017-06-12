from datetime import datetime, timedelta
from functools import wraps
import requests


def time_duration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        return (end - start).seconds + (end-start).microseconds/1000000
    return wrapper


@time_duration
def get_nets(url):
    requests.get(url)


@time_duration
def get_net_by_id(url):
    requests.get(url)


@time_duration
def add_net(url, data):
    requests.post(url, data=data)


@time_duration
def net_enter(url, data):
    requests.post(url, data=data)


@time_duration
def net_error(url):
    requests.get(url)


@time_duration
def add_password(url, data):
    requests.post(url, data=data)


@time_duration
def offline(url, data):
    requests.post(url, data=data)


@time_duration
def get_countries(url):
    requests.get(url)


@time_duration
def get_country_by_id(url):
    requests.get(url)


@time_duration
def get_regions(url):
    requests.get(url)


@time_duration
def get_region_by_id(url):
    requests.get(url)


@time_duration
def delete_net_by_id(url):
    requests.delete(url)