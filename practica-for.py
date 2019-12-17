print("aprendiendo con for")
miEmail=input("por favor ingresa tu email: ")
email=False
for i in miEmail:
    if (i=="@") or (i=="."):
        email=True
if email==True:
    print("email es correcto")
    for j in range(10):
        print(miEmail)
else:
    print("no es correcto")