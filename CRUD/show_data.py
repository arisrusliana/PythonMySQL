import mysql.connector

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
        print('\n')
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