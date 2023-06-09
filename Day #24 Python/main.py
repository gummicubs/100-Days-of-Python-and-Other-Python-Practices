#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
names = []
with open('./Input/Names/invited_names.txt') as f:
    for line in f.readlines():
        name = line.strip('\n')
        names.append(name)

print(names)


with open('./Input/Letters/starting_letter.txt') as letter:
    letter_body = letter.read()

    
for i in range(len(names)):
    personalized = letter_body.replace('[name]', names[i])
    with open(f'./Output\ReadyToSend/{names[i]}.txt', 'w') as g:
        g.write(personalized)
        print(f"{names[i]}'s letter is done.")
    