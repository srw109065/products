import os # operating system

products = []
#讀取檔案
if os.path.isfile('products.csv'):#檢查檔案
	print('找到檔愛了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格,日期' in line:
				continue #跳到下一迴繼續
			name, price, date  = line.strip().split(',')
			products.append([name,price,date])
	print(products)
else:
	print('找不到檔案...')

#運行方式
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':
		break
	price = input("請輸入商品價格: ")
	price = int(price)
	date = input("請輸入購買日期: ")
	#原始方式
	#p = []
	#p.append(name)
	#p.append(price)
	#三種結合的簡潔方式
	#p = [name, price]
	#更快速的方式
	products.append([name, price,date])

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #encoding 解決編碼無法顯示中文
	f.write('商品,價格,日期\n') #用來增加Excel 欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + ',' + (p[2]) + '\n')