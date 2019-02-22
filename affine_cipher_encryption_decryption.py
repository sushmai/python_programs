#!/usr/bin/env python

uppercase = list(map(chr, range(ord("A"), ord("Z") + 1)))
lowercase = list(map(chr, range(ord('a'), ord('z') + 1)))
#symbols = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-",".", ":", ","]


alphabet = uppercase + lowercase #"+symbols"

def main():
    print("***Affine Cipher*** ")
    
    plain_text = input("enter text to encrypt : \n")
    #plain_text = ("helloworld")
    #plain_text = ("OverhilloverdalethoroughbushthoroughbrierbrierOverparkoverpaleThoroughfloodthoroughfireIdowandereverywhereSwifterthanthemoonssphereAndIservetheFairyQueenTodewherorbsuponthegreenThecowslipstallherpensionersbeThecowslipstallherpensionersbeIntheirgoldcoatsspotsyouseeThoseberubiesfairyfavoursInthosefreckleslivetheirsavoursImustgoseeksomedewdropshereAndhangapearlineverycowslipsear")                                                             
                              
                                    
                               
    print("Plain Text : " + plain_text)

    cipher_text = cipher(plain_text, 9, 13)
    print("cipher_text : {0}".format(cipher_text))

    #Letter Count for CipherText
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lettercount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                   'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
                   'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
                   'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in cipher_text.upper():
        if letter in LETTERS:
            lettercount[letter] += 1
    print(lettercount)

    deciphertext = decipher(cipher_text, 9, 13)
    print("deciphertext : {0}".format(deciphertext))
    return

def hcf(a, b) : return a if b == 0 else hcf(b, a % b)

def areRelativePrimes(a, b): return hcf(a,b) == 1

def getMultiplicativeInverse(a):
    result = 1

    for i in range(1, len(alphabet)):
        if(a * i ) % len(alphabet) == 1:
            result = i
    return result
    
#encryption
def cipher(plain_text, a, b):
    if(a<1 or a > len(alphabet)):
        return("a must be in the interval of [1, {0}]".format(len(alphabet)))
    if(b < 1 or b > len(alphabet)):
        return("b must be in the interval of [1, {0}]".format(len(alphabet)))
    if (not areRelativePrimes(a, len(alphabet))):
        return("a must be relatively prime to {0}".format(len(alphabet)))
    result = ""
    m = len(alphabet)
    for pChar in plain_text:
        p = alphabet.index(pChar)
        c = a * p + b % m
        cIdx = c % len(alphabet)
        cChar = alphabet[cIdx]

        result += cChar        
    return result

#Decryption
def decipher(ciphertext, a, b):
    if(a < 1 or a >len(alphabet)):
        return("a must be in the interval of [1, {0}]".format(len(alphabet)))
    if(b < 1 or b > len(alphabet)):
        return("b must be in the interval of [1, {0}]".format(len(alphabet)))
    if (not areRelativePrimes(a, len(alphabet))):
        return("a must be relatively prime to {0}".format(len(alphabet)))
    result = ""
    m = len(alphabet)
    for cChar in ciphertext:
        c = alphabet.index(cChar)
        aInverse = getMultiplicativeInverse( a )
        pIdx = aInverse * (c - b) % len(alphabet)
        if pIdx < 0:
            pIdx += len(alphabet)

        pChar = alphabet[pIdx]

        result += pChar
    return result
main()
    


    
