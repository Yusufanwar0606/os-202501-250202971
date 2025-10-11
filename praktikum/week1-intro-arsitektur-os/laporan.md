
# Laporan Praktikum Minggu 1.
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Yusuf Anwar  
- **NIM**   : 250202971  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Mahasiswa mampu :
- Memahami Konsep Dasar Arsitektur OS
- Mempersiapkan Pemecahan Masalah Sistem
- Mendorong Pemikiran Kritis
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
1. Sebutkan tiga fungsi utama sistem operasi. 
   **Jawaban:** fungsi utamanya adalah mengatur eksekusi ,penjadwalan proses,mengalokasikan, melindungi ruang memori,mengontrol akses ke perangkat hardware.
2. Jelaskan perbedaan antara kernel mode dan user mode. 
   **Jawaban:**  Kernel Mode adalah akses penuh ke hardware (privileged), hanya untuk kernel OS. sedangkan User Mode adalah akses terbatas (non-privileged) untuk aplikasi; akses hardware via system call.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. 
   **Jawaban:**  Monolithic: Linux, Unix .
Microkernel: Minix, QNX.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  **Jawaban:** mengirimkan tugas menggunakan git dan vs studio karena blm paham  
- Bagaimana cara Anda mengatasinya?
  **Jawaban:** mencari panduan di youtube agar bisa paham menggunakannya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
