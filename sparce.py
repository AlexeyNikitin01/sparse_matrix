# row_pointer = [0, 0, 2, 6, 8]
# cols = [0, 2, 0, 2, 3, 5, 3, 4,]
# values = [9, 2, 1, 3, 4, 6, 2, 3,]
""" [0 0 0 0 0 0],
    [9 0 2 0 0 0],
    [1 0 3 4 0 6],
    [0 0 0 2 3 0] """

rows_pointers = [0, ]
values = []
cols = []

matrix = [[1, 0, 0, 0, ],
          [0, 1, 2, 0, ],
          [0, 0, 3, 0, ],
          [0, 2, 1, 3, ], ]

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]:
            values.append(matrix[i][j])
            cols.append(j)
            count += 1
    rows_pointers.append(count)
# rows_pointers=[0, 1, 3, 4, 7] values=[1, 1, 2, 3, 2, 1, 3] cols=[0, 1, 2, 2, 1, 2, 3]

vector_b = [0, 2, 0, 3, ]

assert max(cols)+1 == len(vector_b)

result_vector = []
for i in range(len(rows_pointers)-1):
    segment_pointer = rows_pointers[i:i+2]
    row_pointer = segment_pointer[1] - segment_pointer[0]
    result = 0
    for j in range(row_pointer):
        segment_cols = cols[segment_pointer[0]:segment_pointer[1]]
        segment_values = values[segment_pointer[0]:segment_pointer[1]]
        value_vector = vector_b[segment_cols[j]]
        result += value_vector * segment_values[j]
    result_vector.append(result)

print(result_vector)
