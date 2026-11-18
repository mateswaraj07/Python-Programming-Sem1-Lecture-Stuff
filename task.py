
# Create Task

import asyncio

async def main():
    task = asyncio.create_task(fn2())

    print("one")
    # await asyncio.sleep(1)

    await task
    # await fn2()

    print("four")

    await asyncio.sleep(3)
    print("five")

    await asyncio.sleep(1)

async def fn2():
    await asyncio.sleep(2)
    print("two")

asyncio.run(main())
