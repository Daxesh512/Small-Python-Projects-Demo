columns = 5
for i in range(1,columns+1):
    print(" "*((columns+1)-i), end="")
    for j in range(1,i+1):
        print('*', end=" ")
    print("\r")

for k in range(columns,1,-1):
    print(" "*((columns+2)-k), end="")
    for m in range(k,1,-1):
        print('*', end=" ")
    print("\r")