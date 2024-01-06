
import os
    # Python File Open

# with open("text.txt", "w") as file:       its for new file 
#     file.write("Hello, this is the content of the file.")
# f = open("text.txt","r")
# print(f.read())
# f= open('E:\Python\File Handling\demofile.txt' , 'r')
# print(f.read())
# print("Jutt",f.read(10))


        # ReadLine method is used to read first 2 lines in file

# print(f.readline())

            # Python File Write


# f = open('E:\Python\File Handling\demofile.txt' , 'a') 

# f.write('/nHi am zaheer this line is added form by me Ok')

# f.close()

# f= open('E:\Python\File Handling\demofile.txt' , 'r')
# print(f.read())


        # Over write the content


# The 'w' is used to over write the DAta 
# The 'r' is used t0 only read the file.
# The 'a' is used to add data in the buttom side

f = open('E:\Python\File Handling\demofile.txt' , 'w')
f.write('this content is new added by me. okk')
f.close()

f = open('E:\Python\File Handling\demofile.txt' , 'r')
print(f.read())


# f = open('CreadedByPython' , 'x')
f = open('CreadedByPython' , 'w')
f.write('I am a Full Stack developer')
f.close()
f= open('CreadedByPython' , 'r')
print(f.read())

os.remove('CreadtedByPython')





if os.path.exists('CreatedByPython'):
    os.remove('CreatedByPython')
else : 
    print('The File dose Not Exist')    


