# eQSL Image Downloader

Este programa simplifica la descarga automática de archivos ADIF y de imágenes QSL desde eQSL.cc. Está diseñado para radioaficionados que buscan una manera eficiente de gestionar sus confirmaciones QSL electrónicas.

## Características

- Descarga automática de archivos ADIF de la bandeja de entrada de eQSL.cc.
- Descarga de imágenes QSL correspondientes a cada QSO registrado en el archivo ADIF.
- Organización y almacenamiento local de archivos e imágenes descargados.

## Pre-requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes librerías en tu entorno Python:

- `python-dotenv`: Para la gestión de variables de entorno.
- `Beautiful Soup 4`: Para el procesamiento de datos HTML y XML.
- `adif_io`: Para la lectura y manipulación de archivos ADIF.
- `requests`: Para realizar peticiones HTTP.

Puedes instalar estas librerías utilizando el siguiente comando:

```bash
pip install python-dotenv beautifulsoup4 adif_io requests
```

## Configuración

Para utilizar este programa, necesitas crear un archivo `.env` en el directorio raíz del proyecto con las siguientes variables:

```
callsign=TU_INDICATIVO_DE_EQSL
password=TU_CONTRASEÑA_DE_EQSL
```

Reemplaza `TU_INDICATIVO_DE_EQSL` y `TU_CONTRASEÑA_DE_EQSL` con tu indicativo de radioaficionado y tu contraseña de eQSL.cc, respectivamente.

## Uso

Para ejecutar el programa, simplemente navega hasta el directorio del proyecto y ejecuta el script principal:

```bash
python eQSL_Image_Downloader.py
```

El programa realizará los siguientes pasos automáticamente:

1. Descargará el archivo ADIF de tu bandeja de entrada en eQSL.cc.
2. Leerá el archivo ADIF descargado y extraerá la información de los QSOs.
3. Descargará las imágenes QSL para cada QSO encontrado.
4. Guardará los archivos e imágenes en carpetas locales organizadas.

## Contribuir

Las contribuciones son bienvenidas. Si tienes alguna sugerencia para mejorar este proyecto, siéntete libre de crear un pull request o abrir un issue.

