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
        name = 'testabc'
        email = 'testabcd@domain.com'
        alamat = 'testalamat'
        kota = 'testkota'
        id = 15

        sql = 'UPDATE anggota_perpus SET name=%s,email=%s,alamat=%s,kota=%s WHERE id=%s'
        val = (name,email,alamat,kota,id)
        
        # eksekusi sql
        mycursor.execute(sql,val)

        koneksi.commit() 
    except mysql.connector.DatabaseError:
        print('Update data gagal')
        koneksi.rollback()
    else:
        print('Update data berhasil')
        mycursor.close
except:
    pass