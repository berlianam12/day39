print("1. Buat array berisi 50 angka random antara 0-100")
array_pertama = np.random.randint(0, 101, 50)
print(array_pertama)

mean = np.mean(array_pertama)
median = np.median(array_pertama)
std_dev = np.std(array_pertama)
print(f"\n2. Mean: {mean}, Median: {median}, Standard Deviasi: {std_dev}")

angka_diatas_rata2 = array_pertama[array_pertama > mean]
print(f"\n3. Angka yang lebih tinggi dari rata-rata: {angka_diatas_rata2}")

array_genap = array_pertama[array_pertama % 2 == 0]
print(f"\n4. Array baru yang mengandung angka genap: {array_genap}")

min_genap = np.min(array_genap)
max_genap = np.max(array_genap)
print(f"\n5. Minimum dari array genap: {min_genap}, Maksimum dari array genap: {max_genap}")

matrix_5x10 = array_pertama.reshape(5, 10)
print(f"\n6. Matrix 5x10:\n{matrix_5x10}")

matrix_transpose = np.transpose(matrix_5x10)
jumlah_per_baris = np.sum(matrix_transpose, axis=1)
print(f"\n7. Matrix transpose:\n{matrix_transpose}")
print(f"\nJumlah setiap baris dari matrix transpose: {jumlah_per_baris}")

print("\n8. Buat histogram sederhana dari array pertama:")
plt.hist(array_pertama, bins=10, edgecolor='black')
plt.title('Histogram of Array Pertama')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()