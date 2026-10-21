def countFreq(n,k):
    freq=[0]*10
    while n!=0:
        last_digit=n%10
        freq[last_digit]+=1
        n//=10
    res=[]
    for i in freq:
        if i>k:
            res.append(i)
    return res

n=1346987139
print(countFreq(n,1))
# # Function to count digit frequencies greater than k
# def countFreq(n, k):
#     freq = [0] * 10
#     while n != 0:
#         last_digit = n % 10
#         freq[last_digit] += 1
#         n //= 10

#     res = []
#     for i in range(len(freq)):
#         if freq[i] > k:
#             res.append(i)
#     return res

# n = 1346987139
# k = 1
# result = countFreq(n, k)
# print("Digits with frequency >", k, ":", result)
