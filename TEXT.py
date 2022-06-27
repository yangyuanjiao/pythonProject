long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
T = long_text.split('\n');
print(T)
name = T[1];
lei =  T[2];

t1 = long_text.count('.')
t2 = long_text.find('.')

subfund=[]
title=[]
isin=[]

for i in range(0, t1):
    title.append(i)
    title[i] = long_text[t1+1:t2]

for i in range(0,t1):
    t3 = t1;
    t1 = long_text.find('.', t3 + 1);
    t4 = long_text.find('FUND')

    for i in range(0, t4):
        isin.append(i)
        isin[i] = long_text[t1+1:t2]
