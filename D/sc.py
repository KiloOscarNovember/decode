from fn import *

def rot_bf(c):
    print("ROT brute force")
    for i in range(26):
        print(str(i) + " : " + rot(c,i))
        
def start(c):
    print("len : " + str(len(c)))
    rot_bf(c)
    print("atbash : "+atbash(c))
    
def rout1(c):
    #HEXbash, DEC2ASCII
    return(deca_smart(hexbash(c)))
    
def rout2(c):
    #Morse encode, Bin2ASCII
    return hexa(bin_to_hex(morse_e(c,True,'')))