
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Yusuf Anwar
- **NIM**   : 250202971
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2. Menggunakan chmod dan chown untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---

## Dasar Teori
1. Sistem File Linux: Linux menggunakan struktur file hierarki yang dimulai dari direktori root (/), dengan direktori seperti /home, /etc, dan /tmp. Navigasi dilakukan melalui perintah seperti pwd (menampilkan direktori kerja saat ini), ls (menampilkan isi direktori), cd (berpindah direktori), dan cat (membaca isi file), yang membantu pengguna memahami dan mengelola struktur file secara efisien.
2. Permission (Hak Akses): Setiap file dan direktori di Linux memiliki permission yang mengatur hak baca (read), tulis (write), dan eksekusi (execute) untuk pemilik (owner), grup (group), dan lainnya (others). Permission ditampilkan dalam format oktal atau simbolik (misalnya, rwxr-xr--), dan dikelola menggunakan perintah chmod untuk mengubah hak akses guna menjaga keamanan dan kontrol akses.
3. Ownership (Kepemilikan): File dan direktori dimiliki oleh user dan group tertentu, yang dapat diubah menggunakan perintah chown. Konsep ini penting untuk mengatur siapa yang dapat mengakses atau memodifikasi file, mendukung isolasi dan keamanan dalam sistem multi-user seperti Linux.
4. Keamanan Sistem: Permission dan ownership berperan krusial dalam keamanan Linux dengan mencegah akses tidak sah, seperti melalui pengaturan hak akses yang ketat (misalnya, chmod 600 untuk file pribadi). Ini mencegah risiko seperti modifikasi data oleh user yang tidak berwenang, sesuai dengan prinsip-prinsip keamanan dalam sistem operasi.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. **Apa fungsi dari perintah `chmod`?**  
   **Jawaban:** `chmod` digunakan untuk mengubah hak akses (permission) file atau direktori, seperti mengatur siapa yang bisa baca, tulis, atau eksekusi, dalam format oktal (misalnya 755) atau simbolik (misalnya u+rwx).
2. **Apa arti dari kode permission `rwxr-xr--`?**  
   **Jawaban:**  Ini berarti: owner memiliki baca, tulis, dan eksekusi (rwx); group memiliki baca dan eksekusi (r-x); others hanya memiliki baca (r--). Total 10 karakter, dengan karakter pertama menunjukkan tipe file (misalnya - untuk file biasa).
3. **Jelaskan perbedaan antara `chown` dan `chmod`.**
   **Jawaban:**  `chown` mengubah kepemilikan file (owner dan/atau group), sedangkan `chmod` mengubah hak akses (permission) seperti baca, tulis, atau eksekusi. `chown` fokus pada siapa yang memiliki file, sementara `chmod` fokus pada apa yang bisa dilakukan oleh pemilik, grup, atau orang lain.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
