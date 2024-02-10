import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import adif_io
import time


def getAdifFromInboxAndReturnFileName(callsign, password):
    # Se usará el método GET para obtener la imagen
    # a una url con el formato:
    # https://www.eQSL.cc/qslcard/DownloadInBox.cfm?UserName=mycall&Password=mypassword&RcvdSince=20050201

    # Se debe reemplazar mycall, mypassword con los valores correspondientes.

    # Creamos la url
    url = f"https://www.eQSL.cc/qslcard/DownloadInBox.cfm?UserName={mycall}&Password={mypassword}&RcvdSince=20050201"

    print(url)
    # Realizamos la petición
    response = requests.get(url)

    # Verificamos si la petición fue exitosa
    if response.status_code == 200 and ("Your ADIF log file has been built" in response.text):
        # Utilizamos BeautifulSoup para analizar el contenido de la respuesta
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos el enlace del archivo .TXT
        link = soup.find('a', href=True, string='.ADI file')
        if link:
            # Extraemos el href o ruta del enlace
            file_url = "https://www.eQSL.cc" + link['href'].replace('..', '')

            # Realizamos la petición para descargar el archivo
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                # Extraemos el nombre del archivo desde el URL
                file_name = file_url.split('/')[-1]

                # Guardamos el contenido del archivo en la carpeta downloads/adifs
                if not os.path.exists('downloads/adifs'):
                    os.makedirs('downloads/adifs')

                file_path = f"downloads/adifs/{file_name}"
                with open(file_path, 'wb') as f:
                    f.write(file_response.content)
                print(f"Archivo {file_name} descargado exitosamente.")
                return file_path

            else:
                print("No se pudo descargar el archivo.")
        else:
            print("Enlace del archivo .TXT no encontrado.")


def downloadQSLImages(mycall, mypassword, qsls):

    # Url tipo HTTPS://www.eqsl.cc/qslcard/GeteQSL.cfm?Username=mycall&Password=mypassword&CallsignFrom=sendercall&QSOBand=20M&QSOMode=SSB&QSOYear=2009&QSOMonth=6&QSODay=1&QSOHour=07&QSOMinute=30

    # Descargamos las imágenes de las QSLs
    for qsl in qsls:
        CallsignFrom = qsl['CALL']
        QSOYear = qsl['QSO_DATE'][0:4]
        QSOMonth = qsl['QSO_DATE'][4:6]
        QSODay = qsl['QSO_DATE'][6:8]
        QSOHour = qsl['TIME_ON'][0:2]
        QSOMinute = qsl['TIME_ON'][2:4]
        QSOBand = qsl['BAND']
        QSOMode = qsl['MODE']

        url = f"https://www.eqsl.cc/qslcard/GeteQSL.cfm?Username={mycall}&Password={mypassword}&CallsignFrom={CallsignFrom}&QSOBand={QSOBand}&QSOMode={QSOMode}&QSOYear={QSOYear}&QSOMonth={QSOMonth}&QSODay={QSODay}&QSOHour={QSOHour}&QSOMinute={QSOMinute}"

        # Descargamos la imagen de la QSL
        response = requests.get(url)

        if response.status_code == 200:

            # Buscamos la imagen en la respuesta
            soup = BeautifulSoup(response.text, 'html.parser')
            img = soup.find('img', src=True)
            if img:
                img_url = "https://www.eqsl.cc" + img['src'].replace('..', '')

                # Guardamos la imagen en la carpeta downloads/qsls
                if not os.path.exists('downloads/qsls'):
                    os.makedirs('downloads/qsls')

                img_path = f"downloads/qsls/{CallsignFrom}_{QSOYear}{QSOMonth}{QSODay}_{QSOHour}{QSOMinute}.jpg"
                with open(img_path, 'wb') as f:
                    f.write(requests.get(img_url).content)
                print(
                    f"Imagen de QSL de {CallsignFrom} descargada exitosamente.")
            else:
                print("Imagen de QSL no encontrada.")

            time.sleep(10)


# main
if __name__ == "__main__":

    # Cargamos el archivo .env
    load_dotenv()

    mycall = os.getenv("callsign")
    mypassword = os.getenv("password")

    adi_file_name = getAdifFromInboxAndReturnFileName(mycall, mypassword)

    # Leemos el archivo ADI desde el archivo descargado
    qsls = adif_io.read_from_file(adi_file_name)[0]

    downloadQSLImages(mycall, mypassword, qsls)

    print("Proceso finalizado.")
