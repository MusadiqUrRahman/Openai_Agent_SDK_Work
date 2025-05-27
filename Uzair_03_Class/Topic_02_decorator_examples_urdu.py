
# 🧠 Python Decorator Examples (اردو تبصرے کے ساتھ)

# 📌 Example 1: Basic Decorator

def log_decorator(func):
    def wrapper():
        print("User Logged In")  # اضافی پیغام
        func()  # اصل فنکشن
    return wrapper

@log_decorator
def say_hello():
    print("Hello!")

say_hello()


# 📌 Example 2: Decorator with Argument

def custom_message_decorator(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)  # ہم یہاں custom message دے رہے ہیں
            return func(*args, **kwargs)
        return wrapper
    return decorator

@custom_message_decorator("🎉 خوش آمدید صارف!")
def greet():
    print("Hello!")

greet()


# 📌 Example 3: مزاحیہ مثال

def perfume(func):
    def wrapper():
        print("Applying perfume 🌸")  # اضافی عمل
        func()  # اصل فنکشن
    return wrapper

@perfume
def enter_room():
    print("Entering the room 🚪")

enter_room()
