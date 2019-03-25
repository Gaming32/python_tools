"Converts between DHCP unique id and string (both ways)"
def encode_id(string, include_x = False):
	"Encodes a string to a DHCP unique id"
	out = ''
	for c in string.strip():
		out += hex(ord(c))[2:]
	out = ('0x' if include_x else '') + out.lower()
	return out
from python_tools.tools import str_split_len
def decode_id(id):
	"Decodes a DHCP unique id to a string"
	id = id.lower().replace('0x', '')
	if len(id) % 2 != 0: id = '0' + id
	chars = str_split_len(id, 2)
	out = ''
	try:
		for char in chars:
			out += chr(eval('0x' + str(char)))
	except SyntaxError:
		raise AttributeError('Invalid character in id (id was %s)' % id)
	return out
	
if __name__ == '__main__':
	import sys

	try: encode = sys.argv.index('-e')
	except ValueError: encode = -1

	try: decode = sys.argv.index('-d')
	except ValueError: decode = -1

	if encode != -1:
		string = sys.argv[encode + 1]
	else: string = 'Encoded!'
	encoded = encode_id(string, True)
	if decode != -1:
		string = sys.argv[decode + 1]
	else: string = '0x4465636F64656421'
	decoded = decode_id(string)
	
	print(encoded + '\n' + decoded)