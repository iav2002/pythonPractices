with open("/Users/ignacioalarconvarela/VsCode_Python/MiniPracticas/file_system/my_file.txt") as file: #Reading our file 
    contents = file.read()
    print(contents)

with open("/Users/ignacioalarconvarela/VsCode_Python/MiniPracticas/file_system/my_file.txt", mode = "w") as file: #Writing to our file
    file.write("\nNew text.") 

with open("/Users/ignacioalarconvarela/VsCode_Python/MiniPracticas/file_system/my_file.txt", mode = "a") as file: #Appeding strings to our file
    file.write("\nNew text.") 


    failure