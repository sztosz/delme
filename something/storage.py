storage = {}


def put(key, value):
    storage[key] = value


def retrieve(key):
    return storage[key] if storage[key] else None
