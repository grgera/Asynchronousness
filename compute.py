import asyncio

async def compute(a, b):
    print("Compute...")
    await asyncio.sleep(3)
    return a + b

async def print_sum(a, b):
    result = await compute(a, b)
    print(f'{a} + {b} = {result}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))