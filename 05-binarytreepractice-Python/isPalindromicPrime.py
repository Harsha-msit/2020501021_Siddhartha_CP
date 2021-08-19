def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def isPalindrome(n):
    c=0
    dn=n
    dn2=n
    r=0
    while(dn>0):
        c+=1
        dn=dn//10
    c-=1
    while(dn2>0):
        x=dn2%10
        r+=x*(10**c)
        c-=1
        dn2=dn2//10
    return(r==n)

def isPalindromicPrime(n):
    return (isPrime(n) and isPalindrome(n))

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")