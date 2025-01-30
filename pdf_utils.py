import re

def extraer_fecha(texto):
    patron = r"Fecha y hora de emision:\s*(\d{2}-[a-z]{3}-\d{4})"
    coincidencia = re.search(patron, texto, re.IGNORECASE)
    return coincidencia.group(1) if coincidencia else None

def extraer_numero_dte(texto):
    patron = r"(?:Número de DTE|Número de documento|No\. Documento)[:\s]*(\d+-\d+|\d+)"
    coincidencia = re.search(patron, texto, re.IGNORECASE)
    return coincidencia.group(1) if coincidencia else None

def extraer_nit_proveedor(texto):
    # Patrón que cubre múltiples formatos comunes
    patron = r'(?i)(?:Nit Emisor|NIT|Identificaci[oó]n Tributaria)[:\s]*([0-9A-Z-]+)'
    coincidencia = re.search(patron, texto)
    
    if coincidencia:
        nit = coincidencia.group(1)
        # Limpiar caracteres no deseados
        nit = nit.replace(' ', '').replace('_', '').strip()
        return nit if len(nit) >= 8 else None  # Validación básica de longitud
    return None


def extraer_total(texto):
    # Busca el último valor numérico después de TOTALES:
    patron = r"TOTALES:(?:\s*[\d.,]+){2}\s*([\d.,]+)"
    coincidencia = re.search(patron, texto)
    if coincidencia:
        total = coincidencia.group(1).replace(',', '')
        return float(total)
    return None