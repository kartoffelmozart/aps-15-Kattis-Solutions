n,T = map(int,input().split())
task_times = map(int,input().split())
for i,t in enumerate(task_times):
    T -= t
    if T < 0: 
        print(i)
        break
if T >= 0: print(n)