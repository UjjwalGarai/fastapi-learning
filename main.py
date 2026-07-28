import asyncio
import time

def sync_task(task_id:int):
    print(f"Sync Task {task_id} Start")
    time.sleep(2)
    print(f"Sync Task {task_id} Completed")

sync_task(1)
sync_task(2)


async def async_task(task_id:int):
    print(f"Async Task {task_id} Start")
    await asyncio.sleep(2)
    print(f"Async Task {task_id} Completed")


async def main():
    await asyncio.gather(
        async_task(1),
        async_task(2)
    )
    
asyncio.run(main())
