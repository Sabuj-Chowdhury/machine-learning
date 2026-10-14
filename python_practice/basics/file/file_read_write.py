# read file
# file = open('./text.txt',"r")
# content = file.read()
# print(content)
# # always need to close after reading or writing for preventing data leakage 
# file.close()
# print(file.closed)


# with keyword

# with open('./text.txt',"r") as file:
#     content = file.read()
#     print(content)
    
# print(file.closed)

# write in file(a new file)
# with open("./test_write.txt","w") as file:
#     file.write("Hello test file\n")
#     file.write("Playin with file write ,read and append")

# writing in a existing file(overwwrids the file )
# with open('./text.txt',"w") as file:
#     file.write("Writing via w mood, might overwride previous content with this")

# not overwriting just add new things with existing file
with open('./text.txt',"a") as file:
    file.write("\nnew string line added")
    
with open('./text.txt',"r") as file:
    content =file.read()
    print(content)