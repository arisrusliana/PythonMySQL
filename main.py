import os
import CRUD as CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
   
    while(True):
        match sistem_operasi:
            case ('nt'): os.system('cls')
            case ('posix'): os.system('clear')
        
        # menu
        print('SELAMAT DATANG')
        print('DI APLIKASI PERPUSTAKAAN')
        print('='*120)
        print(f'1. Lihat Data')
        print(f'2. Input Data')
        print(f'3. Update Data')
        print(f'4. Delete Data')
        print(f'5. Keluar\n')
    
        pilih_menu = input('Pilih menu yang Anda inginkan (1-5) : ')
    
        match pilih_menu:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': CRUD.delete_console()
            case '5': break
            case _: print('Menu tidak valid')
        
       
        is_done = input('Apakah sudah selesai?(y/n) : ')
        if is_done == 'y' or is_done == 'Y':
            break
        
    print('\n')
    print(5*' === '+' Program Berakhir '+ 5*' === ')
    print('\n')