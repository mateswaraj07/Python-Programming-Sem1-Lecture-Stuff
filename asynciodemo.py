import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to Asyncio")

asyncio.run(greet())