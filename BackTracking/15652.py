N,M = input().split()
N = int(N)
M = int(M)

input_list = list( making_int for making_int in range(1,N+1))
dfs_temp_list = []
start_index = 0

def DFS():
    global start_index
    if(len(dfs_temp_list) == M):
        print(" ".join(dfs_temp_list))
        return
    for start_index_temp in range(start_index, N):
        dfs_temp_list.append(str(start_index_temp+1))
        #print(dfs_temp_list)
        start_index = start_index_temp
        DFS()
        dfs_temp_list.pop()

DFS()