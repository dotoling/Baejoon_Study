# 불가능 위치 판단을 할때 기존에 지나온 점들을 기록 , 행 , 열 체크 후에 대각선은 두 점의 x좌표끼리의 차이와 y좌표끼리의 차이가 같으면 대각선이다.
# 이는 기울기로 증명가능
# pypy3 로 제출시 백준 통과

board_size = int(input())
start_index = [0,0]  # init start pos
queens_position = [] # queens position now
output_result = 0
x_pos_mapping_list = [0 for index in range(0,board_size)]

def possible_check(input_list):
    for exist_queen in queens_position:
        if(abs(exist_queen[0]-input_list[0])==abs(exist_queen[1]-input_list[1])):
            return False
    return True

def DFS(input_index_list):
    global output_result
    for x_num in range(0,board_size):

        if(x_pos_mapping_list[x_num] == 0):
            if (possible_check([x_num, input_index_list[1]]) == True):
                queens_position.append([x_num, input_index_list[1]])
                if(len(queens_position) == board_size):
                    output_result += 1
                    queens_position.pop()
                    continue
                x_pos_mapping_list[x_num] = 1
                DFS([x_num,input_index_list[1]+1])
                x_pos_mapping_list[x_num] = 0
                queens_position.pop()

DFS(start_index)
print(output_result)