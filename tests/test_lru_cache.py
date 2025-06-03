from algorithms.lru_cache.lru_cache import LRUCache


def test_lru_cache_evict() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) is None
    assert cache.get(2) == 2
