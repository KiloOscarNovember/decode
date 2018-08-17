def assign_digits(x):
    a=[0]*len(x)

    for i in range(len(x)):
        a[i]=[x[i],i]
        
    a.sort(key=lambda t:(t[0],t[1]))

    b=[0]*len(x)
    for i in range(len(x)):
        b[i]=a[i][1]
        
    c=[0]*len(x)
    for i in range(len(x)):
        c[b[i]]=i+1

    return c

def mixed_alphabet(keyword, combined=False):
    kw_alphabet_added = keyword.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if combined:
        kw_alphabet_added = kw_alphabet_added.replace("J","I")

    already_appeared=[]
    result =""
    for s in kw_alphabet_added:
        if not s in already_appeared:
            result+=s
            already_appeared.append(s)
    return result
    
def mixed_alphanumeric(keyword):
    kw_alphabet_added = keyword.upper() + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    already_appeared=[]
    result =""
    for s in kw_alphabet_added:
        if not s in already_appeared:
            result+=s
            already_appeared.append(s)
    return result

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text