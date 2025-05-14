import os

cwd = os.getcwd()

print(cwd)

list = os.listdir(r"C:\\Users\\om\\Desktop\\material_wise\\3 os examples")

print(list)

for root,dirs,files in os.walk(r"C:\\Users\\om\\Desktop\\material_wise\\3 os examples"):
	print("files",files)
	print("dirs",dirs)
	print("list",list)