#Andreas Nugroho
#71200646

#Andi sedang mengerjakan tugas matematika, andi memiliki kesulitan untuk menghitung. Andi memerlukan kalkulator sederhana untuk menghitung. 
#buatlah kalkulator sederhana untuk membantu Andi dalam mengerjakan matematika

#input 
#pilihan dari user
#angka pertama 
#angka kedua

#proses
#Penambahan (+)
#pengurangan (-)
#perkalian (*)
#pembagian (/)

#output
#hasil

def tambah (x,y):
    return x + y
def kurang (x,y):
    return x - y
def kali (x,y):
    return x * y
def bagi (x,y):
    return x / y

print("="*5, "Kalkulator Sederhana","="*5)
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:

    pilih = input("Masukkan Pilihan Anda (1,2,3,4) : ")

    if pilih in ('1','2','3','4'):
        angka1 = float(input("Masukkan Angka Pertama : "))
        angka2 = float(input("Masukkan Angka Kedua : "))

        if pilih == '1':
            print(angka1, "+",angka2, "=",tambah(angka1,angka2))
        elif pilih == '2':
            print(angka1, "-",angka2,"=",kurang(angka1,angka2))
        elif pilih == '3':
            print(angka1,"*",angka2,"=",kali(angka1,angka2))
        elif pilih == '4':
            print(angka1,"/",angka2,"=",bagi(angka1,angka2))
        break
    else:
        print("Inputan Tidak Ada!")
        

