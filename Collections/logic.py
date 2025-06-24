# def pal(n):
#     s=str(n)
#     return s==s[::-1]

# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5 +1)):
#         if n%i==0:
#             return False
#     return True
# def pal_prime(n):
#     return pal == prime
# # print(pal_prime(int(input("Enter the number:"))))



#Program for prime and the Even

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5 +1)):
        if n%i==0:
            return False
    return True
def Even(n):
    return n%2==0
    
def even_prime(n):
    return prime(n) and Even(n)