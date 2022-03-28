import copy as cp

def NM_Problem(output_list, cur_count , max_count):
    if(cur_count == max_count):
        print(" ".join(map(str,output_list)))
        return
    new_output_list = cp.deepcopy(output_list)
    for posible_num in total_possible_number:
        if((posible_num in output_list)==False):
            temp_list = cp.deepcopy(new_output_list)
            temp_list.append(posible_num)
            NM_Problem(temp_list,cur_count+1,max_count)

input_val_list = []
for input_val in input().split():
    input_val_list.append(int(input_val))

total_possible_number = list(range(1,input_val_list[0]+1))


NM_Problem([],0,input_val_list[1])



