
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
![alt text](<screenshots/Screenshot 2025-10-11 200914.png>)

---

## Analisis
1. Jelaskan makna hasil percobaan.
  **Jawaban:** makna dari :
   - uname -a yaitu menunjukkan identitas lengkap sistem kernel Linux, mencerminkan "siapa" dan "bagaimana" OS berjalan, seperti versi inti yang menentukan fitur dan kompatibilitas
   - lsmod | head yaitu mewakili "ekstensi hidup" kernel, di mana modul adalah bagian modular yang dimuat untuk fungsi tambahan, menandakan fleksibilitas arsitektur monolithic/modular.
   - dmesg | head yaitu rekaman komunikasi internal dengan hardware dan proses, mengungkap dinamika boot dan runtime untuk diagnosis mendalam.
  
2. Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
   **Jawaban:**
   - Fungsi Kernel: Hasil seperti scheduling proses mencerminkan manajemen CPU/memori/I/O kernel untuk efisiensi dan isolasi, sesuai teori multitasking aman.
   - System Call: Pemanggilan (e.g., fork()) menunjukkan transisi user-to-kernel mode via syscall table, validasi teori akses privileged resources dengan overhead minimal.
   - Arsitektur OS: Hasil performa tinggi di monolithic (Linux) vs modular di microkernel (Minix) mengilustrasikan trade-off teori: kecepatan vs keandalan.
3. Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  **Jawaban:**
   - Arsitektur: Linux (monolithic modular) hasil cepat/low-overhead sedangkan Windows (hybrid) lebih kompleks dengan overhead tinggi.
   - System Call: Linux (POSIX, strace mudah) sedangkan Windows (Win32 API, tersembunyi di ntdll, tracing sulit).
   - Performa/Keamanan: Linux konsisten untuk server, fleksibel modifikasi sedangkan Windows stabil desktop, ketat keamanan tapi closed-source.
   - Tools: Linux (source terbuka, compile mudah) sedangkan Windows (WDK/WSL terbatas, proprietary). Linux lebih cocok praktikum akademik.
---

## Kesimpulan
   - OS berfungsi sebagai perantara antara user/aplikasi (user mode, terbatas) dengan hardware (via kernel mode, privilese penuh), menggunakan system call sebagai mekanisme transisi aman. Komponen utama seperti kernel, device driver, dan file system memastikan efisiensi dan proteksi, seperti terlihat di eksperimen Linux (uname -a, lsmod, dmesg) yang menampilkan modul kernel dinamis.

   - Monolithic kernel (Linux, Windows) efisien dan cepat tapi rentan bug; layered approach (THE OS) lebih terstruktur dengan overhead; microkernel (Minix, QNX) modular dan aman tapi lambat. Untuk sistem modern, monolithic hybrid seperti Linux paling relevan karena seimbang performa, skalabilitas (server/cloud), dan adaptasi hardware.

   - Praktikum ini menekankan evolusi OS untuk komputasi distributed, dengan diagram User → System Call → Kernel → Hardware sebagai visualisasi sederhana. Hasil eksperimen memperkuat bahwa OS seperti Linux mendukung kebutuhan sehari-hari sambil prioritaskan isolasi dan keamanan.

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
