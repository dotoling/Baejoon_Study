N = int(input())
input_numbers = list(map(int, input().split()))
input_symbols_num = list(map(int, input().split()))
symbols = ['+', '-', '*', '/']
custom_symbols_record = []


# symbol string init
for symbol_index in range(0,4):
    for loop_symbol in range(0,input_symbols_num[symbol_index]):
        custom_symbols_record.append(symbols[symbol_index])

use_index = []
symbols_string = ""
output_list = []

def DFS():
    global symbols_string
    global output_list
    if(len(use_index)==N-1):
        output_list.append(symbols_string)
        return
    else:
        temp_list=[]
        for custom_index in range(0,N-1):
            if(custom_index in use_index):
                continue
            if((custom_symbols_record[custom_index] in temp_list) == False):
                temp_list.append(custom_symbols_record[custom_index])
                symbols_string += custom_symbols_record[custom_index]
                use_index.append(custom_index)
                DFS()
                symbols_string = symbols_string[:-1]
                use_index.pop()

def find_max_min(target_list):
    max_num = 0
    min_num = 0
    init_flag = True

    for output_string_one in target_list:
        temp_num = input_numbers[0]
        for char_index in range(0,len(output_string_one)):
            if(output_string_one[char_index] == '+'): temp_num+=input_numbers[char_index + 1]
            elif(output_string_one[char_index] == '-'): temp_num-=input_numbers[char_index + 1]
            elif(output_string_one[char_index] == '*'): temp_num= temp_num * input_numbers[char_index + 1]
            elif(output_string_one[char_index] == '/'): 
                temp_num= int(temp_num / input_numbers[char_index + 1])

        
        if(init_flag == True):
            max_num = temp_num
            min_num = temp_num
            init_flag = False
        else:
            if(temp_num > max_num):
                max_num = temp_num
            if(temp_num < min_num):
                min_num = temp_num
    
    return [max_num, min_num]


DFS()
result_list = find_max_min(output_list)
print(result_list[0])
print(result_list[1])





