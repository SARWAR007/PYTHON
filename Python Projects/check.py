def replace_word(string_input,str_to_replace,assign_str):
    
    print(string_input)
    print(str_to_replace)
    print(assign_str)

    split_input = string_input.split()
    result_string = ''
    for value in string_input:
        print(value)

        if value == str_to_replace:

            value = assign_str

            print(value)
        
        result_string += value 
    return result_string.strip()
    


    
inp_str = input("Enter the string :")

replace_string = input("Enter the word you want to replace from the string :")



str_assign = input("Enter the value you want to assign instead of replace string :")

print(inp_str,replace_string,str_assign)

print(replace_word(inp_str,replace_string,str_assign))
