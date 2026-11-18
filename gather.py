
# Print results after gathering all

import asyncio

async def square(n):
    await asyncio.sleep(2)
    return n * n

async def main():
    results = await asyncio.gather(
        square(2),
        square(3),
        square(4)
    )

    print(results)

asyncio.run(main())
async def square(n) – Defines an asynchronous function.


"""
Explanation of the code:
await asyncio.sleep(2) – Waits for 2 seconds without blocking other coroutines.
return n*n – Returns the square of the number.
asyncio.gather() – Runs all three coroutines concurrently and collects their results.
await asyncio.gather() – Waits until all three tasks finish.
print(results) – Prints all results together.
asyncio.run(main()) – Executes the main asynchronous function.
"""