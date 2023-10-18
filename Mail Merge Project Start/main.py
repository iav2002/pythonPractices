#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


with open("Mail Merge Project Start/Input/Names/invited_names.txt") as starts:
    base = starts.readlines() #separamos los nombres del archivo y los ponemos en un array
  

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read() 
    print(letter_content)
    for name in base:
        clean_name = name.strip()
        final = letter_content.replace(PLACEHOLDER, clean_name)
        with open (f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{final}", mode =  "w") as completed_letter:
            completed_letter.write(final)

        
