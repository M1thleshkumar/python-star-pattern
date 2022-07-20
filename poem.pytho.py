print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are''')



rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))

print("triangle Star Pattern") 
for i in range(rows):
    for j in range(i+1):
        print('*', end = '  ')
    print()
rows = int(input("enter number of rows:"))
columns=int(input("enter number of columns:"))

for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")
