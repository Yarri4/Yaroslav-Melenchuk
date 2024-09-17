# Дополнительное практическое задание по модулю*


grades = list_ = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = set = {'Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve'}

dlina_a = len(grades[0])
dlina_b = len(grades[1])
dlina_j = len(grades[2])
dlina_k = len(grades[3])
dlina_s = len(grades[4])

summa_a = sum(grades[0], 0)
summa_b = sum(grades[1], 0)
summa_j = sum(grades[2], 0)
summa_k = sum(grades[3], 0)
summa_s = sum(grades[4], 0)

Result_a = summa_a/dlina_a
Result_b = summa_b/dlina_b
Result_j = summa_j/dlina_j
Result_k = summa_k/dlina_k
Result_s = summa_s/dlina_s




Result = {}

Result.update (
    { 'Aaron':Result_a,
    'Bilbo':Result_b,
    'Johnny':Result_j,
    'Khendrik':Result_k,
    'Steve':Result_s
    }
    
)

print('Средний балл:', Result)