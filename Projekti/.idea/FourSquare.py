import string
from more_itertools import unique_everseen
import numpy as np

class Matrix:
    UL=[]

    UR=[]

    DL=[]

    DR=[]


    def __init__(self,keyword1,keyword2):
        self.UR=self.createMatrix(keyword1)
        self.DL=self.createMatrix(keyword2)
        self.UL=self.createMatrix()
        self.DR=self.createMatrix()

    def createMatrix(self,keyword=None):
        if keyword:
            keywordNR = ''.join(unique_everseen(keyword))
            matrix = np.empty((5, 5), dtype='U1')
            alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
            temp=0
            for (i, j), value in np.ndenumerate(matrix):
                if(temp<len(keywordNR)):
                    matrix[i,j]=keywordNR[5*i+j].upper()
                    alphabet = "x" + alphabet
                    alphabet = alphabet.replace(keywordNR[5*i+j].upper(),'')
                    temp+=1
                else:
                    matrix[i,j]=alphabet[5*i+j]
            return matrix
        else:
            matrix = np.empty((5, 5), dtype='U1')
            alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
            for (i, j), value in np.ndenumerate(matrix):
                matrix[i,j]=alphabet[5*i+j]
            return matrix

def Encrypt(matrixes,message):
    if (len(message)%2!=0):
        message+='x'
    encryptedMessage=''
    i1,i2,j1,j2 = 0,0,0,0
    for k in range(0, len(message),2):
        for (i,j),value in np.ndenumerate(matrixes.UL):
            if(matrixes.UL[i,j] == message.upper()[k]):
                i1=i
                j1=j
            if(matrixes.DR[i,j] == message.upper()[k+1]):
                i2=i
                j2=j
        encryptedMessage+=matrixes.UR[i1][j2]+matrixes.DL[i2][j1]
    return encryptedMessage

def Decrypt(matrixes,message):
    decryptedMessage=''
    i1,i2,j1,j2 = 0,0,0,0
    for k in range(0, len(message),2):
        for (i,j),value in np.ndenumerate(matrixes.UR):
            if(matrixes.UR[i,j] == message.upper()[k]):
                i1=i
                j1=j
            if(matrixes.DL[i,j] == message.upper()[k+1]):
                i2=i
                j2=j
        decryptedMessage+=matrixes.DR[i1][j2]+matrixes.UL[i2][j1]
    return decryptedMessage


matrixes = Matrix("secret","keyword")
message= "QlirimMatoshi"
encrypted = Encrypt(matrixes,message)
print("The encrypted message is: ",encrypted)
decrypted = Decrypt(matrixes,encrypted)
print("The encrypted message is: ",decrypted)

