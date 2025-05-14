a = [10,20,30,40,50,60]

b = [10,20,30,70,80,90]

result = [ digit for digit in b if digit in a]

print(result)

result_1 = [no for no in b if no not in a]

print(result)