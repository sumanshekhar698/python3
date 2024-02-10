hello = 'hello world'

#method and fn
print(len(hello))#len is a function

greeting = ''' Hey Today is
a good day 
to study Python'''#for multi line string we use triple quotes

language = 'python is a good language'
print(greeting)


#concatination
series1 = 'The vampire'
series2 =  'diaries'
fav_series = series1 + ' ' + series2
print(fav_series)



#dynamic unpacking of characters
movie = 'fighter'
a,b,c,d,e,f,g = movie #!CAUTION make sure the len and the no of variables are same
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

print('-------------------------------------------')
#Access of String
print(movie[-1])
print(movie[-5])

print(fav_series[-1])#last character can be accessed via -1
print(fav_series[len(fav_series)-1])


# compare two strings
flavor2 = 'chocalate'
flavor1 = 'chocalaVe'
print(flavor1 == flavor2)

# slicing
s = 'HelloWorld'
print(s[:])
print(s[::])
print(s[1:4])#starting index is inclusive and ending index is exclusive
s_sliced1 = s[:5]
print(s_sliced1)


print(s[::-1])#reverse string
print(s[::2])
print(s[::-2])


s_sliced2 = s[8:1:-1]# if negative step count reverse the positive index [end, start = start, end]
print(s_sliced2)
# print(s)


s_sliced3 = s[-4:-2]
print(s_sliced3)

print(s[2:100])#python handles out of range index gracefully
print(s[1000:199999])#python handles out of range index gracefully

