import hashlib;

print( hashlib.sha256(str('root').encode()).hexdigest() )