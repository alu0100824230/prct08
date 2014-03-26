
#! encoding: UTF-8
import modulo
def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)
if __name__=="__main__":
   import sys
   if (len(sys.argv)==4):
     p1=int(sys.argv[1])
     p2=int(sys.argv[2])
     p3=float(sys.argv[3])
   else:
     print "Usted debe proporcionar tres valores, errorpi.py y tres valores numéricos, ahora se ejecutará por defecto con los valores 5 5 0.1"
     p1=5
     p2=5
     p3=0.1
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s