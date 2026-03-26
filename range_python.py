from positivr_or_negative import multiply


def lower_cases():
    for i in range(ord('a'),ord('z')+1):
        print('{:c}'.format(i),end='')

lower_cases() #calling / putting to use the function

print("\n \n")
print(multiply(50, 100))