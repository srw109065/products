products = []
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':
		break
	price = input("請輸入商品價格: ")
	#原始方式
	#p = []
	#p.append(name)
	#p.append(price)
	#三種結合的簡潔方式
	#p = [name, price]
	#更快速的方式
	products.append([name, price])
print(products)