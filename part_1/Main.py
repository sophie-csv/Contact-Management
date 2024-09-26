# f = open('test.txt', 'w')
# f.write('sophie')
# f.close()

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

f = open('test.txt', 'r')
text = f.read()
f.close()

text += ' and he is the best'

f = open('test.txt', 'w')
f.write(text)
f.close()

