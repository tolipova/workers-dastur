ishchilar=[]

while True:
    ism = input("Ishchining ismini kiriting: ") 
    if ism.lower() == 'exit':
        break
ishga_kirish_vaqti={}    

while len(ishchilar)>0:
    ishchilar_ismi = ishchilar.pop(0) #ruyxatni boshidan ma'lumot oladi
    vaqt = float(input(f"{ishchilar_ismi} ishga kelgan vaqtini kirit: "))
    ishga_kirish_vaqti[ishchilar_ismi] = vaqt
print("\n ishga kelgan vaqtlar")    
for ism,vaqt in ishga_kirish_vaqti.items():
    print(f"{ism}:{vaqt}")
kechikkanlar=[]
for ism,vaqt in ishga_kirish_vaqti.items() :
    if int(vaqt)  >= 9:
        kechikkanlar.append(ism)
print("\n 9dan keyin kelganlar")
for ism in kechikkanlar  :
    print(ism)

vaqtida_kelganlar=list(ishga_kirish_vaqti.keys())
print("\n vaqtida kelganlar: ")
for ism in vaqtida_kelganlar:
    print(f"{ism}:{vaqt}")
