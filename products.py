products = []
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':
		break
	price = input("請輸入商品價格: ")
	price = int(price)
	#原始方式
	#p = []
	#p.append(name)
	#p.append(price)
	#三種結合的簡潔方式
	#p = [name, price]
	#更快速的方式
	products.append([name, price])
print(products)
#把清單一個一個 拿出來打印
for p in products:
	print(p[0], '的價格是', p[1], '元')
#寫入Text
with open('products.csv', 'w', encoding='utf-8') as f: #encoding 解決編碼無法顯示中文
	f.write('商品,價格\n') #用來增加Excel 欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
#讀取Text
k = []
with open('products1.txt', 'r') as f:
	for p in f:
		print(p.strip())
		k.append(p.strip())
print(k)
