listMobil =[
    {
    'idMobil' : 111,
    'merk' : 'Honda',
    'tahun' : 2020,
    'model': 'City Car',
    'hargaSewa': 10000,
	'status' : 'Tersedia'   
    },
    {
    'idMobil' : 112,
    'merk' : 'Honda',
    'model': 'City Car',
    'tahun' : 2022,
    'hargaSewa': 15000,
	'status' : 'Tersedia'  
    },
    {
    'idMobil' : 113,
    'merk' : 'Toyota',
    'model': 'City Car',
    'tahun' : 2022,
    'hargaSewa': 13000,
	'status' : 'Tersedia'  
    },
    {
    'idMobil' : 114,
    'merk' : 'Isuzu',
    'model': 'Mini Bus',
    'tahun' : 2021,
    'hargaSewa': 20000,
	'status' : 'Kosong'    
    }   
]

cart = []


def menampilakanDaftarMobil() :
    print('-----------------------------------Daftar Mobil-----------------------------------\n')
    print('__________________________________________________________________________________\n')
    print('idMobil\t|  Merk   \t|  Model   \t| Tahun\t| Harga Sewa   \t| Satus')
    print('__________________________________________________________________________________\n')
    for i in range(len(listMobil)):
        print ('  {}  \t|  {}\t|  {}  \t| {}\t| {}  \t| {}'.format(listMobil[i]['idMobil'],listMobil[i]['merk'],listMobil[i]['model'],listMobil[i]['tahun'],listMobil[i]['hargaSewa'],listMobil[i]['status'] ))
   
def Read():
    x = int(input('''
            Menu Tampilkan Data Mobil
            1. Tampilkan Semua Data Mobil   
            2. Tampilkan Data Berdasarkan idMobil            
            3. Kembali ke menu utama
            Menu yg ingin di jalankan (1-3) : '''))
    if (x == 1):
        menampilakanDaftarMobil()
        Read()
    elif (x == 2):
        filterId()
    elif (x == 3):
        mainmenu()
    else:
        Read()

def filterId():      
    def tabel():
        print('-----------------------------------Daftar Mobil-----------------------------------')
        print('__________________________________________________________________________________\n')
        print('idMobil\t|  Merk   \t|  Model   \t| Tahun   \t| Harga Sewa   \t| Satus')
        print('__________________________________________________________________________________\n')
        for i in range(len(searchMobil)):
            print ('{}  \t|  {}  \t|  {}  \t| {}  \t| {}  \t| {}'.format(searchMobil[i]['idMobil'],searchMobil[i]['merk'],searchMobil[i]['model'],searchMobil[i]['tahun'],searchMobil[i]['hargaSewa'],searchMobil[i]['status'] )) 
        
    idMobil = int(input('\n\tKetikkan idMobil: '))
    for i in range(len(listMobil)):
        if (i==len(listMobil)-1) and (idMobil != listMobil[i]['idMobil']):
            print('\t------idMobil Tdak Di temukan------')
        elif idMobil == listMobil[i]['idMobil']:
            searchMobil = [i for i in listMobil 
                          if i['idMobil']== idMobil]
            tabel()
            break
        else:
            continue
    Read()
            

def Add():
    inTambah = int(input('''
            Menu Menambah Data Mobil
            1. Menambah Data Mobil   
            2. Kembali ke menu utama
            Menu yg ingin di jalankan (1-2) : '''))

    def tabel():
        print('-----------------------------------Daftar Mobil-----------------------------------')
        print('__________________________________________________________________________________\n')
        print('idMobil\t|  Merk   \t|  Model   \t| Tahun   \t| Harga Sewa   \t| Satus')
        print('__________________________________________________________________________________\n')
        for i in range(len(searchMobil)):
            print ('{}  \t|  {}  \t|  {}  \t| {}  \t| {}  \t| {}'.format(searchMobil[i]['idMobil'],searchMobil[i]['merk'],searchMobil[i]['model'],searchMobil[i]['tahun'],searchMobil[i]['hargaSewa'],searchMobil[i]['status'] )) 
          
    if (inTambah == 1):
        idMobil = int(input('\nKetikkan idMobil: '))
        for i in range(len(listMobil)):
            if idMobil == listMobil[i]['idMobil']:
                searchMobil = [i for i in listMobil 
                            if i['idMobil']== idMobil]
                tabel()
                print('\n------idMobil tersebut sudah ada------')
                Add()
                break
            else :
                print('NewID Silakan Masukkan Data Baru')
                print('\n\t------Input Data MObil Baru------')
                idMobil    = int(input ('\tMasukkan idMobil :'))
                merkMobil  = input ('\tMasukkan merk Mobil :')
                modelMobil = input('\tMasukkan model Mobil :')
                tahun      = int(input('\tMasukkan tahun Mobil :'))
                hargaSewaMobil = int(input('\tMasukkan hargaSewa Mobil :'))
                statusMobil = input('\tMasukkan status Mobil :')
                break
        cek = input('\nLanjut Simpan Data Mobil ? (ya/tidak)')
        if(cek == 'ya'):
            listMobil.append({
                'idMobil' : idMobil,
                'merk' : merkMobil,
                'model' :modelMobil,
                'tahun' : tahun,
                'hargaSewa' :hargaSewaMobil,
		        'status' :statusMobil    
                })
            print('------Data Tersimpan------')
            menampilakanDaftarMobil()
            Add()
        else:
            print('------Data Tidak Tersimpan------')
            Add()
    if (inTambah == 2):
         mainmenu()

   
def Update():
    menampilakanDaftarMobil()
    inUpdate = int(input('''
            Menu Update Data Mobil
            1. Update Data Mobil            
            2. Kembali ke menu utama
            Menu yg ingin di jalankan (1-2) : '''))

    def tabel():
        print('-----------------------------------Daftar Mobil-----------------------------------')
        print('__________________________________________________________________________________\n')
        print('Index\t|  Merk   \t|  Model   \t| Tahun   \t| Harga Sewa   \t| Satus')
        print('__________________________________________________________________________________\n')
        for i in range(len(searchMobil)):
            print ('  {}  \t|  {}  \t|  {}  \t| {}  \t| {}  \t| {}'.format(searchMobil[i]['idMobil'],searchMobil[i]['merk'],searchMobil[i]['model'],searchMobil[i]['tahun'],searchMobil[i]['hargaSewa'],searchMobil[i]['status'] )) 

    if (inUpdate == 1):
         idMobil = int(input('\n\tKetikkan idMobil: '))
         for i in range(len(listMobil)):
            if (i==len(listMobil)-1) and (idMobil != listMobil[i]['idMobil']):
                 print('\t------idMobil Tdak Di temukan------')
                 Update()
                 break
            elif idMobil == listMobil[i]['idMobil']:
                searchMobil = [i for i in listMobil 
                            if i['idMobil']== idMobil]
                tabel()
                cek = input('\nLanjut Update data ? : (ya/tidak)')
                if (cek == 'ya'):
                    updateData = int(input('''
                        Data yg ingin di update :                                                                               
                        1. HargaSewa
                        2. Status
                        Masukkan kategori yg ingin di update : '''))   
                    if  updateData == 1:               
                        hargaSewa = int(input ('\t\t\tMasukkan data terbaru:'))
                        cek = input('\nLanjut Proses Update data ? : (ya/tidak)')
                        if (cek == 'ya'):
                            listMobil[i]['hargaSewa'] = hargaSewa
                            print('Data sudah diupdate')
                    elif  updateData == 2:               
                        Status = (input ('\t\t\tMasukkan data terbaru:'))
                        cek = input('\nLanjut Proses Update data ? : (ya/tidak)')
                        if (cek == 'ya'):
                            listMobil[i]['status'] = Status
                            print('Data sudah diupdate')
                    else :            
                        Update()    
                Update()
    if (inUpdate == 2):
         mainmenu()
    else :
        menampilakanDaftarMobil()

     

def Delete():
    inHapus = int(input('''
            Menu Hapus Data Mobil
            1. Hapus Data Mobil            
            2. Kembali ke menu utama
            Menu yg ingin di jalankan (1-2) : '''))

    def tabel():
        print('-----------------------------------Daftar Mobil-----------------------------------')
        print('__________________________________________________________________________________\n')
        print('Index\t|  Merk   \t|  Model   \t| Tahun   \t| Harga Sewa   \t| Satus')
        print('__________________________________________________________________________________\n')
        for i in range(len(searchMobil)):
            print ('  {}  \t|  {}  \t|  {}  \t| {}  \t| {}  \t| {}'.format(searchMobil[i]['idMobil'],searchMobil[i]['merk'],searchMobil[i]['model'],searchMobil[i]['tahun'],searchMobil[i]['hargaSewa'],searchMobil[i]['status'] )) 

    if (inHapus == 1):
         idMobil = int(input('\tKetikkan idMobil: '))
         for i in range(len(listMobil)):
            if (i==len(listMobil)-1) and (idMobil != listMobil[i]['idMobil']):
                print('\t------idMobil Tdak Di temukan------')
                Delete() 
            elif idMobil == listMobil[i]['idMobil']:
                searchMobil = [i for i in listMobil 
                            if i['idMobil']== idMobil]
                tabel()
                cek = input('\nLanjut Proses Hapus data ? : (ya/tidak)')
                if (cek == 'ya'):
                    del listMobil[i]
                    menampilakanDaftarMobil()
                    print ('-------Data Sudah dihapus-------')
                    break
                if (cek == 'tidak'):
                    menampilakanDaftarMobil()
                    print ('-------Data Tidak dihapus-------')
                    Delete()
                break
            else:
                continue
    if (inHapus == 2):
        mainmenu()

def Filter():
    inFilter = int(input('''
        Filter data Berdasarkan
        1. Merk    
        2. Model               
        3. Status
        4. Kembali ke menu utama
        Filter Data Mobil berdasarkan No (1-3) : '''))

    def tabel():
         print('-----------------------------------Daftar Mobil-----------------------------------\n')
         print('__________________________________________________________________________________\n')
         print('Index\t|  Merk   \t|  Model   \t| Tahun   \t| Harga Sewa   \t| Satus')
         print('__________________________________________________________________________________\n')
         for i in range(len(searchMobil)):
            print ('  {}  \t|  {}  \t|  {}  \t| {}  \t| {}  \t| {}'.format(i,searchMobil[i]['merk'],searchMobil[i]['model'],searchMobil[i]['tahun'],searchMobil[i]['hargaSewa'],searchMobil[i]['status'] ))  #dictionary
         
    if (inFilter == 1):
        merk = input('Ketikkan Nama Merk : ')
        searchMobil = [i for i in listMobil
               if i['merk']== merk]
        tabel()
        Filter()
    elif (inFilter == 2): 
        model = input('Ketikkan Nama Model : ')
        searchMobil = [i for i in listMobil
               if i['model']== model]
        tabel()
        Filter()
    elif (inFilter == 3): 
        status = input('Ketikkan Nama Model : ')
        searchMobil = [i for i in listMobil
               if i['status']== status]
        tabel()
        Filter()
    else:
        mainmenu()


def Rent():
    def tabelSewaMobil() :
        print('----------------------------------------Daftar Mobil----------------------------------------\n')
        print('____________________________________________________________________________________________\n')
        print('index \t| idMobil\t|  Merk   \t|  Model   \t| Tahun\t| Harga Sewa   \t| Satus')
        print('____________________________________________________________________________________________\n')
        for i in range(len(listMobil)):
            print ('  {}  \t|  {}  \t|  {}\t|  {}  \t| {}\t| {}  \t| {}'.format(i,listMobil[i]['idMobil'],listMobil[i]['merk'],listMobil[i]['model'],listMobil[i]['tahun'],listMobil[i]['hargaSewa'],listMobil[i]['status'] ))
    
    inputsewa = int(input('''
        Menu Menyewa Mobil :
        1. Menyewa Mobil
        2. Kembali ke menu utama
        \nMasukkan menu yg ingin di jalankan : '''))
    tabelSewaMobil()
    if(inputsewa == 1):
        while True :         
            indexMobil = int(input('\nMasukkan index Mobil yang ingin disewa : '))
            if listMobil[indexMobil]['status'] == 'Kosong':
                print ('Status Mobil Kosong')     
            else :
                while True:
                    jumlahHari = int(input('Masukkan Jumlah hari penyewaan - max 30 hari: '))
                    if (jumlahHari > 30):
                        print ('Batas maximal penyewaan 30 hr')
                    elif (jumlahHari < 0):
                        print ('Minimal sewa 1 hari')   
                    else :
                        break  
           
                cart.append({
                'idMobil' : listMobil[indexMobil]['idMobil'],
                'merk' : listMobil[indexMobil]['merk'],
                'jumlahHari' : jumlahHari,
                'hargaSewa' : listMobil[indexMobil]['hargaSewa'],
                'index' : listMobil
                })
            
                print('\n-----------------Cart Penyewaan-----------------')
                print('idMobil\t| merk\t| jumlahHari \t| hargaSewa')       
                for item in cart :
                    print ('{}\t| {}\t| {}\t\t| {}'.format(item['idMobil'],item['merk'],item['jumlahHari'],item['hargaSewa']))   
                cek = input('Ada tambahan unit yg akan di sewa ? (ya/tidak)')
                if(cek == 'tidak'):
                    break            
        print('\n-----------------Summary Penyewaan-----------------')
        print('idMobil \t| merk \t| jumlahHari \t| hargaSewa \t| Total hargaSewa')   
        totalhargaSewa = 0
        for item in cart :
            print ('{}\t| {}\t| {}\t\t| {}'.format(item['idMobil'],item['merk'],item['jumlahHari'],item['hargaSewa']))
        totalhargaSewa += item['jumlahHari'] * item['hargaSewa']
        while True :
            print('Total yang harus di bayar = {}'.format(totalhargaSewa))
            jmlUang = int(input('\nMasukkan Jumlah Uang : '))
            if( jmlUang > totalhargaSewa) :
                kembali = jmlUang - totalhargaSewa
                print('Terima kasih \n\nKelebihan Uang Anda : {}'.format(kembali))
                cart.clear()
                break
            elif(jmlUang == totalhargaSewa):
                print('Terima Kasih')
                cart.clear()
                Rent()
                break
            else :
                kekurangan = totalhargaSewa - jmlUang
                print('Uang anda kurang sebesar {}'.format(kekurangan))
         
        cart.clear()
        Rent()
    else:
        mainmenu()

def mainmenu():    
    while True :                                
        pilihanMenu = int(input('''                 
        SELAMAT DATANG DI Rental Mobil SIMPLE
                        
            List Menu :
            1. Menampilkan Data Mobil 
            2. Menambahkan Data Mobil               
            3. Mengupdate Data Mobil 
            4. Menghapus Data Mobil
            5. Memfilter Data MObil    
            6. Menyewa Mobil
            7. Keluar Program         

            Masukkan angka Menu yg ingin di jalankan: '''))
        if(pilihanMenu == 1):
            Read()
        elif(pilihanMenu == 2):
            Add()     
        elif(pilihanMenu == 3):
            Update()           
        elif(pilihanMenu == 4):
            Delete()
        elif(pilihanMenu == 5):
            Filter()
        elif(pilihanMenu == 6):
            Rent()
        elif(pilihanMenu == 7):
            break
        else:
            mainmenu()

mainmenu()