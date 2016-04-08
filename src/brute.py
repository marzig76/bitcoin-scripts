import sys
import ecdsa
import base58
import random
import pybip38
import hashlib

resultfile = open("results.txt", 'w')

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

target_addr = '1J5cjne6YVkgRTMTjqnaJVk1CWEEr3CcdX'
encpriv = '6PfRB98F9vZLhSpqY5URas5vYUU3qYQrpkJFTLuCg1FvDni6LwT3qAirkp'


def rando():
    return random.randrange(0, len(alphabet))


def guess(length):
    guess = ''
    for i in range(0, length):
        r = rando()
        guess += alphabet[r:r+1]

    return guess


def pub_from_priv(privkey):
    # generate signing and verifying keys from privkey
    signkey = ecdsa.SigningKey.from_string(
        privkey.decode('hex'), curve=ecdsa.SECP256k1)
    verifykey = signkey.verifying_key

    # build pubkey based on spec
    pubkey = ('\04' + verifykey.to_string()).encode('hex')
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(pubkey.decode('hex')).digest())
    build_key = '\00' + ripemd160.digest()
    d256_checksum = hashlib.sha256(
        hashlib.sha256(build_key).digest()).digest()[:4]
    addr = base58.b58encode(build_key + d256_checksum)

    return addr


while True:
    # generate key
    secret_key = guess(6)
    print secret_key

    # hint - only 3,4 or 5 uppercase characters
    count = 0
    for i in secret_key:
        if i == str.upper(i):
            count += 1

    if 3 <= count <= 5:
        # decrypt bip38 encrypted key
        wif = pybip38.bip38decrypt(secret_key, encpriv)

        if wif:
            # convert from wif to regular private key
            privkey = base58.b58decode(wif).encode('hex')[2:-8]
            addr = pub_from_priv(privkey)

            # if this matches, we have our bitcoin!
            if addr == target_addr:
                results = (
                    'secret_key: ' + secret_key + '\n' +
                    'addr: ' + addr + '\n' +
                    'wif: ' + wif + '\n' +
                    'privkey: ' + privkey
                )

                print(results)
                resultfile.write(results)
                sys.exit()
