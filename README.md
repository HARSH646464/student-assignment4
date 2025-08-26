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
```# File Write, Append, and Read Program in Python

This program demonstrates how to *write, **append, and **read* text from a file (output.txt) using Python's with open() statement.

## 📌 Code

```python
with open('output.txt', 'w') as file:
    text = input("Enter text to write to the file: ")
    file.write(text + '\n')
    print("Data successfully written to output.txt.\n")

with open('output.txt', 'a') as f:
    text1 = input('Enter additional text to append: ')
    f.write(text1 + '\n')
    print("Data successfully appended.\n")

with open('output.txt', 'r') as file2:
    reading_file = file2.read()
    print('Final content of output.txt:\n', '\n' + reading_file)
```
