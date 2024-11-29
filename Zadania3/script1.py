def create_hollow_matrix(a, b):
    temp = []
    for y in range(b): # how many columns
        temp.append(0)
    c = []
    for x in range(a): # how many rows
        c.append(temp)
    return c

def matrix_rows(m):
    return len(m)

def matrix_columns(m):
    return len(m[0])

def show_matrix(m):
    for x in range(matrix_rows(m)): # for each row
        for y in range(matrix_columns(m)): #for each column
            print(m[x][y],end=" ")
        print("")

def multiply_add_list(l1,l2):
    out_sum = 0
    for i in range(len(l1)):
        out_sum = out_sum + l1[i]*l2[i]
    return out_sum

def multiply_matrix(m1,m2):
    if matrix_columns(m1) == matrix_rows(m2):
        d = matrix_columns(m1)
        c_rows = matrix_rows(m1)
        c_columns = matrix_columns(m2)
        c = create_hollow_matrix(c_rows, c_columns)
        for x in range(c_rows):
            for y in range(c_columns):
                for index in range(d):
                    c[x][y] = c[x][y] + m1[x][index]*m2[index][y]
    else:
        c = None
    return c

a = [[1,2,3], [4,5,6]] #2x3 a[a[0], a[1]]
b = [[1], [1], [1]] # 3x1 b[b[0], b[1], b[3]]

show_matrix(a)
print("")
show_matrix(b)
print("")
c = multiply_matrix(a,b)
show_matrix(c)
