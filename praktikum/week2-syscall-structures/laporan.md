
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
- System Call sebagai Antarmuka Aman: System call adalah mekanisme utama untuk interaksi antara program aplikasi (mode user) dan kernel (mode kernel), memungkinkan akses terkontrol ke resource sistem seperti file dan hardware, sambil mencegah akses langsung yang berisiko keamanan.
- Fungsi Kernel dalam Sistem Operasi: Kernel bertindak sebagai inti OS yang menangani tugas kritis seperti manajemen memori, proses, dan I/O, memastikan stabilitas dan isolasi melalui mode privileged, dengan arsitektur seperti monolitik di Linux.
- Alur Eksekusi System Call: Proses dimulai dari panggilan user, transisi ke kernel via trap instruction (e.g., syscall), validasi izin, eksekusi fungsi kernel, dan pengembalian hasil, didukung oleh context switch untuk keamanan.
- Jenis System Call Utama: Termasuk file management (e.g., open, read), process management (e.g., fork, execve), device management (e.g., ioctl), dan inter-process communication (e.g., socket), yang relevan dengan eksperimen strace.
- Hubungan dengan Eksperimen: Teori ini mendasari observasi di strace dan dmesg, di mana system call divisualisasikan sebagai transisi aman, menunjukkan peran kernel dalam mengelola operasi low-level untuk keamanan OS.

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

##  hasil eksperimen :
![alt text](screenshots/strace.png)
![alt text](screenshots/dmesg.png)


---

## Analisis
1. Hasil eksperimen ```strace``` dan ```dmesg``` dalam bentuk tabel observasi
   
| Nama User       | Deskripsi                                                                 | Fungsi                                                                 |
|-----------------|---------------------------------------------------------------------------|------------------------------------------------------------------------|
| read            | User untuk operasi baca (read) file; sering terkait dengan akses baca sistem. | Mengelola izin baca untuk file dan direktori, memastikan keamanan akses data tanpa modifikasi. |
| write           | User untuk operasi tulis (write) file; terkait dengan akses tulis.       | Mengontrol izin tulis untuk file, mencegah perubahan tidak sah pada data sistem. |
| daemon          | User standar untuk menjalankan daemon (proses latar belakang) sistem.     | Menjalankan layanan sistem seperti cron atau syslog tanpa akses root, meningkatkan keamanan. |
| bin             | User untuk binary executables (program sistem).                          | Mengelola akses ke direktori /bin, tempat executable dasar seperti ls atau cat disimpan. |
| sys             | User untuk sistem operasi dan komponen inti.                             | Mengontrol akses ke resource sistem seperti /sys, untuk operasi kernel dan hardware. |
| sync            | User untuk sinkronisasi data (sync operations).                          | Menjalankan perintah sync untuk memastikan data ditulis ke disk, mencegah kehilangan data. |
| games           | User untuk aplikasi game dan hiburan.                                     | Mengelola akses ke direktori /usr/games, membatasi game agar tidak mengganggu sistem utama. |
| man             | User untuk manual pages (dokumentasi sistem).                             | Mengontrol akses ke /usr/share/man, tempat halaman manual seperti man syscalls disimpan. |
| lp              | User untuk line printer (printer).                                        | Mengelola layanan printing, seperti CUPS, untuk akses aman ke perangkat printer. |
| mail            | User untuk sistem email (mail).                                           | Mengontrol akses ke layanan email seperti sendmail atau postfix, untuk pengiriman pesan. |
| news            | User untuk news server (berita).                                          | Mengelola akses ke layanan news seperti NNTP, untuk distribusi berita atau RSS. |
| uucp            | User untuk Unix-to-Unix Copy Protocol (UUCP).                             | Mengontrol transfer file antar sistem Unix, sering digunakan untuk jaringan lama. |
| proxy           | User untuk proxy server.                                                  | Mengelola akses ke layanan proxy seperti Squid, untuk caching dan filtering web. |
| www-data        | User untuk web server (seperti Apache atau Nginx).                        | Mengontrol akses ke direktori web (/var/www), memastikan keamanan situs web. |
| backup          | User untuk operasi backup.                                                | Mengelola akses ke tools backup seperti rsync atau tar, untuk penyimpanan data. |
| list            | User untuk mailing list.                                                  | Mengontrol akses ke layanan mailing list seperti Mailman, untuk distribusi email grup. |
| irc             | User untuk Internet Relay Chat (IRC).                                     | Mengelola akses ke server IRC, untuk komunikasi real-time. |
| gnats           | User untuk GNU Bug Tracking System.                                       | Mengontrol akses ke sistem pelacakan bug, untuk pengelolaan laporan error. |
| nobody          | User anonim atau tanpa hak istimewa (nobody).                             | Digunakan untuk proses yang tidak memerlukan akses spesifik, meningkatkan keamanan. |
| systemd-network | User untuk systemd network management.                                    | Mengelola layanan jaringan systemd, seperti konfigurasi IP dan DNS. |
| systemd-resolve | User untuk systemd DNS resolver.                                          | Mengontrol resolusi DNS melalui systemd-resolved, untuk lookup domain. |
| messagebus      | User untuk D-Bus message bus.                                             | Mengelola komunikasi antar-proses via D-Bus, untuk integrasi aplikasi. |
| systemd-timesync| User untuk systemd time synchronization.                                  | Mengontrol sinkronisasi waktu melalui systemd-timesyncd, untuk NTP. |
| syslog          | User untuk sistem logging (syslog).                                       | Mengelola akses ke layanan logging seperti rsyslog, untuk pencatatan event sistem. |
| _apt            | User untuk APT package manager.                                           | Mengontrol akses ke operasi package management, seperti update dan install. |
| uuidd           | User untuk UUID daemon.                                                   | Mengelola pembuatan UUID unik untuk sistem, digunakan dalam database atau file. |
| tcpdump         | User untuk packet analyzer (tcpdump).                                     | Mengontrol akses ke tools analisis jaringan, untuk monitoring paket. |
| landscape       | User untuk Canonical Landscape (management tool).                         | Mengelola akses ke layanan monitoring dan manajemen sistem dari Canonical. |

2. ![alt text](screenshots/systemcall.png)


3. analisis: Pentingnya System Call untuk Keamanan OS dan Interaksi Kernel
   - System call merupakan jembatan penting antara program aplikasi di mode user dan kernel di mode kernel dalam sistem operasi Linux. Konsep system call memungkinkan aplikasi untuk meminta layanan kernel, seperti akses file, manajemen proses, atau interaksi perangkat keras, tanpa langsung mengaksesnya. Hal ini penting untuk keamanan OS karena system call mencegah program user dari akses langsung ke resource sensitif, yang bisa menyebabkan kerusakan atau serangan. Misalnya, jika program user bisa langsung memanipulasi memori kernel, itu bisa memicu crash sistem atau eksploitasi seperti buffer overflow. Oleh karena itu, system call bertindak sebagai lapisan proteksi, di mana kernel memvalidasi setiap permintaan sebelum dieksekusi.

   - OS memastikan transisi user-kernel berjalan aman melalui mekanisme seperti trap instruction (misalnya, syscall pada x86). Saat program user memanggil system call, CPU beralih dari mode user ke mode kernel, menyimpan konteks user, dan menjalankan kode kernel yang sesuai. Kernel kemudian memeriksa izin (seperti user ID atau capability), memproses permintaan, dan mengembalikan hasil tanpa mengungkap detail internal. Ini dilakukan dengan bantuan ring gate atau software interrupt, yang mencegah akses ilegal. Contohnya, system call seperti open(2) memerlukan parameter seperti path dan flag, yang divalidasi oleh kernel untuk menghindari akses file unauthorized.

   - Beberapa contoh system call yang sering digunakan di Linux termasuk:
     File I/O: open(2), read(2), write(2), untuk mengelola file secara aman.
     Process Management: fork(2), execve(2), untuk membuat dan menjalankan proses baru.
     Device Communication: ioctl(2), untuk berinteraksi dengan perangkat seperti USB.
     Inter-Process Communication: socket(2), untuk jaringan.
     Dengan demikian, system call tidak hanya meningkatkan keamanan dengan membatasi akses, tetapi juga memastikan efisiensi dan stabilitas OS. Tanpa system call, OS akan rentan terhadap error dan serangan, sehingga konsep ini menjadi fondasi utama dalam desain sistem operasi modern seperti Linux.

---

## Kesimpulan
- Pentingnya System Call dalam Sistem Operasi: System call berfungsi sebagai antarmuka aman antara program user dan kernel, memastikan akses terkontrol ke resource seperti file, proses, dan hardware. Praktikum ini menunjukkan bahwa tanpa system call, OS rentan terhadap risiko keamanan, dan pemahaman alur eksekusinya (dari user mode ke kernel mode) adalah kunci untuk pengembangan software yang stabil.

- Keterampilan Praktis yang Diperoleh: Melalui eksperimen seperti menggunakan strace dan dmesg, saya belajar menganalisis system call secara langsung, mengidentifikasi jenisnya (e.g., file I/O, process management), dan membuat diagram alur untuk visualisasi. Hal ini meningkatkan kemampuan debugging dan pemahaman interaksi kernel di lingkungan Linux.

- Aplikasi di Masa Depan: Praktikum ini menekankan bahwa konsep system call relevan untuk memastikan keamanan dan efisiensi OS, yang bisa diterapkan dalam pengembangan aplikasi, troubleshooting sistem, atau studi lanjut tentang kernel. Secara keseluruhan, ini memperkuat dasar pengetahuan saya tentang operasi sistem modern.
  
---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi? 

   **Jawaban:**  Fungsi utama system call adalah menyediakan antarmuka aman antara program aplikasi (mode user) dan kernel (mode kernel). System call memungkinkan aplikasi untuk meminta layanan seperti akses hardware, manajemen memori, atau I/O tanpa langsung mengakses resource sistem, sehingga menjaga integritas dan keamanan OS.
2. Sebutkan 4 kategori system call yang umum digunakan. 

   **Jawaban:**  
   - File Management: Seperti open(2), read(2), write(2), untuk operasi file dan direktori.
   - Process Management: Seperti fork(2), execve(2), wait(2), untuk membuat, mengelola, dan menghentikan proses.
   - Device Management: Seperti ioctl(2), untuk berinteraksi dengan perangkat keras seperti disk atau jaringan.
   - Inter-Process Communication: Seperti socket(2), pipe(2), untuk komunikasi antar-proses atau jaringan.
3. Mengapa system call tidak bisa dipanggil langsung oleh user program? 
   **Jawaban:**  System call tidak bisa dipanggil langsung karena program user berjalan di mode user, yang memiliki akses terbatas untuk mencegah kerusakan sistem. Untuk memanggil system call, program harus menggunakan instruksi khusus seperti syscall atau interrupt, yang memicu CPU untuk beralih ke mode kernel. Ini memastikan kernel dapat memvalidasi permintaan terlebih dahulu, sehingga mencegah akses ilegal dan menjaga keamanan.



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
**jawaban:** Saya juga kesulitan menganalisis output strace untuk mengidentifikasi system call spesifik, karena outputnya sangat detail dan memerlukan pemahaman konsep dasar kernel.
  
- Bagaimana cara Anda mengatasinya?  
**Jawaban:** saya mempraktikkan perintah berulang kali (e.g., strace ls) dan mencatat 5–10 system call pertama dalam tabel, sambil membandingkannya dengan buku Operating System Concepts untuk penjelasan fungsi masing-masing.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
