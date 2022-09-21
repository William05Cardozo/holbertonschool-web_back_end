#!/usr/bin/env python3
"""
Take the code from wait_n.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """call funtion task_wait_n"""
    lista: List[float] = []
    order_list: List[float] = []
    for i in range(n):
        lista.append(task_wait_random(max_delay))
    for x in asyncio.as_completed(lista):
        get_number = await x
        order_list.append(get_number)
    return order_list
