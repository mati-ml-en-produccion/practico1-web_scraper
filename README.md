# Práctico 1 - ML en Producción

En este práctico abordaremos algunos conceptos básicos sobre: 

- Git 
- Docker
- Dependencias en Python
- Ejemplo
- Conectarte a Azure Cloud mediante CLI

# Git

Git es un sistema de control de versiones de software libre y de código abierto diseñado para manejar proyectos de cualquier tamaño con velocidad y eficiencia. 

Git proporciona una forma de compartir el código fuente con otros desarrolladores a través de repositorios remotos, como *GitHub* o *Bitbucket*

Para comenzar a usar Git, necesitas tenerlo instalado en tu computadora. 

Puedes descargar Git desde su sitio web oficial [Download Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) y seguir las instrucciones de instalación para tu sistema operativo.

Una vez que tengas Git instalado, hay algunas "terminologías" que es necesario conocer. 

Un repositorio Git es el lugar donde se almacena el código fuente de tu proyecto. Puedes crear un repositorio nuevo o clonar uno existente desde un repositorio remoto, como GitHub o Bitbucket.



### Los comandos básicos de Git que debes conocer son los siguientes:

*   **git init**: para crear un nuevo repositorio en una carpeta vacía.
*   **git clone**: para clonar un repositorio existente desde un repositorio remoto.
*   **git add**: para agregar los cambios en tu código al área de preparación.
*   **git commit**: para guardar los cambios en tu repositorio local junto con un * mensaje descriptivo.
* **git push**: para enviar los cambios guardados en tu repositorio local al repositorio remoto.
* **git pull**: para actualizar tu repositorio local con los cambios realizados en el repositorio remoto.
* **git status**: informa si estas up to date o tienes cambios por subir. 

Además Git permite trabajar con ramas **(branch)** para poder trabajar features por separado sin afectar el trabajo comun de la rama principal. **(main)**

El repositorio remoto que vamos a utilizar será **GitHub**




### Para poder usar Github debemos seguir los siguientes pasos: 

1. Crea una cuenta de GitHub en https://github.com/signup y asegúrate de haber iniciado sesión.

2. Crea un nuevo repositorio en GitHub. Haz clic en el botón "Nuevo repositorio" en la página principal de GitHub y dale un nombre a tu repositorio (en este caso, "web_scraper"). También puedes añadir una descripción opcional para el repositorio.

3. Configura Git en tu computadora. Si aún no lo has hecho, instala Git en tu computadora y configura tu nombre y dirección de correo electrónico para que se asocien con tus confirmaciones de Git. 

   Puedes hacer esto con los siguientes comandos en la línea de comando:

```
git config --global user.name "Tu nombre"
git config --global user.email "tu correo electrónico"

```


### Para configurar una clave SSH en GitHub desde tu local, sigue los siguientes pasos:

1. Verifica si ya tienes una clave SSH existente en tu computadora ejecutando el siguiente comando en la línea de comando: `ls -al ~/.ssh` Si ya tienes una clave SSH, verás una lista de archivos que comienzan con "id_rsa" o "id_dsa". Si no tienes una clave SSH, puedes generar una con el siguiente comando: `ssh-keygen -t rsa -b 4096 -C "tu correo electrónico"`.


2. Copia la clave pública de SSH en tu portapapeles dependiendo de tu sistema operativo.

  **Para sistemas Mac**: ` cat ~/.ssh/id_rsa.pub | pbcopy`

  **Para sistemas Linux:** `cat ~/.ssh/id_rsa.pub | xclip -selection clipboard`

  **Para sistemas Windows (usando PowerShell)**: `Get-Content ~/.ssh/id_rsa.pub | Set-Clipboard`


3. Inicia sesión en tu cuenta de GitHub en tu navegador web y navega a la página de configuración de tus claves SSH: https://github.com/settings/keys

   Haz clic en el botón "Nueva clave SSH".

  Dale un nombre descriptivo a tu clave SSH en el campo "Título".


4. Pega la clave pública de SSH que acabas de copiar en el campo "Clave". Asegúrate de que la clave se haya copiado correctamente y que no haya espacios adicionales ni líneas en blanco.

Haz clic en el botón "Agregar clave SSH" para guardar tu clave SSH en tu cuenta de GitHub.

Ahora puedes utilizar la URL de SSH para clonar o hacer push/pull desde tus repositorios de GitHub. 

Por ejemplo, en lugar de usar https://github.com/Usuario/Repositorio.git, utiliza git@github.com:Usuario/Repositorio.git


### Ejemplo luego de haber realizado la configuración de la clave ssh: 

1. **Clonar el repositorio:** `git clone git@github.com:mati-ml-en-produccion/web_scraper.git`

2. **Ejecutar un cambio:** Ejemplo, agregar un archivo con hola_mundo.txt

3. **Agregar el cambio:** `git add .` *(el . significa que agregue todos los archivos o se le puede especificcar un nombre)* 

4. **Guardar los cambios en el repositorio local con un mensaje descriptivo:** `git commit - m "first commit"`

5. **Subir los cambios al repositorio remoto:** `git push` 

Si todo está OK deberiamos ver nuestro cambio en la web de GitHub.



# Docker

Docker es una plataforma de virtualización de contenedores que permite a los desarrolladores crear, implementar y ejecutar aplicaciones de manera aislada en un entorno seguro y reproducible.


### Descarga e instala Docker en tu sistema operativo. 

Puedes descargar Docker Desktop para Windows o Mac desde la página oficial de Docker: https://www.docker.com/products/docker-desktop. Para sistemas Linux, sigue las instrucciones de instalación específicas para tu distribución.

Familiarízate con los conceptos básicos de Docker, como imágenes, contenedores y volúmenes. Puedes consultar la documentación oficial de Docker para obtener más información: https://docs.docker.com/get-started/

### Para crear una imagen de Docker, necesitarás seguir los siguientes pasos:

1. Crea un archivo **Dockerfile** que describa cómo construir la imagen. 

  El archivo Dockerfile es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir la imagen. 

  El Dockerfile debe incluir información sobre la base de la imagen, los comandos necesarios para instalar las **dependencias** de la aplicación y cualquier otra configuración necesaria.

  ⚠ **Ubica el archivo Dockerfile en el directorio raíz de tu proyecto.**


2. Ejecuta el comando **docker build** para construir la imagen. 
El comando docker build toma como argumento la ruta al directorio que contiene el archivo Dockerfile. Ejemplo: `docker build -t web_scraper:latest .`

3. Ejecuta el comando **docker run** y especifica la imagen que deseas utilizar. 
  El argumento `-rm` del comando docker run indica a Docker que elimine automáticamente el contenedor después de que se detenga.
  Ejemplo: `docker run --rm web_scraper:latest`

Puedes usar el dashboard para ver tus contenedores, imagenes y volumenes 


### Además del Dockerfile, para ejecutar un contenedor Docker para una aplicación Python necesitarás lo siguiente:


1. **Tu código fuente**: Deberás tener el código fuente de tu aplicación disponible para incluirlo en la imagen de Docker. Asegúrate de incluir cualquier archivo o dependencia necesaria para ejecutar la aplicación.

2. **Dependencias:** Asegúrate de tener un archivo de requisitos (como `requirements.txt`) que enumere todas las dependencias de Python que necesita tu aplicación. El archivo debe incluir todas las bibliotecas y módulos que necesitas para ejecutar tu aplicación.

3. **Comando de inicio:** Deberás especificar el comando de inicio que Docker utilizará para ejecutar tu aplicación. Para una aplicación Python, el comando de inicio suele ser algo así como python app.py.

4. **Puerto de escucha:** Si tu aplicación escucha en un puerto específico, asegúrate de exponer ese puerto al contenedor Docker. Puedes hacer esto utilizando el argumento -p del comando docker run. Por ejemplo, docker run -p 8080:8080 nombre_de_la_imagen expondrá el puerto 8080 del contenedor al puerto 8080 del host. Sino, por defecto se asigna el puerto 3000

# Dependencias de Python

Las dependencias de Python son módulos o bibliotecas que una aplicación de Python utiliza para su correcto funcionamiento. 

En Python, las dependencias se administran mediante el administrador de paquetes pip. 


Pip es una herramienta de línea de comandos que se utiliza para descargar e instalar paquetes de Python desde el Python Package Index (PyPI), que es un repositorio de paquetes de software de Python. 

Pip permite a los desarrolladores de Python definir las dependencias de su aplicación en un archivo de requisitos (`requirements.txt`), que enumera todas las bibliotecas y módulos necesarios para ejecutar la aplicación.

Las dependencias son importantes porque permiten a los desarrolladores de Python reutilizar el código existente en sus propias aplicaciones, lo que acelera el proceso de desarrollo y reduce los errores. 


### Dentro del requirements.txt

Bibliotecas de Python: Se enumeran las bibliotecas de terceros que se utilizan en la aplicación, junto con sus versiones específicas (si no se encuentra la versión especificada el sistema se encargara de tomar la versión). 

Por ejemplo, `requests==2.26.0` especifica la biblioteca Requests en la versión 2.26.0. y `requests`, no especifica la versión. 

# Conectarte a Azure desde tu entorno local. 

1.   Abre una terminal en tu máquina local.

2.   Instala el CLI de Azure siguiendo las instrucciones que se encuentran en la documentación oficial: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

3. Después de instalar el CLI de Azure, ejecuta el siguiente comando en la terminal para iniciar sesión en tu cuenta de Azure:  `az login --use-device-code`

   **Para Mac:** `brew update && brew install azure-cli`

   **Para Windows:** [Windows Installer](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)

   **Para Linux:** [Linux Installer](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
)

  El comando `az login --use-device-code` abrirá una ventana de tu navegador predeterminado y te pedirá que inicies sesión en tu cuenta de Azure. 

Luego de eso te habras autenticado correctamente con **AzureCloud**
