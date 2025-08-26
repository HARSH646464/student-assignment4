try:
    f=open('sample.txt','r')
    reading_file=f.readlines()
    print('Reading the file:')
    for file_no,line in enumerate(reading_file,start=1):
         print(f"Line{file_no}:{line.strip()}")
    f.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
    
