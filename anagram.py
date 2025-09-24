s1=input("enter string 1:")
s2=input("enter string 2:")
s1=s1.lower()
s2=s2.lower()
# if len(s1)==len(s2):
#     if sorted(s1)==sorted(s2):
#         print("anagram")
#     else:
#         print("not anagram")
# else:
#     print("not anagram")


if len(s1)==len(s2):
    for i in s1:
        if i not in s2:
            print("not anagram")
            break
    else:
        print("anagram")
else:
    print("not anagram")