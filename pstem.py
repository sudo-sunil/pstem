s=input().lower()
#print(s) 
l=[]
m=0
vowels=['a','e','i','o','u']


def vowel_or_not(x):
    if x in vowels:
        return True
    elif x=='y' and len(l)>=1 and l[-1] == 'c':
        return True
    else:
        return False

for i in range(len(s)):
    if vowel_or_not(s[i]) == True:
        l.append('v')
    else:
        l.append('c')
        
for i in range(len(l)):
    if i < len(l)-1:
        if l[i]=='v' and l[i+1]=='c':
            m +=1

def double_cons(x,y):
    if vowel_or_not(x)==False:
        if x==y:
            return True
        else:
            return False
    else:
        return False

def cvc(a,b,c,s):
    if (vowel_or_not(a)==False) and (vowel_or_not(b)==True) and (vowel_or_not(c)==False):
        if (c !='w') or (c != 'x') or (c != 'y'):
            return True
        else:
            return False
    else:
        return False

#print(l)    
#print(m)

def step1a(s):
    if s.endswith('sses'):
        a = s[-4:]
        s = s.replace(a,'ss')
    elif s.endswith('ies'):
        a = s[-3:]
        s = s.replace(a,'i')
    elif s.endswith('ss'):
        a = s[-2:]
        s = s.replace(a,'ss')
    elif s.endswith('s'):
        b = list(s)
        b[-1] = ''
        s = "".join(b)

    return s

def step1b(s):
    if m>0 and s.endswith('eed'):
        a = s[-3:]
        s = s.replace(a,'ee')

    elif ('v' in l[:-2]) and s.endswith('ed'):
        b = list(s)
        b[-2:] = ''
        s = "".join(b)
        if m==1 and (cvc(s[-3],s[-2],s[-1],s)==True):
            a = s[-3:]
            s = s.replace(a,'e')
        elif s.endswith('at'):
            a = s[-2:]
            s = s.replace(a,'ate')
        elif s.endswith('bl'):
            a = s[-2:]
            s = s.replace(a,'ble')
        elif s.endswith('iz'):
            a = s[-2:]
            s = s.replace(a,'ize')
        elif double_cons(s[-1],s[-2])==True:
            if not (s.endswith('l') or s.endswith('s') or s.endswith('z')):
                a = s[-2:]
                s = s.replace(a,s[-1])
        

    elif ('v' in l[:-3]) and s.endswith('ing'):
        b = list(s)
        b[-3:] = ''
        s = "".join(b)
        if m==1 and (cvc(s[-3],s[-2],s[-1],s)==True):
            a = s[-3:]
            s = s.replace(a,'e')
        elif s.endswith('at'):
            a = s[-2:]
            s = s.replace(a,'ate')
        elif s.endswith('bl'):
            a = s[-2:]
            s = s.replace(a,'ble')
        elif s.endswith('iz'):
            a = s[-2:]
            s = s.replace(a,'ize')
        elif double_cons(s[-1],s[-2])==True:
            if not (s.endswith('l') or s.endswith('s') or s.endswith('z')):
                a = s[-2:]
                s = s.replace(a,s[-1])
    return s

def step1c(s):
    if ('v' in l[:-1]) and s.endswith('y'):
        s = s.replace(s[-1],'i')
    return s
    
def step2(s):
    if m>0:
        if s.endswith('ational'):
            a = s[-7:]
            s = s.replace(a,'ate')
        elif s.endswith('ization'):
            a = s[-7:]
            s = s.replace(a,'ize')
        elif s.endswith('iveness'):
            a = s[-7:]
            s = s.replace(a,'ive')
        elif s.endswith('fulness'):
            a = s[-7:]
            s = s.replace(a,'ful')
        elif s.endswith('ousness'):
            a = s[-7:]
            s = s.replace(a,'ous')
        elif s.endswith('tional'):
            a = s[-6:]
            s = s.replace(a,'tion')
        elif s.endswith('biliti'):
            a = s[-6:]
            s = s.replace(a,'ble')
        elif s.endswith('entli'):
            a = s[-5:]
            s = s.replace(a,'ent')
        elif s.endswith('ousli'):
            a = s[-5:]
            s = s.replace(a,'ous')
        elif s.endswith('ation'):
            a = s[-5:]
            s = s.replace(a,'ate')
        elif s.endswith('alism'):
            a = s[-5:]
            s = s.replace(a,'al')
        elif s.endswith('aliti'):
            a = s[-5:]
            s = s.replace(a,'al')
        elif s.endswith('iviti'):
            a = s[-5:]
            s = s.replace(a,'ive')
        elif s.endswith('enci'):
            a = s[-4:]
            s = s.replace(a,'ence')
        elif s.endswith('anci'):
            a = s[-4:]
            s = s.replace(a,'ance')
        elif s.endswith('izer'):
            a = s[-4:]
            s = s.replace(a,'ize')
        elif s.endswith('abli'):
            a = s[-4:]
            s = s.replace(a,'able')
        elif s.endswith('alli'):
            a = s[-4:]
            s = s.replace(a,'al')
        elif s.endswith('ator'):
            a = s[-4:]
            s = s.replace(a,'ate')
        elif s.endswith('eli'):
            a = s[-3:]
            s = s.replace(a,'e')
    return s
    
def step3(s):
    if m>0:
        if s.endswith('icate'):
            a = s[-5:]
            s = s.replace(a,'ic')
        elif s.endswith('ative'):
            a = s[-5:]
            s = s.replace(a,'')
        elif s.endswith('alize'):
            a = s[-5:]
            s = s.replace(a,'al')
        elif s.endswith('iciti'):
            a = s[-5:]
            s = s.replace(a,'ic')
        elif s.endswith('ical'):
            a = s[-4:]
            s = s.replace(a,'ic')
        elif s.endswith('ness'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('ful'):
            a = s[-3:]
            s = s.replace(a,'')
        
    return s

def step4(s):
    if m>1:
        if s.endswith('ement'):
            a = s[-5:]
            s = s.replace(a,'')
        elif s.endswith('ance'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('ence'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('able'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('ible'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('ment'):
            a = s[-4:]
            s = s.replace(a,'')
        elif s.endswith('ant'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ent'):
            a = s[-3:]
            s = s.replace(a,'')    
        elif s.endswith('sion') or s.endswith('tion'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ism'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ate'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('iti'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ous'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ive'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('ize'):
            a = s[-3:]
            s = s.replace(a,'')
        elif s.endswith('al'):
            a = s[-2:]
            s = s.replace(a,'')
        elif s.endswith('er'):
            a = s[-2:]
            s = s.replace(a,'')
        elif s.endswith('ic'):
            a = s[-2:]
            s = s.replace(a,'')
        elif s.endswith('ou'):
            a = s[-2:]
            s = s.replace(a,'')
    return s
        
def step5a(s):
    if m>1 and s.endswith('e'):
        s = s.replace(s[-1],'')
    elif m==1 and (cvc(s[-4],s[-3],s[-2],s)==False) and s.endswith('e'):
            s = s.replace(s[-1],'')
    return s

def step5b(s):       
    if m>1 and (double_cons(s[-1],s[-2])==True):
        if s.endswith('l'):
            a = s[-2:]
            s = s.replace(a,s[-1])
    return s

s = step1a(s)
s = step1b(s)
s = step1c(s)
s = step2(s)
s = step3(s)
s = step4(s)
s = step5a(s)
s = step5b(s)

print(s)