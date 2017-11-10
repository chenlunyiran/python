# 读取文本文件
f = open('D:/test.txt', 'r')
print(f.read())
f.close()

try:
    f = open('D:/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 每次都这么写实在太繁琐，Python引入了with语句来自动帮我们调用close()方法
with open('D:/test.txt', 'r') as f:
    print(f.read())

with open('D:/test.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

# 读取二进制文件
with open('D:/image.jpg', 'rb') as f:
    print(f.read())

#写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('D:/test.txt', 'w') as f:
    f.write('Hello, world!')

