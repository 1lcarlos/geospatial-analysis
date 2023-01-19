import rasterio
fileBand3 ='LC09_L1TP_007058_20221226_20221226_02_T1/LC09_L1TP_007058_20221226_20221226_02_T1_B3.TIF'
dataset = rasterio.open(fileBand3)


#print (dataset.width)
#print (dataset.height)
#print (dataset.bounds)
#print (dataset.transform)
#print (dataset.transform*(0,0)) #Esquina Superior isquierda
#print (dataset.transform * (dataset.width, dataset.height)) #Esquina Inferior derecha
#print (dataset.crs)
print (dataset.indexes)

band3 = dataset.read(1)

print (band3)

dataset.close()