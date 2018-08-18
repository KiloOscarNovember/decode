from common import *
def deca(list):
    result = ""
    for i in list:
        if str(i).isdecimal():
            if 32 < int(i) <127:
                result+=chr(int(i))
            else:
                result += "("+str(i)+")"
        else:
            result+=str(i)
    return result

def deca_smart(text):
    import re
    list=re.findall(r"0[3-9][0-9]|[3-9][0-9]|1[0-2][0-9]",text)
    print('Separated as : ',end='')
    print(list)
    return deca(list)
    
def adec(list):
    result=[]
    for i in list:
        result.append(ord(i))
    return result
    
def dechex(list):
    result=[]
    for i in list:
        if str(i).isdecimal():
            result.append(hex(i).replace("0x",""))
        else:
            result.append("(" + i + ")")
    return result

def hexdec(list):
    result=[]
    for i in list:
            result.append(int(i,16))
    return result

def hex_to_ascii85(a):
    a=a+ "0"*(-len(a) %8) #8桁で区切れるようにゼロ埋めする
    b=[a[i*8:(i+1)*8] for i in range(int(len(a)/8))]
    c=[int(i,16) for i in b]
    d=[]
    for i in c:
        for k in range(5)[::-1]:
            d.append(int(i/(85**k)) %85)
    e=[chr(i+33) for i in d]
    return "".join(e)
    
def ascii85_to_hex(e):
    e=e+ "0"*(-len(e) %5) #5桁で区切れるようにゼロ埋めする
    d=[ord(i)-33 for i in e]
    c=[]
    for i in range(int(len(d)/5)):
        t=0
        for j in range(5):
            t+=d[i*5 +j]*(85**(4-j))
        c.append(t)
    b=[hex(i).replace("0x","") for i in c]
    return "".join(b)
    
def bin_to_hex(a):
    a=a+ "0"*(-len(a) %4) #4桁で区切れるようにゼロ埋めする
    b=[a[i*4:(i+1)*4] for i in range(int(len(a)/4))]
    c=[hex(int(i,2)).replace("0x","") for i in b]
    return "".join(c)
    
def hex_to_bin(c):
    b=[bin(int(i,16)).replace("0b","").zfill(4) for i in c]
    return "".join(b)

def hexa(c):
    return deca([int(i,16) for i in split_by_len(c,2)])

def uudecode(a, bin_output=False):
    b="".join([bin(ord(i)-32).replace("0b","").zfill(6) for i in a])
    length =len(b)
    pad = -length %24
    c=b.zfill(length + pad)
    d=[c[i*8:(i+1)*8] for i in range(int(len(c)/8))]
    e=[chr(int(i,2)) for i in d]
    if bin_output:
        return c
    else:
        return "".join(e)
    
#print(dechex(["a",100,97,65,66,51,300]))        
#print(hexdec(['v', '0x64', '0x61', '0x41', '0x42', '0x33', '0x12c']))
#print(adec(" ^+.(+@_@$~*~@~(~&@*!($+@%^+@^@(~(#($+#_~!"))
#print(hex_to_ascii85("b220077beffddcaa52a2aff6fff138808738678ff0f400a1"))
#aaa = """o>O(N"("_m{leL({"{BoLlO_GlLN_LcLlL[j9%_>uL(#>_>G>.g'["ooJLlLo.^LL'_'D-l9Lf{_o'"""
#aaa="fg!edi0afenVnbt00vehtwt!ziXarg3rzert"
#print(len(aaa))
#print(aaa)
#print(ascii85_to_hex(aaa))
#print(bin_to_hex("01011110101101000110101"))
#print(hex_to_bin("5eb46a"))
#c ="be077423c921606c05c88"
#print(hex_to_ascii85(c))
#print(deca_smart('758184525566898279785057557278'))