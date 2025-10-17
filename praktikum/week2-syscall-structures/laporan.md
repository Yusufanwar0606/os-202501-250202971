
# Laporan Praktikum Minggu [X]
**Topik: struktur system call dan fungsi Kernel**

---

## Identitas
- **Nama**  : Yusuf Anwar  
- **NIM**   : 250202971 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
---

## Dasar Teori

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
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
1. hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.
![Screenshot hasil](screenshots/example.png)
2. diagram alur system call 
![Screenshot hasil](screenshots/example.png)
3. - System call merupakan jembatan penting antara program aplikasi di mode user dan kernel di mode kernel dalam sistem operasi Linux. Konsep system call memungkinkan aplikasi untuk meminta layanan kernel, seperti akses file, manajemen proses, atau interaksi perangkat keras, tanpa langsung mengaksesnya. Hal ini penting untuk keamanan OS karena system call mencegah program user dari akses langsung ke resource sensitif, yang bisa menyebabkan kerusakan atau serangan. Misalnya, jika program user bisa langsung memanipulasi memori kernel, itu bisa memicu crash sistem atau eksploitasi seperti buffer overflow. Oleh karena itu, system call bertindak sebagai lapisan proteksi, di mana kernel memvalidasi setiap permintaan sebelum dieksekusi.

   - OS memastikan transisi user-kernel berjalan aman melalui mekanisme seperti trap instruction (misalnya, syscall pada x86). Saat program user memanggil system call, CPU beralih dari mode user ke mode kernel, menyimpan konteks user, dan menjalankan kode kernel yang sesuai. Kernel kemudian memeriksa izin (seperti user ID atau capability), memproses permintaan, dan mengembalikan hasil tanpa mengungkap detail internal. Ini dilakukan dengan bantuan ring gate atau software interrupt, yang mencegah akses ilegal. Contohnya, system call seperti open(2) memerlukan parameter seperti path dan flag, yang divalidasi oleh kernel untuk menghindari akses file unauthorized.

   - Beberapa contoh system call yang sering digunakan di Linux termasuk:
     File I/O: open(2), read(2), write(2), untuk mengelola file secara aman.
     Process Management: fork(2), execve(2), untuk membuat dan menjalankan proses baru.
     Device Communication: ioctl(2), untuk berinteraksi dengan perangkat seperti USB.
     Inter-Process Communication: socket(2), untuk jaringan.
     Dengan demikian, system call tidak hanya meningkatkan keamanan dengan membatasi akses, tetapi juga memastikan efisiensi dan stabilitas OS. Tanpa system call, OS akan rentan terhadap error dan serangan, sehingga konsep ini menjadi fondasi utama dalam desain sistem operasi modern seperti Linux.


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
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
