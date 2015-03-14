from bepro import *
from bordes import *
import matplotlib.pyplot as plt

#Se lee una Imagne RGB
img=cv2.imread('immu.jpg',1)

#Dada una imagen RGB, esta se convierte enescala de grises.
img2=gris(img)

#Se aplica un filtro gauss para eliminar ruido.
img3=gauss(img2)

#Se calcula los gradientes para cada pixel.
m, datos=prewitt(img3)
print 'Una vez mostrado el histograma, identifique el umbral mas adecuado'
print 'posteriormente cierre la ventana de la figura para continuar'

#se genera un histograma con los datos generados anteriormente.
plt.hist(datos,bins=10,color='green',alpha=0.1)
plt.xlabel('Gradientes')
plt.ylabel('Freuencias)
plt.title('histograma')
plt.show()
#En base al histograma mostrado, un umbral es solicitado.
umb=int(raw_input("El umbral es:  "))

#Finalmente se despliega una imagen donde se muestran
#los bordes detenctados
img4=borde(m,umb,img3)

cv2.imshow('Bordes Prewitt',img4)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
