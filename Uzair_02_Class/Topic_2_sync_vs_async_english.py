
# ==================================================
#           Synchronous vs Asynchronous in Python
# ==================================================

import time
import asyncio

# -------------------------------
# Synchronous Code Example
# -------------------------------
def sync_task(name, seconds):
    print(f"Starting {name}")
    time.sleep(seconds)
    print(f"Finished {name} after {seconds} seconds")

def run_sync():
    print("🔹 Running Synchronous Tasks")
    start = time.time()
    sync_task("Task 1", 4)
    sync_task("Task 2", 6)
    sync_task("Task 3", 8)
    end = time.time()
    print(f"⏱ Total time (Sync): {end - start:.2f} seconds\n")


# -------------------------------
# Asynchronous Code Example
# -------------------------------
async def async_task(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name} after {seconds} seconds")

async def run_async():
    print("🔸 Running Asynchronous Tasks")
    start = time.time()
    await asyncio.gather(
        async_task("Task 1", 10),
        async_task("Task 2", 2),
        async_task("Task 3", 5),
    )
    end = time.time()
    print(f"⏱ Total time (Async): {end - start:.2f} seconds\n")


# -------------------------------
# Main Runner
# -------------------------------
if __name__ == "__main__":
    print("======================================")
    print("    Python Sync vs Async Comparison")
    print("======================================\n")

    # Run synchronous version
    run_sync()

    # Run asynchronous version
    asyncio.run(run_async())
