import numpy as np
import pandas as pd

# 1. Membuat array 10.000 x 10.000 dengan angka acak (0 sampai 100)
print("Sedang membuat array... Mohon tunggu.")
data = np.random.randint(0, 100, size=(10000, 10000), dtype=np.int32)

# 2. Print informasi array
print("\nInformasi Array:")
print(f"Dimensi: {data.shape}")
print(f"Total elemen: {data.size}")
print("\nCuplikan isi data (ujung kiri atas):")
print(data[:10, :10])  # Mencetak 5 baris dan 5 kolom pertama

# 3. Simpan ke CSV
# Menggunakan Pandas karena lebih cepat dan efisien dalam menulis file CSV besar
print("\nSedang menyimpan ke file 'data_besar.csv'...")
df = pd.DataFrame(data)
df.to_csv("data_besar.csv", index=False, header=False)

print("Proses selesai! File berhasil disimpan.")