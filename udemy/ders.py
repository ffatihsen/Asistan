#Bu fonksiyon dosyadaki tekrar eden isimleri siler.Temiz bir dosyaya tekrarsız şekilde yazar.
def kontrol():
    file = open("deneme2", "r")
    fileControl = open("deneme3", "w")
    deneme3 = []
    for line in file:
        if line not in deneme3:
            fileControl.write(line)
            deneme3.append(line)


#Bu fonksiyon dosyadaki karakterleri boşluk görene kadar yazar boşluktan sonrasını siler.
def temizlik():
    file2 = open("deneme2", "w")
    file =open("deneme","r")
    for line in file:
        for harf in line:
            if(harf!=" "):
                file2.write(harf)
            elif(harf==" "):
                file2.write("\n")
                break
    file2=open("deneme2","r")
    print(file2.read())

#Çalıştırmak istediğiniz fonksiyonu yorum satırından kaldırın.
#temizlik()
kontrol()


