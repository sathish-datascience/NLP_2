import os

cwd = os.getcwd()

print(cwd)




for root,files,lists in os.walk(r"C:\\\\Users\\om\\Desktop\\material_wise\\3 os examples"):
	print("root",root)
	print("files",files)
	print("list",lists)