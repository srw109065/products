#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳到下一迴繼續
		name, price  = line.strip().split(',')
		products.append([name,price])
print(products)


#運行方式
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
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #encoding 解決編碼無法顯示中文
	f.write('商品,價格\n') #用來增加Excel 欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')