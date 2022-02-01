import os 

products = []

if os.path.isfile("products.csv"):
    print("找到了")
    #讀取檔案    
    with open("products.csv", "r") as f:
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name,price])
    print(products)
else:
    print("沒有找到...")

#使用者輸入
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入商品價格: ")
    price = int(price)
    p = [name, price]
    products.append(p)
#印出購買紀錄
for p in products:
	print(p[0], "的價格是:", p[1])
	
pr = "商品,價格\n"
#寫入檔案
with open("products.csv", "w") as f:
	f.write(pr)
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")
