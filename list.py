invitation=['sita','maya','puja','foolmaya','sumitra','sunita','suman','sushila','sam','samiksha']
print(invitation)
print(sorted(invitation))
print(sorted(invitation,reverse=True))
print(sorted(invitation,key=len))
print(sorted(invitation,key=len,reverse=True))
print(sorted(invitation,key=lambda x:x[-1]))
print(sorted(invitation,key=lambda x:x[-1],reverse=True))
print(invitation)