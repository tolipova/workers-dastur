ishchilar = []

while True:
    ism = input("Ishchining ismini kiriting: ") 
    if ism.lower() == 'exit':
        break
    if ism not in ishchilar:
        ishchilar.append(ism)
        print(f"{ism} ishga qushildi")
    else:
        print(f"{ism} bu ismli ishchi ruyxatga kiritilgan")    

vaqtida_kelganlar=[]
kechikkanlar=[]

for ism in ishchilar:
    ishga_keldimi=input(f"{ism} ishga keldimi yoki kechikdimi? (ha/yoq): ")
    if ishga_keldimi.lower() == 'ha':
        vaqtida_kelganlar.append(ism)
    else:
        kechikkanlar.append(ism)
ajratib_olish = input("Vaqtida kelganlar va kechikkanlarni ajratib olishni xohlaysiz? (ha/yoq): ")        
if ajratib_olish.lower() == 'ha':
    vaqtida_kelganlar= [
        ism for ism in vaqtida_kelganlar if ism !='9'
    ]
print("Ishchilar ruyxati: ")    
print(ishchilar)    

print("Ishga vaqtida kelganlar ruyxati:")
print(vaqtida_kelganlar)

print("Kechikkanlar ruyxati:")
print(kechikkanlar)