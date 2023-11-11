import random
S=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
L=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
N=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SC=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
comb=S+L+N+SC
rS=random.choice(S)
rL=random.choice(L)
rN=random.choice(N)
rSC=random.choice(SC)

print(rS+rL+rSC+rN)
