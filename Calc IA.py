import sys
import numpy as np
from random import randint
plaintext = input("Enter text to be encrypted:")
plaintextASCII = [ord(c) for c in plaintext]
key = []
key.insert(0, randint(1, 255) / 2550)
key.insert(1, randint(1, 255) / 2550)
key.insert(2, randint(1, 127))
key.insert(3, randint(1, 127))
key.remove(key[2])
key.insert(2, key[1] * key[2])

keyDer1 = list(key)
del keyDer1[3]
keyDer1[0] = keyDer1[1] * 3
keyDer2 = []
keyDer2.append(2 * (keyDer1[1]**2) * keyDer1[0])
keyDer2.append(2 * keyDer1[0] * keyDer1[1] * keyDer1[2])
poiX = keyDer2[1] / keyDer2[0]
poiY = (poiX * key[1] - key[2])**3 * key[0] + key[3]
poi = poiX + poiY
plaintextStep1 = []
for i in plaintextASCII:
    plaintextStep1.append(i + poi)


npPlaintextStep2 = []
multMatrix = [[0.5,0.75], [0.25,1]]
npMultMatrix = np.matrix(multMatrix)
for x in range(1, int(len(plaintextStep1) / 4 if len(plaintextStep1) % 4 == 0 else len(plaintextStep1) / 4 + 1) + 1):
    newMatrix = []
    if x * 4  > len(plaintextStep1):
        toPutInMatrix = []
        while len(toPutInMatrix) < len(plaintextStep1) % 4:
            toPutInMatrix.append(plaintextStep1[(x*4) - 4 + len(toPutInMatrix)])
        while len(toPutInMatrix) <= 4:
            toPutInMatrix.append(0)
        newMatrix = [[toPutInMatrix[0], toPutInMatrix[1]], [toPutInMatrix[2], toPutInMatrix[3]]]
    else:
        newMatrix = [[plaintextStep1[x*4-4 - 1], plaintextStep1[x*4-4]], [plaintextStep1[x*4-4 + 1], plaintextStep1[x*4-4 + 2]]]
    npMatrix = np.matrix(newMatrix)
    newValues = npMatrix * npMultMatrix
    for l in newValues:
          for i in l:
              npPlaintextStep2.append(i)
plaintextStep2 = np.asarray(npPlaintextStep2).reshape(-1)

cipherText = []
for x in plaintextStep2:
    x = x * key[1]
    x = x - key[2]
    x = x ** 3
    x = x * key[0]
    x = x + key[3]
    cipherText.append(x)
print("Here's your ciphertext!")
print(cipherText)
