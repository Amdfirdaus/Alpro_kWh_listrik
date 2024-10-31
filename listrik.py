#wat setiap alat dan durasi alat
harga_perkwh=1500

wat_lampu = int(input('masukkan wat lampu = '))
durasi_lampu = int(input('masukkan durasi penggunaan lampu = '))
wat_kipas_angin = int(input('masukkan wat kipas angin = '))
durasi_kipas_angin = int(input('masukkan durasi penggunaan kipas angin = '))
wat_televisi = int(input('masukkan wat televisi = '))
durasi_televisi = int(input('masukkan durasi penggunaan televisi= '))

#proses mencari kwh
print()
kwh_lampu = wat_lampu * durasi_lampu/1000
kwh_kipasangin = wat_kipas_angin * durasi_kipas_angin/1000
kwh_televisi = wat_televisi * durasi_televisi/1000
total_kwh = kwh_kipasangin + kwh_lampu + kwh_televisi

print('kwh lampu = ',kwh_lampu)
print('kwh kipas angin = ',kwh_kipasangin)
print('kwh televisi = ',kwh_televisi)
print('total kwh',total_kwh, '/kwh')

#mencari biaya
biaya_lampu = kwh_lampu * harga_perkwh
biaya_kipas_angin = kwh_kipasangin * harga_perkwh
biaya_televisi = kwh_televisi * harga_perkwh
totalbiaya = biaya_kipas_angin + biaya_lampu + biaya_televisi

print('biaya penggunaan lampu selama', durasi_lampu, 'jam =', biaya_lampu, 'rupiah')

print('biaya penggunaan kipas angin selama', durasi_kipas_angin, 'jam =', biaya_kipas_angin, 'rupiah')

print('biaya penggunaan televisi selama', durasi_televisi, 'jam =', biaya_televisi, 'rupiah')
print('total biaya ', totalbiaya, '/hari')

#total perbulan
totalperbulan = totalbiaya * 30
totalkwhlampu_bulan = kwh_lampu * 30
totalkwhkipasangin_bulan = kwh_kipasangin * 30
totalkwhtelevisi_bulan = kwh_televisi * 30

#output perbulan
print('total kwh lampu perbulan = ',totalkwhlampu_bulan)
print('total kwh kipas angin perbulan = ',totalkwhkipasangin_bulan)
print('total kwh televisi perbulan = ',totalkwhtelevisi_bulan)

print('harga total perbulan = ',totalperbulan)







 
