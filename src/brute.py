import time

# Mencari index huruf pada table of unique letter
def search_index(char, arr):
    for i in range(len(arr)):
        if char == arr[i]:
            return i

# Fungsi permutasi
def permut(l):
    # Basis rekurens saat elemen list hanya ada 1
    if len(l) == 1:
        return [l]
    
    permlist = []

    # Iterasi input l (list) dan menghitung permutasinya
    for i in range(len(l)):
        x = l[i]

        # Sisa list setelah l[i] diambil dari list
        sisa = l[:i] + l[i+1:]

        # Menghasilkan semua kemungkinan permutasi di mana
        # m adalah elemen pertama
        for j in permut(sisa):
            permlist.append([x] + j)
    return permlist

# Deklarasi array
wordlist = []
charlist = []
numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Memasukkan input kata-kata dalam array of sentences
while True:
    print("Silakan input nama file!")
    print("Contoh: input.txt")
    filename = "../test/" + input("Nama file: ")
    try:
        f = open(filename)
        break
    except:
        print("File tidak ditemukan!")
        continue
start_time = time.time() # Memulai perhitungan waktu eksekusi program
lines = f.read().splitlines()
for line in lines:
    if line[-1] == '+':
        wordlist.append(line[:-1])
        wordlist.append(lines[-1])
        break
    wordlist.append(line)
    
# Memasukkan huruf-huruf unik pada charlist
for word in wordlist:
    for x in word:
        if x in charlist:
            continue
        charlist.append(x)
print(charlist)

# Membuat list permutasi
perms = permut(numlist)
count = 0 # Deklarasi awal jumlah percobaan saat brute force nanti


for perm in perms:
    count += 1

    # Membuat list of string kosong untuk hasil konversi char ke integer
    results = ['' for i in wordlist]

    for i in range(len(wordlist)):
        word = wordlist[i]
        # Konversi dari kata menjadi angka
        for char in word:
            idx = search_index(char, charlist)
            if results[i] == '' and perm[idx] == '0': # Tidak menerima 0 di awal
                break
            results[i] = results[i] + str(perm[idx])
        if results[i] == '':
            break
    
    if '' in results:
        continue

    sum = 0
    for result in results[:-1]:
        sum += int(result)
    
    if sum == int(results[-1]):
        print(perm[:len(charlist)])
        for word in wordlist[:-1]:
            print('\n' + '{:>7}'.format(word), end='')
        print('+')
        print("-------")
        print('{:>7}'.format(wordlist[-1]))
        for result in results[:-1]:
            print('\n' + '{:>7}'.format(result), end='')
        print('+')
        print("-------")
        print('{:>7}'.format(results[-1]))
        print("\n--- Total tes: ", count, "---")
        print("--- %s detik ---" % (time.time() - start_time))
        break