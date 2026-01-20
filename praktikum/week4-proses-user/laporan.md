
# Laporan Praktikum Minggu [3]
Topik: Manajemen Proses dan User di Linux  

---

## Identitas
- **Nama**  : Yusuf Anwar
- **NIM**   : 250202971
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem. 

---

## Dasar Teori
1. Konsep Proses dalam Sistem Operasi
Proses adalah program yang sedang dieksekusi, dikelola oleh kernel Linux. Setiap proses memiliki PID (Process ID) unik, status (running, sleeping, dll.), dan sumber daya seperti CPU, memori, dan file descriptor.
Hierarki proses: Dimulai dari proses induk (parent) seperti init atau systemd (PID 1), yang melahirkan proses anak (child). Ini memungkinkan kontrol paralel dan isolasi, mencegah satu proses mengganggu yang lain.
Teori dasar: Berdasarkan model proses Unix, di mana fork() membuat child process, dan exec() mengganti image proses. Kernel menggunakan scheduler untuk alokasi CPU.

2. Manajemen User dan Hak Akses
User adalah entitas yang berinteraksi dengan sistem, diidentifikasi oleh UID (User ID) dan GID (Group ID). User root (UID 0) memiliki hak penuh, sementara user biasa dibatasi oleh izin file (rwx untuk read/write/execute).
Grup: Mekanisme untuk berbagi akses antar user, seperti grup sudo untuk perintah administratif. Prinsip "least privilege" memastikan user hanya akses yang diperlukan.
Teori dasar: Berdasarkan model keamanan DAC (Discretionary Access Control), di mana owner file mengontrol akses. Linux menggunakan /etc/passwd dan /etc/group untuk penyimpanan data user.

3. Monitoring dan Kontrol Proses
Monitoring: Menggunakan perintah seperti ps (snapshot statis) dan top (real-time) untuk melihat status proses, termasuk penggunaan sumber daya. Ini membantu debugging dan optimasi performa.
Kontrol: Melalui sinyal (signals) seperti SIGTERM (terminate) atau SIGKILL (force kill), dikirim oleh kill. Kernel menangani sinyal untuk mengubah status proses.
Teori dasar: Berdasarkan konsep inter-process communication (IPC) dan scheduling. Kernel Linux (misal, CFS scheduler) mengalokasikan CPU berdasarkan prioritas.

4. Hubungan dengan Keamanan Sistem
Manajemen user mencegah privilege escalation (peningkatan hak akses ilegal), sementara kontrol proses menghentikan malware atau proses berbahaya.
Teori dasar: Mengikuti prinsip security by design, dengan isolasi proses melalui namespaces dan cgroups (di systemd). Audit log (misal, via journald) memungkinkan tracking aktivitas.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   whoami
   id
   groups
 ```
```bash
     sudo adduser praktikan
     sudo passwd praktikan
```

```bash
   ps aux | head -10
   top -n 1
```
```bash
     sleep 1000 &
     ps aux | grep sleep
```

```bash
     kill <PID>
```

 ```bash
   pstree -p | head -20
   ```

---

## Hasil Eksekusi
![Screenshot hasil](screenshots/userlinux.png)

![Screenshot hasil](screenshots/userlinux1.png)

![Screenshot hasil](screenshots/userlinux2.png)

![Screenshot hasil](screenshots/userlinux3.png)

![Screenshot hasil](screenshots/userlinux4.png)

---

## Analisis
1.  hierarki proses dalam bentuk diagram pohon (pstree) di laporan.
   
    ``` bash
    systemd(1)-+-agetty(241)
               |-agetty(244)
               |-cron(192)
               |-dbus-daemon(196)
               |-init-systemd(Ub(2)-+-SessionLeader(150)---Relay(180)(158)---bash(180)-+-head(445)
               |                    |                                                  `-pstree(444)
               |                    |-init(7)---{init}(8)
               |                    |-login(181)---bash(369)
               |                    `-{init-systemd(Ub}(9)
               |-networkd-dispat(208)
               |-rsyslogd(210)-+-{rsyslogd}(228)
               |               |-{rsyslogd}(230)
               |               `-{rsyslogd}(231)
               |-systemd(349)---(sd-pam)(352)
               |-systemd-journal(82)
               |-systemd-logind(223)
               |-systemd-resolve(114)
               |-systemd-timesyn(115)---{systemd-timesyn}(177)
               |-systemd-udevd(111)
               `-unattended-upgr(250)---{unattended-upgr}(286)
    
    ```
2. **Hubungan antara User Management dan Keamanan Sistem Linux:** Manajemen user di Linux melibatkan pembuatan user, pengaturan password, dan penugasan grup untuk membatasi akses. User `root` memiliki hak penuh, sementara user biasa hanya dapat mengakses file mereka sendiri. Ini mencegah kerusakan sistem oleh malware atau kesalahan user. Grup memungkinkan kontrol akses bersama (misal, grup `sudo` untuk perintah administratif). Dengan demikian, manajemen user menjaga prinsip "least privilege" untuk keamanan, mencegah eskalasi hak akses, dan memungkinkan audit aktivitas.

---

## Kesimpulan
- Praktikum ini memberikan pemahaman mendalam tentang manajemen proses di Linux, termasuk monitoring dengan perintah seperti `ps` dan `top`, serta kontrol proses menggunakan `kill` berdasarkan PID.
- Konsep manajemen user, seperti identifikasi dengan `id` dan pembuatan user baru dengan `adduser`, menekankan pentingnya pengaturan hak akses untuk membatasi penggunaan sistem.
- Secara keseluruhan, praktikum ini menunjukkan hubungan erat antara manajemen user dan keamanan sistem Linux, dengan semua langkah eksperimen berhasil diselesaikan dan didokumentasikan.

---

## Quiz
1. **Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?**  
    **Jawaban:**  
Proses `init` (atau `systemd` di sistem modern) adalah proses pertama yang dijalankan setelah booting kernel. Ia bertanggung jawab atas inisialisasi sistem, peluncuran layanan, dan pengelolaan proses anak. `systemd` juga mengelola startup paralel dan pemulihan layanan.

2. **Apa perbedaan antara `kill` dan `killall`?**  
   **Jawaban:**  
`kill` mengirim sinyal ke proses berdasarkan PID (Process ID) spesifik. `killall` mengirim sinyal ke semua proses yang cocok dengan nama perintah, tanpa perlu PID. `killall` lebih mudah untuk menghentikan multiple instance, tetapi berpotensi berbahaya jika nama proses umum.

3. **Mengapa user `root` memiliki hak istimewa di sistem Linux?**  
    **Jawaban:**  
User `root` adalah superuser dengan UID 0, yang memberikan akses penuh ke semua file, perintah, dan konfigurasi sistem. Ini memungkinkan administrasi penuh, tetapi juga berisiko tinggi jika disalahgunakan, sehingga penggunaan sudo direkomendasikan untuk tugas administratif.
  
---

## Refleksi Diri
Apa bagian yang paling menantang minggu ini?
Bagian yang paling menantang adalah menganalisis hierarki proses dengan pstree dan menggambarkannya dalam diagram pohon, karena outputnya kompleks dan sulit dipahami tanpa visualisasi yang jelas, terutama dalam lingkungan WSL yang berbeda dari Linux native.

Bagaimana cara Anda mengatasinya?
Saya mengatasinya dengan mempelajari output pstree langkah demi langkah, menggunakan kode Mermaid untuk membuat diagram visual, dan merujuk pada dokumentasi Linux serta referensi buku untuk memahami konsep PID dan parent-child relationship. Selain itu, saya bereksperimen ulang di terminal untuk memverifikasi hasil.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
