import cv2
import pytesseract
import numpy as np
from PIL import Image

def procesar_imagen(imagen_path):
    # Preprocesamiento para mejorar OCR
    img = cv2.imread(imagen_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extraer_texto_de_imagen(imagen_path):
    try:
        # Preprocesar imagen
        imagen_procesada = procesar_imagen(imagen_path)
        
        # Configurar Tesseract
        custom_config = r'--oem 3 --psm 6 -l spa'
        texto = pytesseract.image_to_string(imagen_procesada, config=custom_config)
        return texto
    except Exception as e:
        raise RuntimeError(f"Error en OCR: {str(e)}")