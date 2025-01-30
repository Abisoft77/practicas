from flask import Flask, render_template, request, jsonify
import pdfplumber  
import io
from pdf_utils import extraer_fecha, extraer_numero_dte, extraer_nit_proveedor, extraer_total  # Agregar extraer_total


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/extract-info', methods=['POST'])
def extract_info():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No se ha subido ningún archivo PDF'})
    
    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        return jsonify({'error': 'Archivo no seleccionado'})
    
    try:
        texto_completo = ""
        with pdfplumber.open(io.BytesIO(pdf_file.read())) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_completo += texto + "\n"
        
        return jsonify({
            'fecha': extraer_fecha(texto_completo),
            'numero_dte': extraer_numero_dte(texto_completo),
            'nit_proveedor': extraer_nit_proveedor(texto_completo),  
            'total': extraer_total(texto_completo)  

        })
        
    except Exception as e:
        return jsonify({'error': f'Error procesando PDF: {str(e)}'})

@app.route('/submit', methods=['POST'])
def submit():
    datos = {
        'fecha': request.form['fecha_emision'],
        'factura': request.form['numero_factura'],
        'nombre': request.form['nombre_cliente'],
        'total': request.form['total_factura'],
        'nit': request.form['nit_proveedor'],
        'pdf': None
    }
    
    if 'pdf_factura' in request.files:
        pdf_file = request.files['pdf_factura']
        if pdf_file.filename != '':
            datos['pdf'] = {
                'filename': pdf_file.filename,
                'size': len(pdf_file.read())
            }
    
    return render_template('result.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)