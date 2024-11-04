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

        name = 'abc'
        email = 'abcd'
        alamat = 'abcde'
        kota = 'abcdef'

        sql = 'INSERT INTO  anggota_perpus (name,email,alamat,kota) VALUES ("'+name+'","'+email+'","'+alamat+'","'+kota+'")'

        # eksekusi sql
        mycursor.execute(sql)

        koneksi.commit() 
    except mysql.connector.DatabaseError:
        print('Input data gagal')
        koneksi.rollback()
    else:
        print('Input data berhasil')
        mycursor.close()
except:
    pass