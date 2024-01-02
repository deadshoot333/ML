import numpy as np 

def Stataionary_Dist(A):
    steps=10**3
    A_n=A

    i=0
    while i<steps:
        A_n=np.matmul(A_n,A)
        i+=1
    return A_n[0]

def find_probabilty(seq,A,pi):
    start_state=seq[0]
    probability=pi[start_state]
    prev_state=start_state
    
    for i in range(1,len(seq)):
        curr_state=seq[i]
        probability*=A[prev_state][curr_state]
        prev_state=curr_state
    return probability
state={
        0:"B",
        1:"P",
        2:"H" 
       }
A=np.array([[0.2,0.6,0.2],[0.3,0.0,0.7],[0.5,0,0.5]])

n=int(input("Enter the number of steps = "))
start_state=int(input("Enter the start state = "))
print(state[start_state],"-->",end=" ")
prev_state=start_state

while n-1:
    curr_state=np.random.choice([0,1,2],p=A[prev_state])
    print(state[curr_state],"-->",end=" ")
    prev_state=curr_state
    n-=1

pi=Stataionary_Dist(A)
print(f"\nPI= {pi}")

seq=[]
seq_step=int(input("Enter number 0f equence steps = "))
for i in range(0,seq_step):
    x=int(input())
    seq.append(x)
result=find_probabilty(seq,A,pi)
print(f"Probabily of getting {seq} is = {result}")
print("END")