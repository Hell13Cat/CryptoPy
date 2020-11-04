import bs64, os, json

def is_folder(ref):
	try:
		os.listdir(path=ref)
		return 1
	except:
		return 0


def listdict(rf):
	list = os.listdir(path=rf)
	dirlist = []
	for one_l in list:
		ref = rf + "/" + one_l
		if is_folder(ref) == 1:
			dirlist.append(ref)
			dirlist.extend(listdict(ref))
	return dirlist

def todict(ref):
	dict = {}
	dirlist = listdict(ref)
	dirlist.append(ref)
	dict["folders"] = dirlist
	filelist = []
	count = -1
	for one_l in dirlist:
		count += 1
		list = os.listdir(path=one_l)
		for one_f in list:
			if is_folder(one_l + "/" + one_f) == 0:
				filelist.append({"name":one_f, "id":count, "data": bs64.frombin(bs64.to64(open(one_l+"/"+one_f, "rb").read()))})
	dict["files"] = filelist
	return dict

def fromdict(dict):
	dirlist = dict["folders"]
	filelist = dict["files"]
	for one_d in dirlist:
		os.makedirs("./ready"+str(one_d[1:]), mode=0o777, exist_ok=True)
	for one_f in filelist:
		bin = bs64.from64(bs64.tobin(one_f["data"]))
		file = open("./ready"+str(dirlist[one_f["id"]][1:])+"/"+str(one_f["name"]), "wb")
		file.write(bin)
		file.close()

def tojson(name, refs):
	with open("./cache/"+name, 'w') as fp:
		json.dump(todict(refs), fp)

def fromjson(name):
	with open("./cache/"+name) as json_file:
		data = json.load(json_file)
	fromdict(data)
	
#print(os.listdir(path="."))
#os.makedirs(path, mode=0o777, exist_ok=False) 
#print(os.walk(".", topdown=True, onerror=None, followlinks=False))
#print(os.listdir(path="."))
#os.makedirs(path, mode=0o777, exist_ok=False) 
#print(os.walk(".", topdown=True, onerror=None, followlinks=False))