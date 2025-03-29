#!/usr/bin/python3

#1.标识符
#第一个字符必须是字母表中字母或下划线 _ 。
#标识符的其他的部分由字母、数字和下划线组成。
#标识符对大小写敏感。

#python保留字即关键字
#>>> import keyword
#>>> keyword.kwlist
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

import keyword
print(keyword.kwlist)

#2.注释
#Python中单行注释以 # 开头
#多行注释以 ''' 开头，以 ''' 结束
# 第一个注释
print ("Hello, Python!")
'''
第二个注释
第三个注释
第四个注释
'''

#3.行与缩进
'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
'''
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")
    print ("False")    # 缩进不一致，会导致运行错误

#4.多行语句
'''
在Python中，换行符不是语句的结束符，
换行符后面的代码会被视为同一行的一部分。
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
'''
item_one = 10
item_two = 20
item_three = 30
total = item_one + \
        item_two + \
        item_three
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
for item in total:
    print(item)

#5.数字(Number)类型
'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
'''

#6.字符串(String)类型
'''
字符串类型有 3 种：单引号、双引号和三引号。
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号(三引号也可以是""")可以指定一个多行字符串。
转义符 \。
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
'''

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

print(word)
print(sentence)
print(paragraph)

print("this is a line with \n")
print(r"this is a line with \n")

str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#7.等待用户输入
inputstr = input("\n\n按下 enter 键后退出。")#以上代码中 ，\n\n 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。
print(inputstr)

#8.同一行显示多条语句,Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
print('\n\n',end='')
print('Hello World!',end='')

#9.代码组
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
'''
name = 10
if name > 10 :
    print('name is greater than 10')
elif name > 5 :
    print('name is greater than 5')
else :
    print('name is less than 5')
    
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d\t' % (i, j, i * j), end='')
    print('')

#10.print 输出
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end="" )
print( y, end='' )
print("--------")


#11.import 与 from...import
'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
#导入模块sys
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#导入模块sys的argv，path成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


print(type(42))
print(2 ** 3)