
# Sync vs Async in Python (Urdu Explanation)

## 🔹 Synchronous Code (ہم وقت یا "ایک ساتھ ایک کام")

**وضاحت:**
- Sync کوڈ ایک وقت میں صرف ایک کام کرتا ہے۔
- اگلا کام تب تک شروع نہیں ہوتا جب تک پہلا مکمل نہ ہو جائے۔
- اگر ہر کام کو 2 سیکنڈ لگتے ہیں، تو 3 کاموں میں 6 سیکنڈ لگیں گے۔

### 🧪 مثال:

```python
import time

def sync_task(name, seconds):
    print(f"{name} شروع")
    time.sleep(seconds)
    print(f"{name} مکمل - {seconds} سیکنڈ میں")

def run_sync():
    start = time.time()
    sync_task("Task 1", 2)
    sync_task("Task 2", 2)
    sync_task("Task 3", 2)
    end = time.time()
    print(f"\nکل وقت (Sync): {end - start:.2f} سیکنڈ")

run_sync()
```

### 🔸 نتیجہ:
```
Task 1 شروع
Task 1 مکمل - 2 سیکنڈ میں
Task 2 شروع
Task 2 مکمل - 2 سیکنڈ میں
Task 3 شروع
Task 3 مکمل - 2 سیکنڈ میں

کل وقت (Sync): 6.00 سیکنڈ
```

---

## 🔹 Asynchronous Code (غیر ہم وقت - بیک وقت کام)

**وضاحت:**
- Async کوڈ کئی کام بیک وقت "انتظار" کے دوران چلا سکتا ہے۔
- اگر سبھی کام I/O پر رکنے والے ہوں (جیسے نیند یا ویب ریکویسٹ)، تو ایک ساتھ چلا کر وقت بچایا جا سکتا ہے۔
- 3 کام، ہر ایک کو 2 سیکنڈ لگیں، تو سب ایک ساتھ مکمل ہوں گے = صرف 2 سیکنڈ!

### 🧪 مثال:

```python
import asyncio
import time

async def async_task(name, seconds):
    print(f"{name} شروع")
    await asyncio.sleep(seconds)
    print(f"{name} مکمل - {seconds} سیکنڈ میں")

async def run_async():
    start = time.time()
    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 2),
        async_task("Task 3", 2),
    )
    end = time.time()
    print(f"\nکل وقت (Async): {end - start:.2f} سیکنڈ")

asyncio.run(run_async())
```

### 🔸 نتیجہ:
```
Task 1 شروع
Task 2 شروع
Task 3 شروع
Task 1 مکمل - 2 سیکنڈ میں
Task 2 مکمل - 2 سیکنڈ میں
Task 3 مکمل - 2 سیکنڈ میں

کل وقت (Async): 2.00 سیکنڈ
```

---

## 🔍 فرق:

| پہلو            | Synchronous (ہم وقت)        | Asynchronous (غیر ہم وقت)       |
|------------------|------------------------------|----------------------------------|
| کام کرنے کا طریقہ | ایک وقت میں ایک کام           | کئی کام بیک وقت                  |
| کل وقت          | تمام کاموں کا مجموعہ         | صرف سب سے بڑے انتظار کا وقت     |
| کب استعمال کریں؟| آسان یا CPU والے کام         | نیٹ ورک / I/O / انتظار والے کام |
