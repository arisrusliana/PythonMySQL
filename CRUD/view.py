from CRUD import operasi
import mysql.connector


def delete_console():
    
    # menampilkan data existing
    read_console()

    ID = input ('Masukkan No ID yang ingin Anda hapus : ')
    
    try:
        # membuat koneksi ke database
        koneksi = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'perpustakaan'
        )
        
        try:
            # membuat cursor
            mycursor = koneksi.cursor()

            sql = 'SELECT * FROM anggota_perpus WHERE id = "'+ID+'"'
        
            mycursor.execute(sql)

            hasil = mycursor.fetchall()

            # menampilkan data yang dipilih
            # header
            print(120*'=')
            print(f'|{('ID').center(4)}|{('NAMA').center(30)}|{('EMAIL').center(30)}|{('ALAMAT').center(30)}|{('KOTA').center(20)}| ')
            print(120*'=')
            
            # tabel
            for row in hasil:
                id = row[0]
                nama = row[1]
                email = row[2]
                alamat = row[3]
                kota = row[4]

                print('|{:^4}|{:^30}|{:^30}|{:^30}|{:^20}|'.format(id,nama,email,alamat,kota))
                print(120*'=')

                is_accept = input('Apakah Anda yakin?(y/n) : ')
                if is_accept == 'y' or is_accept == 'Y':
                    operasi.delete_data(ID)
        except :
            print('Pengambilan data gagal')
        else:
            print('')
    except mysql.connector.Error as e:
        print('Error : ',e)
    else:
        print('')  


def update_console():
    
    # menampilkan data existing
    read_console()

    ID = input ('Masukkan No ID yang ingin Anda Update : ')

    try:
        # membuat koneksi ke database
        koneksi = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'perpustakaan'
        )
        
        try:
            # membuat cursor
            mycursor = koneksi.cursor()

            sql = 'SELECT * FROM anggota_perpus WHERE id = "'+ID+'"'
        
            mycursor.execute(sql)

            hasil = mycursor.fetchall()

            # menampilkan data yang dipilih
            # header
            print(120*'=')
            print(f'|{('ID').center(4)}|{('NAMA').center(30)}|{('EMAIL').center(30)}|{('ALAMAT').center(30)}|{('KOTA').center(20)}| ')
            print(120*'=')
            
            # tabel
            for row in hasil:
                id = row[0]
                nama = row[1]
                email = row[2]
                alamat = row[3]
                kota = row[4]

                print('|{:^4}|{:^30}|{:^30}|{:^30}|{:^20}|'.format(id,nama,email,alamat,kota))
            print(120*'=')

            # input data update
            while(True):
                print('\n')
                print('Masukkan data baru')
                update_nama = input('Nama \t: ')
                update_email = input('Email \t: ')
                update_alamat = input('Alamat \t: ')
                update_kota = input('Kota \t: ')
                
                print('\n')
                print('Data baru Anda : ')
                print(f'Nama \t: {update_nama}')
                print(f'Email \t: {update_email}')
                print(f'Alamat \t: {update_alamat}')
                print(f'Kota \t: {update_kota}')
                is_accept = input('Apakah Anda yakin?(y/n) : ')
                if is_accept == 'y' or is_accept == 'Y':
                    break
            
            operasi.update_data (ID,update_nama,update_email,update_alamat,update_kota)
        except:
            print('Pengambilan data gagal')
        else:
            print('')
    
    except mysql.connector.Error as e:
        print('Error : ', e)
    else :
        print('')


def create_console():
    print('\n')
    print(10*'=','INPUT DATA',10*'=')
    input_name = input('Nama \t: ')
    input_email = input('Email \t: ')
    input_alamat = input('Alamat \t: ')
    input_kota = input('Kota \t: ')

    operasi.create_data(input_name,input_email,input_alamat,input_kota)


def read_console():

    try:
        # membuat koneksi ke database
        koneksi = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'perpustakaan'
        )

        try:
            # membuat cursor
            mycursor = koneksi.cursor()

            sql = 'SELECT * FROM anggota_perpus'
        
            mycursor.execute(sql)

            hasil = mycursor.fetchall()
            # judul
            # print('\n')
            print(f'{('TABEL DATA ANGGOTA PERPUSTAKAAN').center(120)}')

            # header
            print(120*'=')
            print(f'|{('ID').center(4)}|{('NAMA').center(30)}|{('EMAIL').center(30)}|{('ALAMAT').center(30)}|{('KOTA').center(20)}| ')
            print(120*'=')
            
            # tabel
            for row in hasil:
                id = row[0]
                nama = row[1]
                email = row[2]
                alamat = row[3]
                kota = row[4]

                print('|{:^4}|{:^30}|{:^30}|{:^30}|{:^20}|'.format(id,nama,email,alamat,kota))
            print(120*'=')

        except:
            print('Pengambilan data gagal')
        else:
            print('')

    except mysql.connector.Error as e:
        print('Error : ', e)
    else :
        print('')