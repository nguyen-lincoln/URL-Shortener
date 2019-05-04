from math import floor
import string

def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + ascii.lowercase + ascii.uppercase 
    r = num % b
    result = base[r];
    q = floor(num/b)
    
    while q:
        r = q % b
        q = floor(q/b)
        result = base[int(r)] + result
    return result