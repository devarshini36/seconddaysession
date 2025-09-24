# k="devarshini"
# if k==k[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

k=input()
for i in range(len(k)//2):
    if k[i]!=k[len(k)-1-i]:
        print("not a palindrome")
        break
else:
    print("palindrome")
