import base64

def to64(data):
	e = base64.b64encode(data)
	return e

def from64(data):
	d = base64.b64decode(data)
	return d

def tobin(data):
	b = data.encode("UTF-8")
	return b

def frombin(data):
	b = data.decode("UTF-8")
	return b