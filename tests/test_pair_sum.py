from algorithms.two_pointers.pair_sum import pair_sum


def test_pair_sum_found() -> None:
    assert pair_sum([1, 2, 3], 5) == (1, 2)


def test_pair_sum_none() -> None:
    assert pair_sum([1, 2], 10) is None
