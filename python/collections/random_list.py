import random

length = int(input('Enter n\n'))
mix_number = int(input('Enter a\n'))
max_number = int(input('Enter b\n'))

result_list = random.sample(range(mix_number, max_number), length)

print(f'result list is: \n{result_list}')
