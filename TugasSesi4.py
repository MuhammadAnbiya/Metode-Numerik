"""
Sebuah perusahaan teknologi sedang mengembangkan sensor untuk mendeteksi perubahan suhu dalam
ruang tertutup. Berdasarkan penelitian, perubahan suhu terhadap waktu dapat dimodelkan dengan fungsi
non-linear sebagai berikut: 
f(x) = 4x3 - 6x2 + 7x - 2
"""

def f(x):
    return 4*x**3 - 6*x**2 + 7*x - 2

"""
Dimana x adalah waktu dalam satuan jam, dan f(x) adalah perubahan suhu yang terukur dalam derajat
Celsius. Perusahaan ingin mengetahui pada waktu kapan perubahan suhu mencapai 0 derajat Celsius, atau
dengan kata lain, mereka ingin menemukan akar dari persamaan non-linear tersebut dengan tebakan interval
awal di [0, 5].
"""

def biseksi(a, b, tol, max_iter=1000):
    """
    a, b = toleransi interval perncarian.
    tol = toleransi error 
    max_iter = maksimum iterasi
    """

    # megecek apakah ada akar dalam interval a, b
    if f(a) * f(b) > 0:
        print("Tidak ada akar dalam interval ini!")
        return None
    
    iteration = 0
    

    while (abs(b - a) >= tol and iteration < max_iter):
        # itung titik tengah
        c = (a + b) / 2
        
        # Hitung nilai fungsi pada titik tengah
        fc = f(c)
        
        print(f"Iterasi {iteration + 1}:")
        print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}") # print hanya untuk 6 angka di belakang koma
        print(f"f(c) = {fc:.6f}")
        print("------------------------")
        
        # mengecek apakah c masih dibawah batas toleransi
        if abs(fc) < tol:
            return c
        
        # kalau a * b masih kurang dari 0 maka nilai b diganti dengan c
        if f(a) * fc < 0:
            b = c

        # jika tidak kurang dari nol maka nilai a diganti dengan c
        else:
            a = c
            
        iteration += 1
    return (a + b) / 2, iteration

# Mencoba sesuai contoh soal
a = 0  
b = 5
toleransi = 0.001 
max_iterasi = 100  

akar, iteration = biseksi(a, b, toleransi, max_iterasi)

if akar is not None:
    print(f"\nAkar yang ditemukan: {akar:.6f}")
    print(f"Nilai f(x) pada akar: {f(akar):.6f}")
    print(f"Maka perubahan suhu mencapai 0 derajat Celcius pada waktu sekitar : {akar:.3f} jam, pada iterasi ke-{iteration}")
