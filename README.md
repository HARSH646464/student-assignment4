# student-assignment4
```# File Reading in Python

This Python program demonstrates how to:

1. Open and read a text file named **sample.txt**  
2. Print its content line by line with line numbers  
3. Handle the error gracefully if the file does not exist  

---

## 📌 Code

```python
try:
    f = open('sample.txt', 'r')
    reading_file = f.readlines()
    print('Reading the file:')
    for file_no, line in enumerate(reading_file, start=1):
        print(f"Line{file_no}:{line.strip()}")
    f.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
```
```
