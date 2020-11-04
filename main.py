import bs64, os, jcr
from cryptography.fernet import Fernet

print("+--->\n| CrypterPy 1.0\n+--->")
os.makedirs("./cache", mode=0o777, exist_ok=True)
if input("e?>>> ") == "y":
	name_r = input("Result name>>> ")
	dirs = input("Folder >>>")
	jcr.tojson(name_r+".ncf", dirs)
	key = Fernet.generate_key()
	open("./"+name_r+".kcf", "wb").write(key)
	f = Fernet(key)
	results = f.encrypt(open("./cache/"+name_r+".ncf", "rb").read())
	open("./"+name_r+".ecf", "wb").write(results)
else:
	name = input("Name>>> ")
	key = open("./"+name+".kcf", "rb").read()
	f = Fernet(key)
	file = open("./"+name+".ecf", "rb").read()
	open("./cache/"+name+".ncf", "wb").write(f.decrypt(file))
	jcr.fromjson(name+".ncf")