
import asyncio

async def download_file():
    print("Downloading file...")
    await asyncio.sleep(3)
    print("File downloaded")

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")

async def main():
    await asyncio.gather(
        download_file(),
        fetch_data()
    )

    print("All tasks completed")

asyncio.run(main())

"""
Explanation of the code:
async def download_file() – Defines an asynchronous function to simulate downloading a file.
await asyncio.sleep(3) – Simulates a 3-second delay for downloading without blocking other coroutines.
async def fetch_data() – Defines an asynchronous function to simulate fetching data.
await asyncio.sleep(2) – Simulates a 2-second delay for fetching data without blocking other coroutines.
asyncio.gather() – Runs both coroutines concurrently and waits for them to complete.
await asyncio.gather() – Waits until both tasks finish.
print("All tasks completed") – Prints a message after both tasks are completed.
asyncio.run(main()) – Executes the main asynchronous function.
"""