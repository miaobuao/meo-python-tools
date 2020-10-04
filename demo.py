import meo  #导入

test = meo.ask("http://dimtub.com") #目标网站
print(test.ss) #打印网站响应花费的精确秒数
print(test.ms) #毫秒数
print(test.r) #获取requests.get的结果
path = "1/文件夹/网页内容.txt" #路径，也可以直接写文件名
test.out(path)	#把获取到的HTML内容写到指定文件中

path2 = "2/2.txt"
fo = meo.addto(path2, "222")  #在path2路径下追加222，并且不会换行

fo = meo.tofile(path2, "333") #把path2内容覆盖成333
fo = meo.addto(path2, "222", 10)  #打开2.txt文件，空开十行再追加222