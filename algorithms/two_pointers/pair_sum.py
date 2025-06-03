"""Pair sum finder using a two-pointer technique."""
from __future__ import annotations

from typing import Iterable, Tuple


def pair_sum(nums: Iterable[int], target: int) -> Tuple[int, int] | None:
    """Return indices of two numbers adding up to ``target`` or ``None``."""
    seen: dict[int, int] = {}
    for idx, num in enumerate(nums):
        other = target - num
        if other in seen:
            return seen[other], idx
        seen[num] = idx
    return None
