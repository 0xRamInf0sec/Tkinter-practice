import base64
def encode(a):
    encoded=base64.b64encode(a.encode("utf-8"))
    encstr=str(encoded,"utf-8")
    print(encstr)
def decode(b):
    msg=b.encode('ascii')
    bytes=base64.b64decode(msg)
    message=bytes.decode('ascii')
    print(message)

print("\t\t Base64 encoder decoder")
inp=input("\nEnter 'E' for Encoding 'D' for Decoding:")
if inp=='E' or inp=='e':
    a = input("Enter message to encode:")
    encode(a)
else:
    b=input("\nEnter message to Decode:")
    decode(b)