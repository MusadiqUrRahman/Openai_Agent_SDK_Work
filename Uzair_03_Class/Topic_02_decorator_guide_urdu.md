
# 🧠 Decorator in Python (اردو میں مکمل گائیڈ)

## 📌 تعریف:
**Decorator** Python میں ایک خاص فنکشن ہوتا ہے جو دوسرے فنکشنز کو **اضافی صلاحیت** دیتا ہے **بغیر اس کے اصل کوڈ کو بدلے**۔

---

## 🍰 روزمرہ کی مثالیں:

### 1. 🎂 کیک پر آئسنگ
- اصل فنکشن: کیک بنانا
- Decorator: آئسنگ جو کیک کو خوبصورت بناتی ہے

### 2. 🛂 VIP پروٹوکول
- اصل فنکشن: ایک عام مسافر
- Decorator: VIP سروس (جلدی بورڈنگ، سلامی، الگ لاوٴنج)

### 3. 👕 کپڑے پر استری
- فنکشن: قمیض پہننا
- Decorator: استری، تاکہ صاف اور چمکدار لگے

---

## 🔧 Python Example 1: Basic Decorator

```python
def log_decorator(func):
    def wrapper():
        print("User Logged In")
        func()
    return wrapper

@log_decorator
def say_hello():
    print("Hello!")

say_hello()
```

📤 Output:
```
User Logged In
Hello!
```

---

## 🎯 Python Example 2: Decorator with Arguments

```python
def custom_message_decorator(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@custom_message_decorator("🎉 خوش آمدید صارف!")
def greet():
    print("Hello!")

greet()
```

📤 Output:
```
🎉 خوش آمدید صارف!
Hello!
```

---

## 🤖 Chainlit Example:

```python
import chainlit as cl

def greet_user(greeting):
    def decorator(func):
        async def wrapper(message: cl.Message):
            await cl.Message(content=greeting).send()
            await func(message)
        return wrapper
    return decorator

@cl.on_message
@greet_user("👋 السلام علیکم! خوش آمدید")
async def main(message: cl.Message):
    await cl.Message(content=f"آپ نے فرمایا: {message.content}").send()
```

---

## 📌 خلاصہ:

| اصطلاح | مطلب |
|--------|-------|
| فنکشن | اصل کام (cake, message, output) |
| Decorator | اضافی عمل (icing, VIP, logging) |
| @decorator | Python کو بتاتا ہے کہ فنکشن decorated ہے |

---

## 😂 مزاحیہ مثال:

```python
def perfume(func):
    def wrapper():
        print("Applying perfume 🌸")
        func()
    return wrapper

@perfume
def enter_room():
    print("Entering the room 🚪")

enter_room()
```

📤 Output:
```
Applying perfume 🌸
Entering the room 🚪
```

---

## 🎁 یاد رکھیں:
> "Decorator ایک ایسا غلاف ہے جو فنکشن کو بہتر، محفوظ اور دلکش بناتا ہے — بغیر اسے بدلے۔"
