# challenge_meli
Script para subir/descargar/borrar archivos de s3 desde una instancia de ec2 o cliente usando curl desde la consola con el puerto 5000                                       

**instrucciones**:  
**descargar archivo** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/downloads3/tu_bucket/tu_key**
El servidor devolvera una presigned url, para descargar dicho archivo usando curl de nuevo o desde el navegador. En los endpoints se deben especificar la funcion **/downloads3/**   seguida del bucket, y para descargar, especificar la key. 

**subir un archivo** : **curl -F 'file=@/PATH/DEL/ARCHIVO' http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/uploads3/tu_bucket**  
El servidor devolvera un texto "archivo subido" si fue exitosa la subida, si el bucket en el que quiere subir el archivo no existe, devolvera "el bucket no existe". el archivo debe ser escrito en el path tal cual aparece en la consola. 
Para saber el path : realpath *archivo*  

**listar archivos en bucket** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/listfiles/tu_bucket/**   
El endpoint */listfiles/tu_bucket* devolvera  un json listando todos los objetos en el bucket especificado 

**borrar archivos** : **curl http://ec2-34-229-160-124.compute-1.amazonaws.com:5000/deletefile/tu_bucket/tu_key**

