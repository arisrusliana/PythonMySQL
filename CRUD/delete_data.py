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

        id = 16

        sql = 'DELETE FROM anggota_perpus WHERE id=%s'
        
        # eksekusi sql
        mycursor.execute(sql,(id,))

        koneksi.commit()

    except mysql.connector.DatabaseError:
        print('Hapus data gagal')
        koneksi.rollback()
    else:
        print('Hapus data berhasil')
        mycursor.close
except:
    pass