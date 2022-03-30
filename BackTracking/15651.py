# FULL EDIT EXSITING 15649 CODE BECAUSE OF TIME COMPLEXITY ( OPTIMISE CODE FOR SPEED )
output_list = []
N, M = map(int,input().split())

def NM_Problem():
    if(len(output_list) == M):
        print(" ".join(map(str,output_list)))
        return
    for posible_num in range(1, N+1):
        output_list.append(posible_num)
        NM_Problem()
        output_list.pop()
    return
NM_Problem()

