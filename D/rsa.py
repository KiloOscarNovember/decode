def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
def rsa_decode():
    n= 1507174481318465466523128991270360113716039108832684797969162807571085936787014823053726763818939
    c= 53286690260644388097425675112080667172813335026633897835642198108382149310515357443327652099643
    p= 1109726393111220267897048234180020381849194524413
    q= 1358149621991924365919728441827592260914436698903
    e= 104547
    
    if p*q == n:
        f=(p-1)*(q-1)
        d=modinv(e, f)
        m=pow(c, d, n)
        return m
    else:
        print('Not properly factorised: \n n  = ' + str(n) + '\n p*q= ' + str(p*q))
    
m= str(rsa_decode())
print(m)

list_A="_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoded= ''.join([list_A[int(i)] for i in [m[i:i+2] for i in range(0,len(m),2)]])
print(decoded)
