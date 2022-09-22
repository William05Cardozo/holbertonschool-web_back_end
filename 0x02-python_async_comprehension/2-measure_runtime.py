#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel using
asyncio.gather.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine"""
    task = []
    start_time = time.time()
    for iterr in range(4):
        task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*task)
    end_time = time.time()
    return end_time - start_time
