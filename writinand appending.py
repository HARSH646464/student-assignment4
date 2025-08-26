with open('output.txt','w') as file:
    text=input("Enter  text to write to the file:")
    file.write(text +'\n')
    print("Data successfully written to output.txt."+'\n')
with open('output.txt','a') as f:
    text1=input('Enter additional to append:')
    f.write(text1 +'\n')
    print("Data successfully apended."+'\n')
    #print('\n')
with open('output.txt','r') as file2:
    reading_file=file2.read()
    print('Final content of output.txt:'+'\n','\n'+reading_file)
