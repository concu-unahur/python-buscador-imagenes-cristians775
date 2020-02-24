import logging
from api import PixabayAPI
import threading
import sys
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'computadoras'
api = PixabayAPI('15362202-85c7e3dd3ffb8e53b1e145798', carpeta_imagenes)


query = sys.argv[1]
num = sys.argv[2]

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, num)
i=0;
for u in urls:
  i+=1
  t=threading.Thread(target=api.descargar_imagen,name=f"T{i}",args=[u])
  t.start()