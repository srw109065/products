import os # operating system


#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格,日期' in line:
				continue #跳到下一迴繼續
			name, price, date  = line.strip().split(',')
			products.append([name,price,date])
	return products

#運行方式
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #encoding 解決編碼無法顯示中文
		f.write('商品,價格,日期\n') #用來增加Excel 欄位名稱
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + ',' + (p[2]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案
		print('找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()