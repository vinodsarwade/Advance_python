
'''this below function will give you an error 
# # bcz you provided int object and it is not iterble for sum and len function.
'''
# def list_avg(sequence):
#     return sum(sequence)/len(sequence)

# list_avg(123)



'''for that we can use type_casting (it will show you , you have to give parameter of list type.)
#sequence is type of list and it will return  float '''

def list_avg1(sequence:list) -> float:
    return sum(sequence)/len(sequence)

print(list_avg1([2,3,4]))

