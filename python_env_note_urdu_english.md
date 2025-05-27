# Python Environment Commands - Quick Note (English + Urdu)

## 1. List All Python Executables in PATH

```powershell
$env:PATH -split ';' | Where-Object { $_ -ne '' } | ForEach-Object { Join-Path $_ 'python.exe' } | Where-Object { Test-Path $_ }
```

🔍 **English:** Lists all `python.exe` files found in directories defined in the system's `PATH` environment variable.  
Use this to see **all available Python installations** on your system.

🔍 **Urdu:** یہ کمانڈ سسٹم کے `PATH` میں شامل تمام فولڈرز میں موجود `python.exe` فائلز کی فہرست دیتی ہے۔  
اسے استعمال کر کے آپ دیکھ سکتے ہیں کہ آپ کے سسٹم پر کون کون سی Python انسٹالیشنز موجود ہیں۔

---

## 2. Show the Currently Active Python Executable

```powershell
python -c "import sys; print(sys.executable)"
```

🎯 **English:** Displays the exact path of the **currently active** Python interpreter being used when you type `python`.

🎯 **Urdu:** یہ کمانڈ وہ Python دکھاتی ہے جو اس وقت فعال ہے، یعنی جب آپ `python` لکھتے ہیں تو کون سی Python استعمال ہو رہی ہے۔

---

## Summary / خلاصہ

| Command / کمانڈ | Purpose (English) | مقصد (Urdu) |
|----------------|-------------------|----------------|
| List all python.exe | Shows all Python installations found in PATH | PATH میں موجود تمام Python انسٹالیشنز دکھاتا ہے |
| Current python | Shows which Python executable is currently being used | اس وقت کون سی Python ایکٹیو ہے، یہ دکھاتا ہے |