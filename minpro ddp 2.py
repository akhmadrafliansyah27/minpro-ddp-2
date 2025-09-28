user = {
    "ahmad" : {"password" : 123, "role" : "manager"},
    "rafli" : {"password" : 456, "role" : "karyawan"}
}
jadwal_matkul = {}
#fungsi login  
def login():
 while True:
     print("== halaman login ===")
     while True:
      try:
          username = input("masukan nama kamu: ")
          password = int(input("masukan password: "))
      except ValueError:
          print("password harus berupa angka.")
      except KeyboardInterrupt:
          print("jangan tekan Ctrl c ya!")
      except EOFError:
          print ("jangan tekan Ctrl z ya!")

      if username in user and user[username]["password"] == password :
           print(f"login berhasil, Role: {user[username]['role']}")
           return user[username]['role']
      
      else:
           print("login gagal,")

#fungsi menu
def menu():
    print("\n=== menu ===")
    print("1. CREATE")
    print("2. READ")
    print("3. UPDATE")
    print("4. DELETE")
    print("5. LOGOUT")

#fungsi creat
def CREAT():
    while True:
        jawab = input("apakah anda ingin menambahkan jadwal matkul? (yes/no): ")
        if jawab == "yes":
                while True:
                 try:
                    nama_matkul = input("masukan nama matkul: ")
                    hari = input("masukan hari: ")
                    jam = input("masukan jam: ")
                    nama_gedung = input("masukan nama gedung: ")
                    break
                 except KeyboardInterrupt:
                    print("jangan tekan Ctrl c ya!")
                 except EOFError:
                     print ("jangan tekan Ctrl z ya!")
        
                jadwal_matkul[nama_matkul] = {
                "nama_matkul"   : nama_matkul,
                "hari"          : hari,
                "jam"           : jam,
                "nama_gedung"   : nama_gedung
                }
                
                print("data berhasil di tambahkan")

        elif jawab == "no":
            print("penambahan jadwal matkul selesai")
            break

        else:
            print("jawaban tidak valid silahkan jawab yes/no")

def READ() :
    print("== daftar jadwal matkul ==")
    if jadwal_matkul:
        for nama_matkul, daftar in jadwal_matkul.items():
            print(f"Nama Matkul : {daftar['nama_matkul']}")
            print(f"Hari        : {daftar['hari']}")
            print(f"Jam         : {daftar['jam']}")
            print(f"Nama Gedung : {daftar['nama_gedung']}")
            print()
    else:
        print("daftar jadwal matkul masih kosong")

def UPDATE():
    READ()
    while True:
     try:
        cari_matkul = input("masukan nama matkul yang ingin di update: ")
        break
     except KeyboardInterrupt:
        print("jangan tekan Ctrl c ya!")
     except EOFError:
        print ("jangan tekan Ctrl z ya!")
  
    if cari_matkul in jadwal_matkul:
            while True:
             try:
                nama_matkul_baru = input("masukan nama matkul yang baru atau tetap masukan nama matkul yang lama  : ")
                hari_baru = input("masukan nama hari yang baru atau tetap masukan nama hari yang lama : ")
                jam_matkul_baru = input("masukan jam yang baru atau tetap masukan jam yang lama : ")
                nama_gedung_baru = input("masukan nama gedung  yang baru atau tetap masukan nama gedung yang lama: ")
                break
             except KeyboardInterrupt:
                print("jangan tekan Ctrl c ya!")
             except EOFError:
                print ("jangan tekan Ctrl z ya!")
     
            jadwal_matkul[cari_matkul] = {
                     "nama_matkul"   : nama_matkul_baru,
                     "hari"          : hari_baru,
                     "jam"           : jam_matkul_baru,
                     "nama_gedung"   : nama_gedung_baru
                     }

            print("data berhasil di tambahkan")
    else:
         print("data dengan nama jadwal matkul tersebut tidak di temukan")

def DELETE():
    READ()
    while True:
     try:
        hapus_matkul = input("masukan nama matkul yang ingin di hapus: ")
        break
     except KeyboardInterrupt:
        print("jangan tekan Ctrl c ya!")
     except EOFError:
        print ("jangan tekan Ctrl z ya!")

    if hapus_matkul in jadwal_matkul:
        del jadwal_matkul[hapus_matkul]
        print("data jadwal matkul tersebut berhasil di hapus")
    else:
        print("data nama jadwal matkul tersebut tidak di temukan")

def LOGOUT():
    print("anda berhasil keluar.")

def menu_manager():
    while True:
        menu()
        pilih = input("pilih menu: ")

        if pilih == "1" or pilih == "CREATE":
            CREAT()
        elif pilih == "2" or pilih == "READ":
            READ()
        elif pilih == "3" or pilih == "UPDATE" :
            UPDATE()
        elif pilih == "4" or pilih == "DELETE":
            DELETE()
        elif pilih == "5" or pilih == "LOGOUT":
            LOGOUT()
            break

        else:
            print("menu tidak valid")

def menu_karyawan():
    while True:
        print("=== menu ===")
        print("1. READ")
        print("2. LOGOUT")
        pilih = input ("pilih menu: ")

        if pilih == "1" or pilih == "READ":
            READ()
        elif pilih == "2" or pilih == "LOGOUT":
            LOGOUT()
            break
        else:
            print("menu tidak valid")

while True:
    role = login()
    if role == "manager":
        menu_manager()
    elif role == "karyawan":
        menu_karyawan()
        break
    else:
        print()






