#Tsak1
#!/usr/bin/env python3

''' Для каждого регулярного выражения, которое требуется написать,
 указаны строки, соответствующие этому выражению (они отмечены знаком +),
 а также строки, не соответствующие этому выражению (отмечены знаком -)'''

# + a
# + ab
# - b
# - ba
REGEXP_1 = r'a'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r'\w{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'\D*[34]$'


# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'(?!zver$)'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'[ab]{3}$'


# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r'\w{2}{3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'.* \w{3} '

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'(?!.{4}$)'
#Task2
#!/usr/bin/env python3
'''
 Для каждого регулярного выражения, которое требуется написать,
 указана строка, в которой нужно найти подстроку, а следом
 после стрелки (--->) указана сама искомая подстрока
'''

# bab ---> a
# bcb ---> c
# bxb ---> x
REGEXP_1 = r'[^b]'

# ooooAAAooooo ---> AAA
# asdfasdAAAAfasdf ---> AAAA
# AAAAAAfasdf ---> AAAAAA
# iiiiiA ----> A
REGEXP_2 = r'A+'

# There is <html> tag ---> <html>
# color can be used as <font color='red'> ---> <font color='red'>
# There is x <> 10 and something was wrong with < or > brace. ---> < or >
REGEXP_3 = r'<[^>]+>'

# C@n Y0u f1nd CaPoAira? ---> CaPoAira
# s0 Wh@t i5 CamelStyle? ---> CamelStyle
# Any simple word should match. ---> Any
# I like regular expressions ---> like
REGEXP_4 = r'(?<=\b)[a-zA-Z]{2,}(?=[? ])'

# all those that were numbered of the camps throughout their hosts were 603550. ---> 603550
# What is the meaning of life, the universe and everything? *42* Douglas Adams ---> 42
# Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898. ----> 29
REGEXP_5 = r'\d+'

# New York: W. H. Freeman, pp. 347-353, 1991. ---> Freeman
# set out to travel much faster than light ---> travel
# Arise ye, and depart; for this is not your rest... ---> depart
REGEXP_6 = r'\w{6,7}'

# I know that cat can catch a mouse! ---> cat can catch a mouse
# But this mouse is faster than the cat. ---> mouse is faster than the cat
# Mouse Mickey is not a simple mouse. Tom is a dummy cat. ---> mouse. Tom is a dummy cat
REGEXP_7 = r'(mouse|cat).*(mouse|cat)'

# his phone number was 892512366482. ---> 892512366482
'the number above is invalid phone number'
# I called +7 999 648-99-86 ans it was right. ---> +7 999 648-99-86
# Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99 ---> 8 915 747-68-99
REGEXP_8 = r'(8|\+7)[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2,3}'
REGEXP_8 = r'(8|\+7)(\s|\d|-)+\d'
#Task3
#!/usr/bin/env python3
'''
 Для каждого регулярного выражения, которое требуется написать,
 указана строка, в которой нужно найти подстроки, а следом
 после стрелки (--->) указан список подстрок, которые нужно найти
'''
# 1 a 1 2 b ---> a, b
# z 2 y     ---> z, y
REGEXP_1 = r'[a-z]'

# aaa bbb ccc ---> aaa, bbb, ccc
# ddd eee fgh ---> ddd, eee, fgh
# a1b c2d e3f ---> a1b, c2d, e3f
REGEXP_2 = r'\w{3}'

# a aa aaa ---> aa, aaa
# b bb bbb ---> bb, bbb
# a bb aaa ---> bb, aaa
REGEXP_3 = r'\w{2,3}'

# 1.1.1.1 aaaa bbbbb      ---> 1.1.1.1
# a.a.a.a bbbb 2.2.2.2    ---> 2.2.2.2
# 3.3.3.3 cccc 4.4.4.4    ---> 3.3.3.3, 4.4.4.4
# 255.23.0.1 cccc 4.4.4.4 ---> 255.23.0.1, 4.4.4.4
# 255.0.23.1 cccc 4.4.4.4 ---> 255.0.23.1, 4.4.4.4
REGEXP_4 = r'\d+\.\d+\.\d+\.\d'

# aaa Abbb ccc ---> Abbb
# Aaa Abbb ccc ---> Aaa, Abbb
# Caa Cbb Accc ---> Accc
REGEXP_5 = r'A\w+'

# a b c d e f ---> a, b, e, f
# abcdef      ---> a, b, e, f
# adf         ---> a, f
# acf         ---> a, f
REGEXP_6 = r'(a|b|[e-z])'

# aaa +1.0 bb              ---> +1.0
# aaa -1.0 bb              ---> -1.0
# aaa -123.234 bb +111.999 ---> -123.234, +111.999
REGEXP_7 = r'[\+|-]\d+\.\d+'

# aaa 18-04-2016 bbb            ---> 18-04-2016
# aaa 18.04.2016 bbb            ---> 18.04.2016
# aaa 18-04-ABCD bbb 18.04.2016 ---> 18.04.2016
# aaa 18/04/ABCD bbb 18/04/2016 ---> 18/04/2016
# aaa 18/04/ABCD bbb 18/4/2016  ---> 18/4/2016
REGEXP_8 = r'\d{2}.\d{1,2}.\d{4}'