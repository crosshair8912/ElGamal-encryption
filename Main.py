import random

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def get_one_prime():
    #p
    for i in gen_primes():
        Buf = []
        if ((random.SystemRandom.random(i) >0.9) & (i>500 )):
            Buf.append(i)
            return random.choice(Buf)



def primary_primitive_root(input):
    #g
    Buf = random.SystemRandom().randrange(input)
    for i in range(Buf,input):
        if ((i**(input-1))%input == 1):
            return i

def private_key(input):
    #x
    Buf = [i for i in range(1,input)]
    return random.SystemRandom().choice(Buf)

def public_key_generate(prime,g,x):
    #y
    Buf = (g**x) % prime
    if Buf == 1:
        return 3
    else:
        return Buf



def random_k(prime):
    #k
    Buf = [i for i in range(1, prime-1)]
    return random.SystemRandom().choice(Buf)

def encrypt(message,prime,x,g,y):
    Buf = []
    Buf1 = []
    l = list(message)


    for i,index in enumerate(message):
        k = random_k(prime)
        a = (g ** k) % prime
        b = ((y ** k)* ord(l[i])) % prime
        Buf.append(b)
        Buf1.append(a)
    return list(zip(Buf1,Buf))

def decrypt(opt,prime,key):
    Buf = []
    for i in opt:
        Buf.append(chr((i[1]*(i[0]**(prime-1-key)))%prime))
    return Buf

a = get_one_prime()
x = private_key(a)
g = primary_primitive_root(a)
y = public_key_generate(a,g,x)

print("Our prime is: "+str(a))
print("Our primary primitive root is(g): "+ str(g))
print("Our private key X is: "+str(x))
print("Our public key Y is: "+str(y))

message = input("Type a word:")
output = encrypt(message,a,x,g,y)


print('Encrypted message is: ' + str(output))
print('Decrypted message is: ' + str(decrypt(output,a,x)))
