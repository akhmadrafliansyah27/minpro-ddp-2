## Mini Project DDP 2
## Tema  : Pengelolaan Jadwal Matkul Prodi Sistem Informasi Kelas B
## Nama  : Akhmad Rafliansyah
## prodi : Sistem Informasi
## kelas : B
## NIM   : 2509116045


![Flowchart](minpro.drawio.png)

**penjelasan flowchart:**
1. Program di mulai dari **start**
2. user akan login dengan memasukan username dan password
3. jika username dan password salah maka user harus memasukan username dan password sampai benar. jika sudah benar maka user akan masuk role manager atau karyawan tergantung dari username dan pasword yang dimasukan
4. jika user masuk role manager maka akan di tampilkan menu khusus role manager yaitu **CREAT**, **READ**, **UPDATE**, **DELETE**, dan  **LOGOUT**.
5. Jika user memilih **CREAT** maka akan ada 2 pilihan yaitu ingin menambahkan data baru atau tidak. jika user memilih tidak maka user akan langsung menuju menu utama lagi. jika user memilih ingin menambahkan data baru maka user harus menginput **nama matkul, hari, jam, dan nama gedung**. setelah itu sistem akan menyimpan data ke dalam daftar dan akan mendapatkan pesan yaitu **"data berhasil di tambahkan"**. alur berlanjut user akan mendapatkan dua pilihan lagi yaitu ingin menambahkan data lagi atau tidak. jika user memilih ingin menambahkan data lagi maka user akan kembali menginput data. jika user memilih tidak maka akan mendapatkan pesan **"penambahan data jadwal matkul selesai"**. selanjutnya user kembali menuju menu utama.
5. jika user memilih **READ** maka akan ada pertanyaan **"Apakah data jadwal Matkul telah ditambahkan?"**. jika data jadwal matkul belum ditambahkan maka user akan mendapatkan pesan **"jadwal matkul belum ditambahkan"** dan user akan langsung menuju menu utama. jika data jadwal matkul sudah  ditambahkan maka sistem akan menampilkan daftar jadwal matkul yang sudah di tambahkan. selanjutnya user akan kembali menuju menu utama.
6. jika user memilih **UPDATE** user akan menginput nama matkul yang ingin di update. jika nama matkul tidak ada maka user akan mendapatkan pesan **"nama matkul tidak ditemukan"** dan user akan langsung menuju menu utama, jika nama matkul ada, maka user akan mengupdate data dari matkul tersebut yaitu harinya, jamnya, dan nama gedungnya. ketika sudah, sistem akan menyimpan data matkul yang di update ke dalam daftar lalu user akan mendapatkan pesan **"data jadwal matkul berhasil ditambahkan"** dan user akan langsung menuju menu utama.
7. jika user memilih **DELETE** user akan menginput nama matkul yang ingin di hapus. jika nama matkul tidak ada maka user akan mendapatkan pesan **"nama matkul tidak ditemukan"** dan user akan langsung menuju menu utama, jika nama matkul ada, sistem akan menghapus data matkul dari dalam daftar lalu user akan mendapatkan pesan **"data jadwal matkul berhasil dihapus"** dan user akan langsung menuju menu utama
8. jika user memilih **LOGOUT** maka user akan mendapatkan pesan **"anda berhasil keluar"** dan program akan langsung menuju login.
9. karena tadi user berada di role manager maka selanjutnya user akan login di role karyawan.
10. Di menu karyawan user akan di tampilkan menu khusus karyawan yaitu **READ** dan **LOGOUT**.
11. jika user memilih **READ** maka akan ada pertanyaan **"Apakah data jadwal Matkul telah ditambahkan?"**. jika data jadwal matkul belum ditambahkan maka user akan mendapatkan pesan **"jadwal matkul belum ditambahkan"** dan user akan langsung menuju menu utama. jika data jadwal matkul sudah  ditambahkan maka sistem akan menampilkan daftar jadwal matkul yang sudah di tambahkan. selanjutnya user akan kembali menuju menu utama.
12. jika user memilih **LOGOUT** maka user akan mendapatkan pesan **"anda berhasil keluar, program selesai"** dan program akan langsung berhenti/**END**.

**penjelasan output pada terminal program pytho dengan memperlihatkan semua kondisi:**

![Output](Screenshot%20(32).png)
