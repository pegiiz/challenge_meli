# challenge_meli
Script para subir/descargar/borrar archivos de s3 desde una instancia de ec2 o cliente usando curl desde la consola con el puerto 5000. 
Este script funciona como un proxy entre Amazon S3 y el cliente. Esta hosteado en una instancia EC2, usando Flask y Gunicorn como WSGI


**instrucciones**:  
**descargar archivo** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/downloads3/tu_bucket/tu_key**
El servidor devolvera una presigned url, para descargar dicho archivo usando curl de nuevo o desde el navegador. En los endpoints se deben especificar la funcion **/downloads3/**   seguida del bucket, y para descargar, especificar la key. 

**subir un archivo** : **curl -F 'file=@/PATH/DEL/ARCHIVO' http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/uploads3/tu_bucket**  
El servidor devolvera un texto "archivo subido" si fue exitosa la subida, si el bucket en el que quiere subir el archivo no existe, devolvera "el bucket no existe". el archivo debe ser escrito en el path tal cual aparece en la consola. 
Para saber el path : realpath *archivo*  

**listar archivos en bucket** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/listfiles/tu_bucket/**   
El endpoint */listfiles/tu_bucket* devolvera  un json listando todos los objetos en el bucket especificado 

**borrar archivos** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/deletefile/tu_bucket/tu_key**

# features a implementar  

**seguridad**: Algo que me quedo pendiente fue poder habilitar el server para que reciba requests desde el puerto 80 con un proxy como nginx, y tambien hacer la certificacion de https.    

Otro feature de seguridad a futuro podria ser implementar un sistema de autenticacion, que la app tenga una base de datos con usuarios y obligue al cliente a logear con sus credenciales antes de hacer cualquier cosa.

**funcionalidades de la app**: mejorar la funcion de subir archivos,ya que esta solo puede subir de a un solo archivo y es muy poco practico. para que se puedan subir carpetas, o archivos en cantidad. podria ser un nuevo endpoint que abra una pagina web y permita arrastrar archivos o poder seleccionar muchos.
