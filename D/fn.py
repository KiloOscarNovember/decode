from transposition import *
from common import *
from code_tables import *
from base_conversion import *

def decode_help():
    txt='''Decode method HELP:
        rot_a(c,k) : 1文字のみのRot. c:text, k:Rot num
        vig_a(c,k,type) : 1文字のみのVig. c:text, k:key, type:"d"ならdecode, その他encode
        rot(c,k) : Rot. c:text, k:Rot num
        vig_e(c,k), vig_d(c,k), beaufort(c,k): Vig encode & decode, Beaufort. c:text, k:key
        vig_e_auto(c,k), vig_d_auto(c,k): Auto key Vig encode & decode. c:text, k:key
        rev(c) : Reverse
        kw(lregexp) : 正規表現にマッチする
        atbash(c)
        playfair_a(c,mode,mx) :2文字のみのPlayfair. c:text, mode:"d"ならdecode, その他encode, mx:Matrixのサイズ。デフォルトは5だが6*6も同様に計算できる。
        playfair_e, playfair_d(text, table_keyword="")
        playfair_d6: 6*6matrixのplayfair
        adfgx_e, adfgx_d(text, table_keyword, transposition_keyword)
        adfgvx_e, adfgvx_d(text, table_keyword, transposition_keyword)
        morse_d, morse_e (text, bin_code=False, delimiter=" ") : bin_code == Trueの場合、-.の代わりに01を使用したMorse. 
        bacon1_d, bacon1_e, bacon2_d, bacon2_e : Bacon cipher. 入力の仕方はmorseと同じ。Bacon1はIとJ, UとVを同一視する。Bacon2はいずれも別々に処理。 
        columnar_e, columnar_d (c,col) : colには順番のリストを入れる。キーワードからassign_digits(x)で生成できる
        affine_e(text, a, b): aは掛け算、bは足し算部分
        railfence_e, railfence_d(text, rails, offset=0)
        bifid_e, bifid_d(text, table_keyword="")
        abc012(text)
        hexbash(c)
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

def rot_a(c, k, type="encode"):
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

    if type == "encode":
        p= (position + k) % l
    elif type == "decode":
        p= (position - k) % l
    elif type == "beaufort":
        p= (k - position) % l
    else:
        p= c
    return list[p]

def vig_a(c,k,type):
    t=list_A.find(k)
    if t<0:
        t=list_a.find(k)
    if t<0:
        t=list_0.find(k)
    if t<0:
        t=0
    return rot_a(c,t, type)

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
        p+=vig_a(c[i],s,"encode")
    return p

def vig_d(c,k):
    l_c=len(c)
    l_k=len(k)
    p=""
    for i in range(l_c):
        s=k[i % l_k]
        p+=vig_a(c[i],s,"decode")
    return p

def beaufort(c,k):
    l_c=len(c)
    l_k=len(k)
    p=""
    for i in range(l_c):
        s=k[i % l_k]
        p+=vig_a(c[i],s,"beaufort")
    return p

def vig_e_auto(c,k):
    l_c=len(c)
    p=""
    for i in range(l_c):
        s=k[i]
        p+=vig_a(c[i],s,"encode")
        k+=c[i]
    return p

def vig_d_auto(c,k):
    l_c=len(c)
    p=""
    for i in range(l_c):
        s=k[i]
        p+=vig_a(c[i],s,"decode")
        k+=vig_a(c[i],s,"decode")
    return p

def kw(regexp):
    import csv
    import re
    kw=open("kw.txt")
    list_all = []
    for row in csv.reader(kw):
        list_all.append(row[0])
    list=[w for w in list_all if re.match(regexp, w)]
    return(list)

def atbash(c):
    list_A_atbash =rev(list_A)
    list_a_atbash=list_A_atbash.lower()
    list_0_atbash=rev(list_0_for_atbash)
    tr_A=str.maketrans(list_A,list_A_atbash)
    tr_a=str.maketrans(list_a,list_a_atbash)
    tr_0=str.maketrans(list_0_for_atbash,list_0_atbash)
    return(c.translate(tr_A).translate(tr_a).translate(tr_0))

def hexbash(c):
    c=c.lower()
    list_hex_atbash =rev(list_hex)
    tr_hex=str.maketrans(list_hex,list_hex_atbash)
    return(c.translate(tr_hex))

def playfair_a(c,mode,mx):
    if mode=="d":
        sft=-1
    else:
        sft=1
        
    if mx==6:
        key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        key = polybius_table
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
    c=c.upper().replace("J","I")
    if len(c)%2 ==1:
        c+="X"
    p=""
    for i in range(0,len(c),2):
        p+=playfair_a(c[i:i+2],"e",5) 
    
    return p    

def playfair_d(c):
    c=c.upper().replace("J","I")
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
    
def polybius_e(text, table_keyword=""):
    table = mixed_alphabet(table_keyword, True)
    text=text.upper().replace("J","I")
    coordinates=[]
    for i in range(len(text)):
        index = table.index(text[i])
        coordinates.append(str(int(index/5)+1))
        coordinates.append(str((index %5)+1))
    return "".join(coordinates)
    
def polybius_d(text, table_keyword=""):
    table = mixed_alphabet(table_keyword, True)
    remain=""
    if len(text) %2 ==1:
        remain = "[" + text[-1] +"]"
        text=text[0:-1]
    result = [table[(int(text[i])-1)*5 + (int(text[i+1])-1)] for i in range(0,len(text),2)]
    return "".join(result)+ remain

def bifid_e(text, table_keyword=""):
    table = mixed_alphabet(table_keyword, True)
    text=text.upper().replace("J","I")
    coordinates=[[0,0] for i in range(len(text))]
    for i in range(len(text)):
        index = table.index(text[i])
        coordinates[i]=[int(index/5), index %5]
    
    transposed_coordinates = [0]*len(text)*2
    for i in range(len(text)):
        transposed_coordinates[i]=coordinates[i][0]
        transposed_coordinates[i+len(text)]=coordinates[i][1]
    
    result = ""
    for i in range(len(text)):
        result += table[transposed_coordinates[2*i]*5+transposed_coordinates[2*i+1]]
    
    return result

def bifid_d(text, table_keyword=""):
    table = mixed_alphabet(table_keyword, True)
    text=text.upper().replace("J","I")
    
    transposed_coordinates = [0]*len(text)*2
    for i in range(len(text)):
        index = table.index(text[i])
        transposed_coordinates[2*i]= int(index/5)
        transposed_coordinates[2*i + 1]= index %5
    
    coordinates=[[0,0] for i in range(len(text))]
    for i in range(len(text)):
        coordinates[i]=[transposed_coordinates[i], transposed_coordinates[i + len(text)]]
    
    result = ""
    for i in range(len(text)):
        result += table[coordinates[i][0]*5+coordinates[i][1]]
    
    return result

def morse_e(text, bin_code=False, delimiter = " "):
    text=text.upper()
    return code_table_e(text, morse_code_table, {"-":"0", ".":"1"}, bin_code, delimiter)

def morse_d(text, bin_code=False, delimiter=" "):
    return code_table_d(text, morse_code_table, {"-":"0", ".":"1"}, bin_code, delimiter)    

def bacon1_e(text, bin_code=False, delimiter = " "):
    text=text.upper()
    return code_table_e(text, bacon1_table, {"a":"0", "b":"1"}, bin_code, delimiter)

def bacon1_d(text, bin_code=False, delimiter=" "):
    return code_table_d(text, bacon1_table, {"a":"0", "b":"1"}, bin_code, delimiter)    

def bacon2_e(text, bin_code=False, delimiter = " "):
    text=text.upper()
    return code_table_e(text, bacon1_table, {"a":"0", "b":"1"}, bin_code, delimiter)

def bacon2_d(text, bin_code=False, delimiter=" "):
    return code_table_d(text, bacon1_table, {"a":"0", "b":"1"}, bin_code, delimiter)    

def abc012(text, delimiter = " "):
    text=text.upper()
    return code_table_e(text, abc012_table, {}, False, delimiter)
    
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
    12
#    print("")
#    print(adfgvx_e("attack at 1200 AM", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy"))
#    print(adfgvx_d("DGDDDAGDDGAFADDFDADVDVFAADVX", "na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz", "privacy"))
#    decode_help()
#     print(bacon1_e("morse code", True))
#    print(bacon1_d("01011 01101 10000 10001 00100 / 00010 01101 00011 00100 ", True))
#     print(morse_d("00 000 101 111 1 / 0101 000 011 1 ",True))
#    print(affine_e("Affine cipher 0123",5,8))
#    print(beaufort("teststrings","beaufort"))
#    print(bifid_d("UAEOLWRINS", "bgwkzqpndsioaxefclumthyvr"))
#    print(polybius_d("52211533243324331543444423432444235214"))
#    print(polybius_e("WFENININESTTHSITHWD"))
#    print(kw(".*nest.*"))
#    print(hexbash("01359ab"))
