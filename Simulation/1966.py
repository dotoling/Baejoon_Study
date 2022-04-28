test_num = int(input())
test_cases = []
input_two_nums_list = []


for loop_num in range(0,test_num):
    input_two_nums_list.append(list(map(int, input().split(' '))))
    test_case = list(map(int, input().split(' ')))
    test_cases.append(test_case)

input_two_nums_index = 0
for test_case_list in test_cases:
    count = 1

    check_list = []
    for loop_check_list in range(0, len(test_case_list)):
        if(loop_check_list == input_two_nums_list[input_two_nums_index][1]):
            check_list.append(1)
        else:    
            check_list.append(0)
    while(True):
        if(len(test_case_list) == 0):
            break
        head_priority = test_case_list[0]
        check_flag = False
        for num in test_case_list:
            if(num > head_priority):
                test_case_list.pop(0)
                temp_data = check_list.pop(0)
                check_list.append(temp_data)
                test_case_list.append(head_priority)
                check_flag = True
                break
        if(check_flag == False):  # if head_priority is max_priority
            test_case_list.pop(0)
            if(check_list.pop(0) == 1):
                print(count)
            count+=1
    input_two_nums_index += 1