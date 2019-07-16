#返回一个数值
def something_return1(a,b)
	c=a+b
	return c

c= something_return1(1,2)

##############################################################

#返回多个数值
def something_return2(a,b):
	c=a+b
	d=a-b
	return c,d

	#第一种引用方式
c = something_return2(1,2)[0]
d = something_return2(1,2)[1]

	#第二种引用方式
c,d = something_return2(1,2)[0]
