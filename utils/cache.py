from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=3 * 60 * 60)

def get_cached_news(source: str, query: str, fetch_func):
    key = f'{source}:{query}'
    if key in cache:
        return cache[key]
    data = fetch_func(query)
    cache[key] = data
    return data