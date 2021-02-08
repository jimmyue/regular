import re

#创建一个Regex对象，r使用原始字符串
print('1.括号()：分组匹配')
phonetext=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phonenumber=phonetext.search('My phone number is 020-222-1234.')
print(phonenumber.group())
print(phonenumber.group(1))
print(phonenumber.group(2))
areaCode, mainNumber = phonenumber.groups()
print(areaCode, mainNumber)

#管道|匹配，返回第一次匹配
print('\n2.管道|：返回第一次匹配')
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

#问号实现可选匹配,字符?表明它前面的分组在这个模式中是可选的
print('\n3.问号?：前面的分组可选')
heroRegex = re.compile (r'Bat(wo)?man')
mo1 = heroRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = heroRegex.search('The Adventures of Batwoman')
print(mo2.group())

#用星号匹配0次或多次，星号之前的分组可以在文本中出现任意次数
print('\n4.星号*：前面的分组出现任意次')
heroRegex = re.compile (r'Bat(wo)*man')
mo1 = heroRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = heroRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = heroRegex.search('The Adventures of Batwowoman')
print(mo3.group())

#加号匹配一次或多次，加号之前的分组可以在文本中出现1次及以上
print('\n5.加号+：前面的分组出现1次及以上')
heroRegex = re.compile (r'Bat(wo)+man')
mo1 = heroRegex.search('The Adventures of Batman')
print(mo1)
mo2 = heroRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = heroRegex.search('The Adventures of Batwowoman')
print(mo3.group())

#花括号匹配特定次数
print('\n6.花括号{}：前面的分组匹配花括号内的次数')
haRegex = re.compile(r'(Ha){2,3}')
mo1=haRegex.search('1Ha1')
print(mo1)
mo2=haRegex.search('2HaHa2')
print(mo2.group())
mo3=haRegex.search('3HaHaHa3')
print(mo3.group())

#贪心和非贪心，Python 的正则表达式默认是“贪心”的
print('\n7.非贪心{}?：尽可能匹配花括号内最少的次数')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

#findall()，返回所有匹配
print('\n8.findall：无分组时返回字符串列表，有分组时返回元组的列表')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo1=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') 
mo2=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)


# 字符分类,字符分类对于缩短正则表达式很有用
print('\n9.字符分类：+代表前面对呀出现任意次，[]大括号内标示只出现对应值')
xmasRegex = re.compile(r'\d+\s\w+')
mo=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

#建立自己的字符分类，[]匹配括号内，[^]匹配非括号内
print('\n10.大括号[]：[]匹配括号内，[^]匹配非括号内')
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1=vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo2=vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)

#插入字符和美元字符，插入字符匹配开始处，美元字符匹配结尾处
print('\n11.插入字符和美元字符：插入字符^匹配开始处，美元字符$匹配结尾处')
wholeStringIsNum = re.compile(r'^\d+$')
mo1=wholeStringIsNum.search('1234567890')
print(mo1.group())
mo2=wholeStringIsNum.search('12345xyz67890')
print(mo2)
mo3=wholeStringIsNum.search('12 34567890')
print(mo3)

#通配字符，匹配除了换行外所有字符
print('\n12.句号.：匹配除了换行外所有字符')
atRegex = re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

#点-星匹配所有字符
print('\n13.点-星.*：匹配除了换行外所有字符')
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

#用句点字符匹配换行
print('\n14.句点字符：用re.DOTALL作为re.compile()的第二个参数,可匹配换行')
noNewlineRegex = re.compile('.*')
mo1=noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo1)
newlineRegex = re.compile('.*', re.DOTALL)
mo2=newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo2)

#不区分大小写
print('\n15.不区分大小写：用re.I作为re.compile()的第二个参数,可不区分大小写')
robocop = re.compile(r'robocop', re.I)
mo1=robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo1)
mo2=robocop.search('ROBOCOP protects the innocent.').group()
print(mo2)
mo3=robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(mo3)

# ?匹配零次或一次前面的分组。
# *匹配零次或多次前面的分组。
# +匹配一次或多次前面的分组。
# {n}匹配n次前面的分组。
# {n,}匹配n次或更多前面的分组。
# {,m}匹配零次到m次前面的分组。
# {n,m}匹配至少n次至多m次前面的分组。
# {n,m}?或*?或+?对前面的分组进行非贪心匹配。
# ^spam意味着字符串必须以spam开始。
# spam$意味着字符串必须以spam结束。
# .匹配所有字符,换行符除外。
# \d、\w 和\s 分别匹配数字、单词和空格。
# \D、\W 和\S 分别匹配出数字、单词和空格外的所有字符。
# [abc]匹配方括号内的任意字符（诸如 a、b 或 c）。
# [^abc]匹配不在方括号内的任意字符。

#sub()方法替换字符串
print('\nsub()方法：替换字符')
mo='WOW: -12.3% YOY(W): +12.3%   MOM: -1.3% YOY(M): -0.3% '
patt=re.compile(r'([+-]\d+\.\d\%)')
result=patt.split(mo)
print(mo)
text=['+11.2%','+11.3%','-1.2%','-1.3%']
mo=re.sub(re.escape(result[1]),text[0],mo)
mo=re.sub(re.escape(result[3]),text[1],mo)
mo=re.sub(re.escape(result[5]),text[2],mo)
mo=re.sub(re.escape(result[7]),text[3],mo)

def findf(str1,n):
	a=str1.find('-',n)
	b=str1.index('%',str1.find('-',n))+1
	return a,b

print(mo.count('-'))
n1=findf(mo,1)
n2=findf(mo,n1[1])

print(mo[n1[0]:n1[1]])
print(mo[n2[0]:n2[1]])

class MyNumbers:
	def __iter__(self):
		self.n = 1
		return self

	def __next__(self):
		if self.n <= str1.count('-'):
			str1='WOW: -12.3% YOY(W): +12.3%   MOM: -1.3% YOY(M): -0.3% '
			start=1
			a=str1.find('-',start)
			b=str1.index('%',str1.find('-',start))+1
			start=b
			self.n += 1
			return a,b
		else:
			raise StopIteration

res=MyNumbers()
myiter = iter(res)
for x in myiter:
  print(x)
