from transposition import *
from common import *
list_A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_a=list_A.lower()
list_0="0123456789"
list_0_for_atbash="123456789"
morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
     	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',  '4': '....-',  
        '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', '9': '----.', 
        '.' : '.-.-.-', ',' : '--..--', ':' : '---...', '?' : '..--..',
        "'" : '.----.', '-' : '-....-', '/' : '-..-.', '@' : '.--.-.', '=' : '-...-',
        ' ' : '/'
        }

def decode_help():
    txt='''Decode method HELP:
        rot_a(c,k) : 1文字のみのRot. c:text, k:Rot num
        vig_a(c,k,type) : 1文字のみのVig. c:text, k:key, type:"d"ならdecode, その他encode
        rot(c,k) : Rot. c:text, k:Rot num
        vig_e(c,k), vig_d(c,k): Vig encode & decode. c:text, k:key
        vig_e_auto(c,k), vig_d_auto(c,k): Auto key Vig encode & decode. c:text, k:key
        rev(c) : Reverse
        kw(length) : 特定文字長のキーワードを返す
        atbash(c)
        playfair_a(c,mode,mx) :2文字のみのPlayfair. c:text, mode:"d"ならdecode, その他encode, mx:Matrixのサイズ。デフォルトは5だが6*6も同様に計算できる。
        playfair_e, playfair_d
        playfair_d6: 6*6matrixのplayfair
        adfgx_e, adfgx_d(text, table_keyword, transposition_keyword)
        adfgvx_e, adfgvx_d(text, table_keyword, transposition_keyword)
        morse_d, morse_e (text, bin_code=False, delimiter=" ") : bin_code == Trueの場合、-.の代わりに01を使用したMorse. 
        columnar_e, columnar_d (c,col) : colには順番のリストを入れる。キーワードからassign_digits(x)で生成できる
        affine_e(text, a, b): aは掛け算、bは足し算部分
        railfence_e, railfence_d(text, rails, offset=0)
        '''
    print(txt)

def adfgx_e(text, table_keyword, transposition_keyword):
    table = mixed_alphabet(table_keyword, True)
    letter_set="ADFGX"
    trimmed_text=text.replace(" ","").upper().replace("J","I")
    
    fractionated=""
    for s in trimmed_text:
        index=table.index(s)
        row_num=int(index/5)
        col_num=index %5
        fractionated+=letter_set[row_num]
        fractionated+=letter_set[col_num]
        
    return "".join(columnar_e(fractionated, assign_digits(transposition_keyword)))

def adfgx_d(text, table_keyword, transposition_keyword):
    fractionated = columnar_d(text, assign_digits(transposition_keyword))
    
    table = mixed_alphabet(table_keyword, True)
    letter_set="ADFGX"
    
    plain_text=""
    for i,s in enumerate(fractionated):
        if i %2 == 0:
            row_num=letter_set.index(s)
        else:
            col_num=letter_set.index(s)
            plain_text+=table[row_num*5 + col_num]
            
    return "".join(plain_text)

def adfgvx_e(text, table_keyword, transposition_keyword):
    table = mixed_alphanumeric(table_keyword)
    letter_set="ADFGVX"
    trimmed_text=text.replace(" ","").upper()
    
    fractionated=""
    for s in trimmed_text:
        index=table.index(s)
        row_num=int(index/6)
        col_num=index %6
        fractionated+=letter_set[row_num]
        fractionated+=letter_set[col_num]

    return "".join(columnar_e(fractionated, assign_digits(transposition_keyword)))

def adfgvx_d(text, table_keyword, transposition_keyword):
    fractionated = columnar_d(text, assign_digits(transposition_keyword))
    
    table = mixed_alphanumeric(table_keyword)
    letter_set="ADFGVX"
    
    plain_text=""
    for i,s in enumerate(fractionated):
        if i %2 == 0:
            row_num=letter_set.index(s)
        else:
            col_num=letter_set.index(s)
            plain_text+=table[row_num*6 + col_num]
            
    return "".join(plain_text)

def rot_a(c,k):
    if list_A.find(c) >=0:
        list= list_A
    elif list_a.find(c) >=0:
        list= list_a
    elif list_0.find(c) >=0:
        list= list_0
    else:
        return c 
    
    l = len(list)
    position = list.find(c)
    p= (position + k) % l
    return list[p]

def vig_a(c,k,type):
    t=list_A.find(k)
    if t<0:
        t=list_a.find(k)
    if t<0:
        t=list_0.find(k)
    if t<0:
        t=0
    if type=="d":
        t=-t
    return rot_a(c,t)

def rot(c,k):
    l=len(c)
    p=""
    for i in range(l):
        p+=rot_a(c[i],k)
    return p

def vig_e(c,k):
    l_c=len(c)
    l_k=len(k)
    p=""
    for i in range(l_c):
        s=k[i % l_k]
        p+=vig_a(c[i],s,"e")
    return p

def vig_d(c,k):
    l_c=len(c)
    l_k=len(k)
    p=""
    for i in range(l_c):
        s=k[i % l_k]
        p+=vig_a(c[i],s,"d")
    return p

def vig_e_auto(c,k):
    l_c=len(c)
    p=""
    for i in range(l_c):
        s=k[i]
        p+=vig_a(c[i],s,"e")
        k+=c[i]
    return p

def vig_d_auto(c,k):
    l_c=len(c)
    p=""
    for i in range(l_c):
        s=k[i]
        p+=vig_a(c[i],s,"d")
        k+=vig_a(c[i],s,"d")
    return p

def kw(length):
    import csv
    kw=open("kw.txt")
    list_all = []
    for row in csv.reader(kw):
        list_all.append(row[0])
    list=[w for w in list_all if len(w)==length]
    return(list)

def atbash(c):
    list_A_atbash =rev(list_A)
    list_a_atbash=list_A_atbash.lower()
    list_0_atbash=rev(list_0_for_atbash)
    tr_A=str.maketrans(list_A,list_A_atbash)
    tr_a=str.maketrans(list_a,list_a_atbash)
    tr_0=str.maketrans(list_0_for_atbash,list_0_atbash)
    return(c.translate(tr_A).translate(tr_a).translate(tr_0))

def playfair_a(c,mode,mx):
    if mode=="d":
        sft=-1
    else:
        sft=1
        
    if mx==6:
        key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    c=c.upper()
    t0=key.index(c[0])
    t1=key.index(c[1])
    t0_r=int(t0/mx)
    t0_c=t0 %mx
    t1_r=int(t1/mx)
    t1_c=t1 %mx
    if t0_r == t1_r and t0_c == t1_c:
        #同じ文字が連続したときの挙動はrumkinに合わせる。Nianticもそうしていたので・・
        s0=((t0_r+sft) %mx)*mx+((t0_c+sft) %mx)
        s1=((t1_r+sft) %mx)*mx+((t1_c+sft) %mx)        
    elif t0_r == t1_r:
        s0=t0_r*mx+((t0_c+sft) %mx)
        s1=t1_r*mx+((t1_c+sft) %mx)
    elif t0_c == t1_c:
        s0=((t0_r+sft) %mx)*mx + t0_c
        s1=((t1_r+sft) %mx)*mx + t1_c
    else:
        s0=t0_r*mx+t1_c
        s1=t1_r*mx+t0_c

    p=key[s0]+key[s1]
    return p
    
def playfair_e(c):
    c=c.upper()
    if len(c)%2 ==1:
        c+="X"
    p=""
    for i in range(0,len(c),2):
        p+=playfair_a(c[i:i+2],"e",5) 
    
    return p    

def playfair_d(c):
    c=c.upper()
    if len(c)%2 ==1:
        c+="X"
    p=""
    for i in range(0,len(c),2):
        p+=playfair_a(c[i:i+2],"d",5) 
    
    return p    

def playfair_e6(c):
    c=c.upper()
    if len(c)%2 ==1:
        c+="X"
    p=""
    for i in range(0,len(c),2):
        p+=playfair_a(c[i:i+2],"e",6) 
    
    return p   

def playfair_d6(c):
    c=c.upper()
    if len(c)%2 ==1:
        c+="X"
    p=""
    for i in range(0,len(c),2):
        p+=playfair_a(c[i:i+2],"d",6) 
    
    return p    

def morse_e(text, bin_code=False, delimiter = " "):
    text=text.upper()
    converted=""

    for s in text[:]:
        if s in morse_code:
            converted+=morse_code[s] + delimiter
        else:
            converted+=s + delimiter
    
    if bin_code:
        converted=replace_all(converted,{"-":"0", ".":"1"})
    
    return converted

def morse_d(text, bin_code=False, delimiter=" "):
    if bin_code:
        morse_code_inv = dict((replace_all(j,{"-":"0", ".":"1"}),i) for (i,j) in morse_code.items())
    else:
        morse_code_inv = dict((j,i) for (i,j) in morse_code.items())
    
    code_string = text.split(delimiter)
    converted=""
    for s in code_string:
        if s in morse_code_inv:
            converted+=morse_code_inv[s]
        elif len(s)>0:
            converted+="[" + s + "]"
    
    return converted        

def affine_e_a(text, a, b):
    if list_A.find(text) >=0:
        list= list_A
    elif list_a.find(text) >=0:
        list= list_a
    elif list_0.find(text) >=0:
        list= list_0
    else:
        return text 
    
    l = len(list)
    position = list.find(text)
    converted= (position*a + b) % l
    return "".join(list[converted])
    
def affine_e(text, a, b):
    l=len(text)
    converted=""
    for i in range(l):
        converted+=affine_e_a(text[i], a, b)
    return converted

# SECOM cipher
# http://users.telenet.be/d.rijmenants/en/secom.htm
# http://kryptografie.de/kryptografie/chiffre/secom.htm

def chain_addition(x):
    y=[0]*10
    for i in range(9):
        y[i]= (x[i]+x[i+1]) %10
    y[9]=(x[9]+y[0]) %10
    return y

def zero2ten(ls):
    return [10 if x==0 else int(x) for x in ls]
    
def ten2zero(ls):
    return [0 if x==10 else x for x in ls]

def make_key_digits(key):
    key=key.replace(" ","").upper()
    if len(key)<20:
        key=key*(int(20/len(key))+1)
    key_a=key[0:10]
    key_b=key[10:20]
    key_a_digits=ten2zero(assign_digits(key_a))
    key_b_digits=ten2zero(assign_digits(key_b))
    key_digits0=[(x+y) %10 for(x,y) in zip(key_a_digits, key_b_digits)]

    key_digits1=chain_addition(key_digits0)
    key_digits2=chain_addition(key_digits1)
    key_digits3=chain_addition(key_digits2)
    key_digits4=chain_addition(key_digits3)
    key_digits5=chain_addition(key_digits4)
    key_digits=key_digits1+key_digits2+key_digits3+key_digits4+key_digits5
    
    return key_b_digits, key_digits

def make_checkerboard(key_digits):
    checkerboard_numbers = ten2zero(assign_digits(zero2ten(key_digits)))
    
    checkerboard=[0]*40
    checkerboard_index=[0]*40
    row0="ES TO NI A"
    row1="BCDFGHJKLM"
    row2="PQRUVWXYZ*"
    row3="1234567890"
    offset1=int(checkerboard_numbers[2])-1
    offset2=int(checkerboard_numbers[5])-1
    offset3=int(checkerboard_numbers[8])-1
    
    for i in range(0,10):
        checkerboard[i]=row0[i]
        checkerboard_index[i]=str(checkerboard_numbers[i])
    for i in range(0,10):
        checkerboard[10+((i+offset1) %10)]=row1[i]
        checkerboard_index[10+i]=str(checkerboard_numbers[2])+str(checkerboard_numbers[i])
    for i in range(0,10):
        checkerboard[20+((i+offset2) %10)]=row2[i]
        checkerboard_index[20+i]=str(checkerboard_numbers[5])+str(checkerboard_numbers[i])
    for i in range(0,10):
        checkerboard[30+((i+offset3) %10)]=row3[i]
        checkerboard_index[30+i]=str(checkerboard_numbers[8])+str(checkerboard_numbers[i])
    
    return checkerboard_numbers, checkerboard, checkerboard_index

def make_key_trans(key_digits, key_b_digits, checkerboard_numbers):
    key_trans_pre = [(x+y) %10 for(x,y) in zip(key_b_digits, checkerboard_numbers)]
    key_trans=columnar_e(key_digits, assign_digits(zero2ten(key_trans_pre)))

    first_trans_len=0
    second_trans_len=0
    already_encountered=[]

    for i in range(1,50):
        if second_trans_len >9:
            break
        if not key_digits[-i] in already_encountered:
            if first_trans_len<10:
                first_trans_len+=key_digits[-i]
                already_encountered.append(key_digits[-i])
            else:
                second_trans_len+=key_digits[-i]
                already_encountered.append(key_digits[-i])
    
    first_trans_key=key_trans[0:first_trans_len]
    second_trans_key=key_trans[first_trans_len:first_trans_len+second_trans_len]
    return first_trans_key, second_trans_key

def secom_e(c,key):
    #Checkerboard & keyの設定
    c=c.replace(" ","*").upper()
    key_b_digits, key_digits = make_key_digits(key)
    checkerboard_numbers, checkerboard, checkerboard_index = make_checkerboard(key_digits[40:50]) 
    first_trans_key, second_trans_key = make_key_trans(key_digits, key_b_digits, checkerboard_numbers)

    #Chckerboard
    plain_numbers=""
    for s in c:
        ind=checkerboard.index(s)
        c_ind=checkerboard_index[ind]
        plain_numbers+=c_ind
    
    padding= "0" * (-len(plain_numbers) %5)
    plain_numbers+=padding
    
    #first columnar transosition
    numbers_trans1 = columnar_e(plain_numbers, assign_digits(zero2ten(first_trans_key)))
    
    #second disrupted columnar transposition
    numbers_trans2 = disrupted_columnar_e(numbers_trans1, assign_digits(zero2ten(second_trans_key)))

    return "".join(numbers_trans2)
    
def secom_d(c,key):
    #Checkerboard & keyの設定
    c=c.replace(" ","").upper()
    key_b_digits, key_digits = make_key_digits(key)
    checkerboard_numbers, checkerboard, checkerboard_index = make_checkerboard(key_digits[40:50]) 
    first_trans_key, second_trans_key = make_key_trans(key_digits, key_b_digits, checkerboard_numbers)

    #second disrupted columnar transposition
    numbers_trans1=disrupted_columnar_d(c, assign_digits(zero2ten(second_trans_key)))
    
    #first columnar transosition
    plain_numbers = columnar_d(numbers_trans1, assign_digits(zero2ten(first_trans_key)))

    #Chckerboard
    p=""
    k=""
    for i in range(len(plain_numbers)):
        k+=plain_numbers[i]
        if (int(k)!=checkerboard_numbers[2] and int(k)!=checkerboard_numbers[5] and int(k)!=checkerboard_numbers[8]):
            ind=checkerboard_index.index(k)
            p+=checkerboard[ind]
            k=""
        elif len(k)==2:
            ind=checkerboard_index.index(k)
            p+=checkerboard[ind]
            k=""

    return "".join(p)

# end of definition. Below are used for test.
if __name__ ==  '__main__':
#    print("")
#    print(adfgvx_e("attack at 1200 AM", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy"))
#    print(adfgvx_d("DGDDDAGDDGAFADDFDADVDVFAADVX", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy"))
#    decode_help()
#    print(morse_e("morse code", True))
#    print(morse_d("00 000 101 111 1 / 0101 000 011 1 ",True))
    print(affine_e("Affine cipher 0123",5,8))