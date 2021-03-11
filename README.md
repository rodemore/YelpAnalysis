# HackathonTAWS
Taller sobre uso básico de sockets en Linux usando C para la materia Programación de Sistemas (CCPG1051) de la ESPOL.

## Instrucciones
La práctica consiste en crear una aplicación cliente - servidor para generar un hash SHA-256 a partir de una cadena de caracteres:
1. El cliente debe enviar al servidor la cadena de caracteres.
2. El servidor debe usar la cadena de caracteres recibida, ignorando el salto de línea al final, y generar un hash SHA-256. Usar [crypto-algorithms](https://github.com/B-Con/crypto-algorithms).
3. El servidor debe enviar el hash SHA-256 en formato ASCII Hex terminado con un salto de línea al cliente.

Toda comunicación entre cliente y servidor debe ser enviada en modo ASCII con salto de línea al final.

Para ejecutar el servidor se debe especificar como argumento el puerto TCP, por ejemplo:
```
$ ./server 8080
server escuchando en puerto 8080...
```

Asumiendo que el servidor esta corriendo en una maquina con la IP 192.168.100 en el puerto 8080, ejemplo de ejecución del cliente:
```
$ ./client 192.168.100 8080
Conectado exitosamente a 192.168.100 en el puerto 8080.
Ingrese texto para enviar al servidor, escriba CHAO para terminar...
> hola
Recibido: b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79
> 
```
Si el servidor esta en la misma máquina, entonces es necesario abrir otra ventana/tab de terminal y ejecutar el cliente de esta forma:
```
$ ./client 127.0.0.1 8080
Conectado exitosamente a 127.0.0.1 en el puerto 8080.
Ingrese texto para enviar al servidor, escriba CHAO para terminar...
> 
```

## Código ejemplo
Este repositorio contiene código ejemplo de una aplicación *eco* cliente - servidor. Es decir, el usuario ingresa una línea de texto desde el cliente, el cliente la envia al servidor y el servidor la envia de regreso.

## Entregable
Modificar el código ejemplo en este repositorio para implementar la aplicación cliente - servidor de hashing SHA-256.

### TIPS
Es necesario modificar solamente el servidor, es decir *server.c*, el *Makefile* y agregar los archivos para implementar SHA-256 (ver [crypto-algorithms](https://github.com/B-Con/crypto-algorithms)).

Además, es importante considerar que el hash debe ser enviado por el socket en formato ASCII Hex (en lugar de directamente en binario). Para esto, se puede usar esta función la cual convierte un buffer binario a una cadena de caracteres en ASCII Hex con un salto de línea al final:
```C
void sprint_hex(char *output, const unsigned char* input, size_t size)
{
    int i;
    for(i = 0; i < size; ++i)
        sprintf(output + 2*i, "%02x", input[i]);
    sprintf(output + 2*i, "\n");
}
```

## Compilación
Para compilar cliente y servidor:
```
$ make
```
Para compilar solo el servidor:
```
$ make server
```
Para compilar cliente y servidor facilitando la depuración con gdb:
```
$ make debug
```
Para compilar cliente y servidor habilitando la herramienta AddressSanitizer, facilita la depuración en tiempo de ejecución:
```
$ make sanitize
```

## Test
Para probar el test de autocalificación:
```
$ make -f Testfile
```
