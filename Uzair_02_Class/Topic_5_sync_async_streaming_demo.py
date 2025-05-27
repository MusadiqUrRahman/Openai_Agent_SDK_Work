
# ========================================================
#    Synchronous vs Asynchronous vs Streaming in Python
# ========================================================

import time
import asyncio

# -------------------------------
# 1. Synchronous Example
# -------------------------------
def sync_task(name, seconds):
    print(f"🔹 [SYNC] Starting {name}")
    time.sleep(seconds)
    print(f"🔹 [SYNC] Finished {name} after {seconds} seconds")

def run_sync():
    print("\n--- Running Synchronous Tasks ---")
    start = time.time()
    sync_task("Task 1", 2)
    sync_task("Task 2", 2)
    sync_task("Task 3", 2)
    end = time.time()
    print(f"⏱ Total time (Sync): {end - start:.2f} seconds")


# -------------------------------
# 2. Asynchronous Example
# -------------------------------
async def async_task(name, seconds):
    print(f"🔸 [ASYNC] Starting {name}")
    await asyncio.sleep(seconds)
    print(f"🔸 [ASYNC] Finished {name} after {seconds} seconds")

async def run_async():
    print("\n--- Running Asynchronous Tasks ---")
    start = time.time()
    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 2),
        async_task("Task 3", 2),
    )
    end = time.time()
    print(f"⏱ Total time (Async): {end - start:.2f} seconds")


# -------------------------------
# 3. Streaming Example (Async Generator)
# -------------------------------
async def stream_task(name, count, delay):
    for i in range(1, count + 1):
        await asyncio.sleep(delay)
        yield f"🔁 [STREAM] {name} - part {i}/{count}"

async def run_streamed():
    print("\n--- Running Streamed Task ---")
    start = time.time()
    async for part in stream_task("Streamed Task", count=5, delay=1):
        print(part)
    end = time.time()
    print(f"⏱ Total time (Streamed): {end - start:.2f} seconds")


# -------------------------------
# Main Runner
# -------------------------------
if __name__ == "__main__":
    print("=======================================")
    print("     Sync vs Async vs Streaming Demo")
    print("=======================================")

    # Run synchronous example
    run_sync()

    # Run asynchronous and streaming examples
    asyncio.run(run_async())
    asyncio.run(run_streamed())
