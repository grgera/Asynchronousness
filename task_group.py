import asyncio
import time

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 .. + 15 = 120 sec
async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))



if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f"Total time: {time.time() - start}")
