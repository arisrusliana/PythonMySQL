
import mysql.connector

def delete_data(ID):
    try:
        # membuat koneksi ke database
        koneksi = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'perpustakaan'
        )
    
        # membuat cursor
        mycursor = koneksi.cursor()
        
        sql = 'DELETE FROM anggota_perpus WHERE id = "'+ID+'"'
        
        mycursor.execute(sql)
        koneksi.commit()

    except mysql.connector.Error as e :
        print('Error : ',e)
    else:
        print('\n')
        print ('Hapus data berhasil')
        mycursor.close()    

def update_data(ID,update_nama,update_email,update_alamat,update_kota):
    try:
        # membuat koneksi ke database
        koneksi = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'perpustakaan'
        )
        
        # membuat cursor
        mycursor = koneksi.cursor()

        sql = 'UPDATE anggota_perpus SET name = "'+update_nama+'", email = "'+update_email+'", alamat = "'+update_alamat+'", kota = "'+update_kota+'" WHERE id = "'+ID+'"'
        
        mycursor.execute(sql)
        koneksi.commit()

    except mysql.connector.Error as e :
        print('Error : ',e)
    else:
        print('\n')
        print ('Update data berhasil')
        mycursor.close()

def create_data(input_name,input_email,input_alamat,input_kota):
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

            name = input_name
            email = input_email
            alamat = input_alamat
            kota = input_kota

            sql = 'INSERT INTO  anggota_perpus (name,email,alamat,kota) VALUES ("'+name+'","'+email+'","'+alamat+'","'+kota+'")'

            # eksekusi sql
            mycursor.execute(sql)

            koneksi.commit() 
        except mysql.connector.DatabaseError:
            print('Input data gagal')
            koneksi.rollback()
        else:
            print('\n')
            print('Input data berhasil')
            print('\n')
            mycursor.close()
    except:
        pass

def read_data():
    pass