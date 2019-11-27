#  ------------------------ Rabu, 27 November 2019 -----------------------------------

# Input tahun : 2019
# Hasil : BUKAN TAHUN KABISAT

# Input tahun : 2020
# Hasil : TAHUN KABISAT

def kabisat(isi):
    if isi%4 == 0:
        print('Hasil : TAHUN KABISAT')
    else:
        print('Hasil : BUKAN TAHUN KABISAT')

tahun = int(input(f'Input tahun : '))
kabisat(tahun)
