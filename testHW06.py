def read_file(file_name):
    with open(file_name, 'r') as file:
        return [float(line.strip()) for line in file]

integers = read_file('file1.txt')
floats = read_file('file2.txt')

sum_integers = sum(integers)
sum_floats = sum(floats)
avg_integers = sum_integers / len(integers)
avg_floats = sum_floats / len(floats)

sum_corresponding = [i + f for i, f in zip(integers, floats)]

print(f'Sum of integers: {sum_integers}')
print(f'Sum of floating-point numbers: {sum_floats}')
print(f'Average of integers: {avg_integers}')
print(f'Average of floating-point numbers: {avg_floats}')
print(f'Sum of corresponding elements: {sum_corresponding}')