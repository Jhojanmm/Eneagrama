import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import landscape


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("eneagrama.ui", self)

        self.setWindowTitle("Exportar a PDF")

        
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])

        
        self.cargar_datos_btn.clicked.connect(self.cargar_datos_desde_excel)

        
        self.exportar_pdf_btn.clicked.connect(self.exportar_a_pdf)

    

    def cargar_datos_desde_excel(self):
        try:
            # Cambia 'archivo_excel.xlsx' al nombre de tu archivo Excel y la hoja que deseas leer.
            df = pd.read_excel('archivos/archivo.xlsx', sheet_name='Hoja1')
            df['Eneatipo'] = ['Perfeccionista', 'Colaborador', 'Competitivo', 'Creativo', 'Analítico', 'Comprometido', 'Dinámico', 'Líder', 'Conciliador']
            df['Dispersión'] = df['Puntaje'].apply(lambda x: 'Presente' if x > 16 else ('Latente' if x == 16 else 'Ausente'))
            df['centro'] = ['Físico', 'Emocional', 'Emocional', 'Emocional', 'Intelectual', 'Intelectual', 'Intelectual', 'Físico', 'Físico']
            df['Energia'] = ['Interna', 'Externa', 'Equilibrio', 'Interna', 'Interna', 'Equilibrio', 'Externa', 'Externa', 'Equilibrio']
            df['Motivación'] = ['Cumplir', 'Aceptación', 'Éxito', 'Autenticidad', 'Conocimiento', 'Seguridad', 'Diversión', 'Influir', 'Paz']
            df['Virtud'] = ['Serenidad', 'Humildad', 'Veracidad', 'Ecuanimidad', 'Desapego', 'Coraje', 'Sobriedad', 'Inocencia', 'Acción']
            df['Miedo'] = ['No cumplir', 'Rechazo', 'Fracaso', 'Ser uno más', 'Ignorancia', 'Amenazas', 'Aburrimiento', 'Descontrol', 'Caos']
            df['Trampa'] = ['Perfección', 'Servicio', 'Eficiencia', 'Ser único', 'Conocimiento', 'Seguridad', 'Idealismo', 'Justicia', 'Búsqueda']
            df['Imagen ideal'] = ['Estoy en lo correcto', 'Soy de utilidad', 'Soy exitoso', 'Soy diferente', 'Soy perceptivo', 'Cumplo con mi deber', 'Estoy Feliz', 'Tengo poder', 'Estoy de acuerdo']
            df['Evita'] = ['Furia', 'Sus necesidades', 'Fallar', 'Sentirse perdido', 'Vacío', 'Soledad', 'Pena emocional', 'Debilidad', 'Conflicto']
            df['Estilo de hablar'] = ['Enseñado, moralizado', 'Haciendo alarde, aconsejando', 'Promoviendo, empujando', 'Lamentando, historias tristes', 'Explicando, sistematizando', 'Con precaución, en Grupo', 'Anécdotas, cuentos', 'Con mando, imperativo', 'Monótono, Sagaz']

            df['Puntaje'] = df['Puntaje'].astype(str)
            # Obtén los nombres de las columnas del DataFrame
            columnas = df.columns.tolist()

            # Configura el número de columnas y sus etiquetas en la QTableWidget
            self.tabla.setColumnCount(len(columnas))
            self.tabla.setHorizontalHeaderLabels(columnas)

            # Limpia la tabla
            self.tabla.setRowCount(0)

            # Agrega los datos del DataFrame a la QTableWidget
            for index, row_data in df.iterrows():
                self.tabla.insertRow(index)
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    if cell_data == "Ausente":
                        item.setBackground(QColor(132, 239, 26))  # Color rojo para valores menores a 30
                    elif cell_data == "Presente":
                        item.setBackground(QColor(240, 62, 24))  # Color verde para valores mayores a 30
                    elif cell_data == "Latente":
                        item.setBackground(QColor(239, 168, 26))
                    self.tabla.setItem(index, col_idx, item)

            

        except Exception as e:
            print("Error al cargar datos desde Excel:", str(e))

    

        

    
    def exportar_a_pdf(self):
        filename = "tabla.pdf"
        doc = SimpleDocTemplate(filename, pagesize=landscape(letter))

        # Estilos de párrafo para ajustar el texto en las celdas
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.alignment = 1  # Alineación centrada

        # Obtener los datos de la tabla, incluyendo los nombres de las columnas
        data = []
        
        # Obtener los nombres de las columnas
        header_row = []
        for col in range(self.tabla.columnCount()):
            header_item = self.tabla.horizontalHeaderItem(col)
            header_text = header_item.text()
            p = Paragraph(header_text, style)
            header_row.append(p)
        
        data.append(header_row)  # Agregar la fila de encabezado
        
        # Obtener los datos de las filas y aplicar colores según los valores
        for row in range(self.tabla.rowCount()):
            row_data = []
            for col in range(self.tabla.columnCount()):
                item = self.tabla.item(row, col)
                # Obtener el texto del elemento y crear un párrafo con estilo
                cell_text = item.text()
                p = Paragraph(cell_text, style)
                row_data.append(p)

            data.append(row_data)

        # Crear una tabla en el PDF
        table = Table(data)
        style = TableStyle([
            # Estilos de tabla (incluyendo bordes)
            ('BACKGROUND', (0, 0), (-1, 0), colors.aliceblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
            # Añadir bordes a todas las celdas
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        # Aplicar colores de fondo a celdas específicas
        for row in range(1, len(data)):
            for col in range(len(data[row])):
                cell_text = data[row][col].getPlainText()
                if cell_text == "Latente":
                    cell_color = colors.orange
                elif cell_text == "Presente":
                    cell_color = colors.green
                elif cell_text == "Ausente":
                    cell_color = colors.red
                else:
                    cell_color = colors.white  # Color de fondo predeterminado
                style.add('BACKGROUND', (col, row), (col, row), cell_color)

        table.setStyle(style)

        elements = []
        elements.append(table)
        doc.build(elements)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    ventana.show()
    sys.exit(app.exec_())
