
# 1. Napisac program realizujacy mnozenie macierzy (gdzie macierze sa reprezentowane przez listy)

def create_hollow_matrix(a, b):
    m_out = [[0 for col in range(b)] for row in range(a)]
    return m_out

def matrix_rows(m):
    return len(m)

def matrix_columns(m):
    return len(m[0])

def show_matrix(m):
    for x in range(matrix_rows(m)):     # for each row
        for y in range(matrix_columns(m)):  #for each column
            print(m[x][y], end=" ")
        print("")

def multiply_add_list(l1,l2):
    sum_out = 0
    for i in range(len(l1)):
        sum_out = sum_out + l1[i]*l2[i]
    return sum_out


def multiply_matrix(m1, m2):
    if matrix_columns(m1) == matrix_rows(m2):
        d = matrix_rows(m2)
        c_rows = matrix_rows(m1)
        c_columns = matrix_columns(m2)
        c = create_hollow_matrix(c_rows, c_columns)
        for x in range(c_rows): # 0 1 2
            for y in range(c_columns): # 0 1 2
                for index in range(d):
                    c[x][y] += m1[x][index] * m2[index][y]
    else:
        c = None
    return c


a = [[1,2,3], [3,2,1], [4,4,4]]
b = [[1,0,0], [0,2,0], [0,0,3]]

show_matrix(a)
print("")
show_matrix(b)
print("")
c = multiply_matrix(a,b)
print("")
show_matrix(c)
