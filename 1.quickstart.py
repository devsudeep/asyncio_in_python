import asyncio, time

print("Program started")

async def main():
    print(f'{time.ctime()} Hello')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Good Bye')
    
asyncio.run(main())
print("Program completed")
