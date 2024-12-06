import asyncio, time

print("Program started")

async def main():
    print(f'{time.ctime()} Hello')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Good Bye')
    
async def main1():
    print(f'{time.ctime()} Hello 1')
    await asyncio.sleep(10.0)
    print(f'{time.ctime()} Good Bye 1')

def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")

loop = asyncio.get_event_loop()
task = loop.create_task(main())
task1 = loop.create_task(main1())
loop.run_in_executor(None, blocking)

loop.run_until_complete(task)
loop.run_until_complete(task1)


pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

