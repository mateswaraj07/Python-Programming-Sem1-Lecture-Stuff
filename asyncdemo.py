
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to Python")

async def main():
    await asyncio.gather(greet(), greet())

asyncio.run(main())
