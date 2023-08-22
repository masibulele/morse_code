

#create morse code dictionary key value pair
def create_morse_code_dict():
    """create morse code key and value dictionary from text file"""
    with open('morse_code_key.txt', 'r') as infile:
        morse_list=[]
        for row in  infile:
            row=row.replace('\n','')
            morse_list.append(row)
        morse_dict={chars.split('=')[0].strip():chars.split('=')[-1].strip() for chars in morse_list }
        return morse_dict

def morse_code_generator(user_input):
    """Takes user input string and converts it to morse code"""
    converted_string=[]
    my_morse_dict= create_morse_code_dict()
    for char in user_input:
        if char.isspace():
            converted_string.append("    ")
        if char in my_morse_dict.keys():
            converted_string.append(my_morse_dict[char])
            converted_string.append(" ")
    return "".join(converted_string)





if __name__ == '__main__':
    #get user input
    while True:
        user_string = input("Please enter the characters or words you world like to convert to morse code: or 'q' to quit\n")
        if user_string == "q":
            break
        morse_code= morse_code_generator(user_string.upper())
        print('The conversion of english to morse code is as follows: \n')
        print(f'{user_string}: {morse_code}')