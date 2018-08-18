def rev(c):
    return c[::-1]
    
def columnar_e(c,col):
    p=[0]*len(c)
    left_col_cnt =len(c) % len(col)
    row_cnt1 = int(len(c)/len(col))+1
    row_cnt2 = int(len(c)/len(col))
    
    i=0
    for j in range(len(col)):
        ind=col.index(j+1)
        if ind<left_col_cnt:
            row_cnt=row_cnt1
        else:
            row_cnt=row_cnt2
        for k in range(row_cnt):
            p[i]=c[k*len(col)+ind]
            i+=1
            
    return p
    
def columnar_d(c,col):
    p=[0]*len(c)
    left_col_cnt =len(c) % len(col)
    row_cnt1 = int(len(c)/len(col))+1
    row_cnt2 = int(len(c)/len(col))

    i=0
    for j in range(len(col)):
        ind=col.index(j+1)
        if ind<left_col_cnt:
            row_cnt=row_cnt1
        else:
            row_cnt=row_cnt2
        for k in range(row_cnt):
            p[k*len(col)+ind]=c[i]
            i+=1
        
    return p
  
def disrupted_columnar_e(c,col):
    rows_full=int(len(c)/len(col))
    lastrow_len=len(c)%len(col)
    
    trans_pre=[0]*len(c) 
    ord_x=0
    curr_len=len(col)
    cnt = 0
    for i in range(rows_full):
        if curr_len == len(col):
            ord_x+=1
            curr_len=col.index(ord_x)
        else:
            curr_len+=1
        for j in range(curr_len):
            trans_pre[i*len(col)+j]=c[cnt]
            cnt+=1
    
    if lastrow_len>0:
        for j in range(lastrow_len):
            trans_pre[rows_full*len(col)+j]=c[cnt]
            cnt+=1
    
    ord_x=0
    curr_len=len(col)
    for i in range(rows_full):
        if curr_len == len(col):
            ord_x+=1
            curr_len=col.index(ord_x)
        else:
            curr_len+=1
        for j in range(curr_len,len(col)):
            trans_pre[i*len(col)+j]=c[cnt]
            cnt+=1
    
    p = columnar_e(trans_pre, col)
    return p

def disrupted_columnar_d(c,col):
    rows_full=int(len(c)/len(col))
    lastrow_len=len(c)%len(col)
    trans_pre=columnar_d(c, col)
    
    p=[0]*len(c) 
    ord_x=0
    curr_len=len(col)
    cnt = 0
    for i in range(rows_full):
        if curr_len == len(col):
            ord_x+=1
            curr_len=col.index(ord_x)
        else:
            curr_len+=1
        for j in range(curr_len):
            p[cnt]=trans_pre[i*len(col)+j]
            cnt+=1
    
    if lastrow_len>0:
        for j in range(lastrow_len):
            p[cnt]=trans_pre[rows_full*len(col)+j]
            cnt+=1
    
    ord_x=0
    curr_len=len(col)
    for i in range(rows_full):
        if curr_len == len(col):
            ord_x+=1
            curr_len=col.index(ord_x)
        else:
            curr_len+=1
        for j in range(curr_len,len(col)):
            p[cnt]=trans_pre[i*len(col)+j]
            cnt+=1
    
    return p
    
def railfence_e(text, rails, offset=0):
    place=[["",0] for i in range(len(text) + offset)] 
    line_cycle = list(range(rails)) + list(range(rails-1)[:0:-1])
    for i in range(len(text)):
        place[i + offset] = [text[i], line_cycle[(i + offset) %(rails*2 -2)]]
    
    result =""
    for i in range(rails):
        for s in place:
            if s[1] == i:
                result+=s[0]
    return result

def railfence_d(text, rails, offset=0):
    place=[["",0] for i in range(len(text) + offset)] 
    line_cycle = list(range(rails)) + list(range(rails-1)[:0:-1])
    for i in range(len(text)):
        place[i + offset] = ["", line_cycle[(i + offset) %(rails*2 -2)]]
    
    t = 0
    for i in range(rails):
        for j in range(len(text)):
            if place[j + offset][1] == i:
                place[j + offset][0]=text[t]
                t+=1
    
    result = ""
    for s in place:
        result += s[0]
    return result
    
def rect(text, col):
    result=""
    for i in range(len(text)):
        result+=text[i]
        if i %col == col-1:
            result+='\n'
    print(result)
