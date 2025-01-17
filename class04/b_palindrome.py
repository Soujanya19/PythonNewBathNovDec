"""

purpose: demonstration of Palindrome check
    palindrome strings
        dad
        mom

"""

test_string = input("Enter the string : ")
print("test_string : ", test_string)

# reverse string
reverse_string = test_string[::-1]
print("reverse_string : ", reverse_string)

print("test_string==reverse_string : ", test_string==reverse_string)

if test_string==reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string, "is not palindrome")
    ##/workspaces/PythonNewBathNovDec/class04/b_palindrome.py
    ## new program