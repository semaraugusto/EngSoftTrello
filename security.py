import hashlib
import binascii
import os

def criptografaSenha(senha):
    sal = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', senha.encode('utf-8'),
                                  sal, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (sal + pwdhash).decode('ascii')

def verificaSenha(senhaCorreta, senhaUsada):
    sal = senhaCorreta[:64]
    senhaSalva = senhaCorreta[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  senhaUsada.encode('utf-8'),
                                  sal.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == senhaSalva
