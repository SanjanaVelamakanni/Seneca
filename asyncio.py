import asyncio
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
async def main():
    task1 = asyncio.create_task(say_after(2, 'Hello'))
    task2 = asyncio.create_task(say_after(1, 'World'))
    await task1
    await task2
asyncio.run(main())




import asyncio
async def print_number(number):
    await asyncio.sleep(number)
    print(f"Number: {number}")
async def main():
    await asyncio.gather(
        print_number(3),
        print_number(1),
        print_number(2),
    )
asyncio.run(main())


import asyncio
async def countdown(name, seconds):
    while seconds:
        print(f"{name}: {seconds} seconds left")
        await asyncio.sleep(1)
        seconds -= 1
    print(f"{name}: Time's up!")
async def main():
    await asyncio.gather(
        countdown("Timer 1", 3),
        countdown("Timer 2", 5),
    )
asyncio.run(main())

