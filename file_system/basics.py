with open("my_file.txt") as file: #Reading our file 
    contents = file.read()
    print(contents)

with open("my_file.txt", mode = "w") as file: #Writing to our file
    file.write("\nNew text.") 

with open("my_file.txt", mode = "a") as file: #Appeding strings to our file
    file.write("\nNew text.") 