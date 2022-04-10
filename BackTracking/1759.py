int_data = list(map(int, input().split()))
string_data = input().split()
string_data.sort()
mo_count = 1
ja_count = 2
start_index = 0

string_temp_list = []
mo_table_list = ['a', 'i', 'e', 'u', 'o']

def DFS():
    global mo_count, ja_count, start_index
    if(len(string_temp_list) == int_data[0] and mo_count<=0 and ja_count<=0):
        if("".join(string_temp_list) == 'cstw'):
            print(mo_count)
        print("".join(string_temp_list))
        return

    temp_check = mo_count + ja_count
    if(mo_count > 0 and ja_count > 0):
        temp_check = mo_count + ja_count
    elif(mo_count > 0):
        temp_check = mo_count
    elif(ja_count > 0):
        temp_check = ja_count
    '''
    if(len(string_data) - start_index - 1 < temp_check):
        return # 불가능 판단 
    '''

    for temp_start_index in range(start_index, int_data[1]):
        if(string_data[temp_start_index] in mo_table_list):
            mo_count -= 1
        else:
            ja_count -= 1
        string_temp_list.append(string_data[temp_start_index])
        start_index = temp_start_index + 1
        DFS()
        start_index = temp_start_index
        string_temp_list.pop()
        if(string_data[temp_start_index] in mo_table_list):
            mo_count += 1
        else:
            ja_count += 1
DFS()