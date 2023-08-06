# Async IO(Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.)

import asyncio

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())


# Another way to schedule tasks concurrently is as follows:
# async def main():
#     L = await asyncio.gather(
#         my_async_function(),
#         my_async_function(),
#         my_async_function(),
#     )
#     print(L)