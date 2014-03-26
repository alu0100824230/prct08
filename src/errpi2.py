
#! encoding: UTF-8
import errorpi
t_upla_intervalos=(10,100,1000,10000,100000)
t_upla_umbrales=(0.1,0.01,0.001,0.0001,0.00001)
for i in t_upla_intervalos:
  print "Con el número de intervalos %d" %i
  for j in t_upla_umbrales:
    s=errorpi.error(i,1,j)
    print "Porcentaje de error para el umbral %f: %5.2f" %(j,s)