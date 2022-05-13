import random as r

def son_top(son = 10):
    taxmin = int(input(f'1 dan {son} gacha son o`yladim topa olasizmi?\n>>'))
    son = r.randint(1, son)
    sanoq = 1
    while son != taxmin:
        if son > taxmin:
            sanoq += 1
            taxmin = int(input('Xato, men o`ylagan son bundan kattaroq, Yana harakat qiling\n>>'))
        elif son < taxmin:
            sanoq += 1
            taxmin = int(input('Xato, men o`ylagan son bundan kichikroq, Yana harakat qiling\n>>'))
    else:
        print(f'TOPDINGIZ! {son} sonini o`ylagan edim. {sanoq} ta taxmin bilan topdingiz. Tabriklayman!')
    return sanoq

def sonimni_top(son = 10):
    print(f'1 dan {son} gacha son o`ylang topishga harakat qilaman.')
    input('Son o`ylagan bo`lsangiz istalgan tugmani bosing.')
    minn = 1
    maks = son
    num = r.randint(1, son)
    sanoq = 1
    while 1:
        javob = input(f'Siz {num} sonini o`yladingiz: to`g`ri(T), son bundan kattaroq(+) yoki kichikroq(-)??')
        if javob == '-':
            maks = num - 1
            sanoq += 1
            num = r.randint(minn, maks)
        elif javob == '+':
            minn = num + 1
            sanoq += 1
            num = r.randint(minn, maks)
        elif javob.lower() == 't':
            print(f'Soningizni {sanoq} ta taxmin bilan topdim!')
            break
    return sanoq

def play(son = 10):
    yana = 1
    while yana:
        taxminlar_user = son_top(son)
        taxminlar_pc = sonimni_top(son)
        if taxminlar_pc > taxminlar_user:
            print('Tabriklayman. Siz yutdingiz!')
        elif taxminlar_pc < taxminlar_user:
            print('Men yutdim!')
        else:
            print('Durrang!')
        yana = int(input('Yana o`ynashni xohlaysizmi: ha(1) / yo`q(0)??'))
        
play()