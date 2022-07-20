rows = int(input("enter number of rows:"))
columns=int(input("enter number of columns:"))

for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")

