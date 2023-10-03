import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView,QFileDialog, QMessageBox
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

        
        self.cargar_datos_btn.clicked.connect(self.cargar_datos_desde_excel)
        self.exportar_pdf_btn.clicked.connect(self.exportar_a_pdf)
        


    def cargar_datos_desde_excel(self):
        try:

            opciones = QFileDialog.Options()
            opciones |= QFileDialog.ReadOnly
            archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de Excel", "", "Archivos de Excel (*.xlsx *.xls);;Todos los archivos (*)", options=opciones)
            
            if archivo:
                # Aquí puedes trabajar con el archivo de Excel seleccionado, por ejemplo, imprimir la ruta
                print(f"Archivo seleccionado: {archivo}")
                # Cambia 'archivo_excel.xlsx' al nombre de tu archivo Excel y la hoja que deseas leer.
                df = pd.read_excel(archivo, sheet_name='Hoja1')
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
                            item.setBackground(QColor(240, 62, 24))  # Color rojo para valores menores a 30
                        elif cell_data == "Presente":
                            item.setBackground(QColor(132, 239, 26))  # Color verde para valores mayores a 30
                        elif cell_data == "Latente":
                            item.setBackground(QColor(239, 168, 26))
                        self.tabla.setItem(index, col_idx, item)


                self.tabla.horizontalHeader().setStretchLastSection(True)
                #self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #### Centro Titulos #################33
                dfCentros = pd.DataFrame()
                dfCentros['Centros'] = ['Físico (N1,N8,N9)', 'Emocional (N2,N3,N4)','Intelectual (N5,N6,N7)']
                fila1 = int(df['Puntaje'][0])+int(df['Puntaje'][7])+int(df['Puntaje'][8])
                fila2 = int(df['Puntaje'][1])+int(df['Puntaje'][2])+int(df['Puntaje'][3])
                fila3 = int(df['Puntaje'][4])+int(df['Puntaje'][5])+int(df['Puntaje'][6])

                lista = [fila1,fila2,fila3]
                dfCentros['Resultado'] = lista
                columnas = dfCentros.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaCentro.setColumnCount(len(columnas))
                self.tablaCentro.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaCentro.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfCentros.iterrows():
                    self.tablaCentro.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        
                        self.tablaCentro.setItem(index, col_idx, item)

                self.tablaCentro.horizontalHeader().setStretchLastSection(True)
                self.tablaCentro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #########################################################
    #### Centro Resultados ############
                dfCentrosR = pd.DataFrame()

                revision = lambda x: "Desequilibrio" if x >= 15 else "Equilibrio"

                dfCentrosR['Físico / Emocional'] = [abs(fila1-fila2), revision(abs(fila1-fila2))]
                dfCentrosR['Físico / Intelectual'] = [abs(fila1-fila3), revision(abs(fila1-fila3))]
                dfCentrosR['Emocional / Intelectual'] = [abs(abs(fila2-fila3)), revision(abs(fila2-fila3))]

                columnas = dfCentrosR.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaCentroR.setColumnCount(len(columnas))
                self.tablaCentroR.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaCentroR.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfCentrosR.iterrows():
                    self.tablaCentroR.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        if cell_data == "Equilibrio":
                            item.setBackground(QColor(132, 239, 26))  # Color rojo para valores menores a 30
                        elif cell_data == "Desequilibrio":
                            item.setBackground(QColor(240, 62, 24))  # Color verde para valores mayores a 30
                        self.tablaCentroR.setItem(index, col_idx, item)

                self.tablaCentroR.horizontalHeader().setStretchLastSection(True)
                self.tablaCentroR.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ##############################################################3##333zzzz
    #### Energias titulos ##########3
                dfEnergias = pd.DataFrame()
                dfEnergias['Energías'] = ['Interna (N1,N4,N5)', 'Externa (N2,N7,N8)','Equilibrio (N3,N6,N9)']
                fila1 = int(df['Puntaje'][0])+int(df['Puntaje'][3])+int(df['Puntaje'][4])
                fila2 = int(df['Puntaje'][1])+int(df['Puntaje'][6])+int(df['Puntaje'][7])
                fila3 = int(df['Puntaje'][2])+int(df['Puntaje'][5])+int(df['Puntaje'][8])

                lista = [fila1,fila2,fila3]
                dfEnergias['Resultado'] = lista
                columnas = dfEnergias.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaEnergia.setColumnCount(len(columnas))
                self.tablaEnergia.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaEnergia.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfEnergias.iterrows():
                    self.tablaEnergia.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        
                        self.tablaEnergia.setItem(index, col_idx, item)

                self.tablaEnergia.horizontalHeader().setStretchLastSection(True)
                self.tablaEnergia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                

    #########################################################
    #### Centro Resultados ############
                dfEnergiasR = pd.DataFrame()

                dfEnergiasR['Interna / Externa'] = [abs(fila1-fila2), revision(abs(fila1-fila2))]
                dfEnergiasR['Interna / Equilibrio'] = [abs(fila1-fila3), revision(abs(fila1-fila3))]
                dfEnergiasR['Externa / Equilibrio'] = [abs(abs(fila2-fila3)), revision(abs(fila2-fila3))]

                columnas = dfEnergiasR.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaEnergiaR.setColumnCount(len(columnas))
                self.tablaEnergiaR.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaEnergiaR.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfEnergiasR.iterrows():
                    self.tablaEnergiaR.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        if cell_data == "Equilibrio":
                            item.setBackground(QColor(132, 239, 26))  # Color rojo para valores menores a 30
                        elif cell_data == "Desequilibrio":
                            item.setBackground(QColor(240, 62, 24))  # Color verde para valores mayores a 30
                        self.tablaEnergiaR.setItem(index, col_idx, item)

                self.tablaEnergiaR.horizontalHeader().setStretchLastSection(True)
                self.tablaEnergiaR.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #########################################################
    #### Espejos ############

                dfEspejos = pd.DataFrame()
                
                dfEspejos['Espejos'] = ['Cumplimiento', 'Socialización','Logro', 'Interiorización']
                fila1 = int(df['Puntaje'][0])+int(df['Puntaje'][5])
                fila2 = int(df['Puntaje'][1])+int(df['Puntaje'][6])
                fila3 = int(df['Puntaje'][2])+int(df['Puntaje'][7])
                fila4 = int(df['Puntaje'][3])+int(df['Puntaje'][4])

                lista = [fila1,fila2,fila3, fila4]
                dfEspejos['Resultado'] = lista

                fila12 = round((int(df['Puntaje'][0])*100)/fila1)
                fila22 = round((int(df['Puntaje'][1])*100)/fila2)
                fila32 = round((int(df['Puntaje'][2])*100)/fila3)
                fila42 = round((int(df['Puntaje'][3])*100)/fila4)

                lista = [f"{fila12}%",f"{fila22}%",f"{fila32}%", f"{fila42}%"]
                dfEspejos['Aporte N1,N2,N3,N4 (%)'] = lista

                fila12 = round((int(df['Puntaje'][5])*100)/fila1)
                fila22 = round((int(df['Puntaje'][6])*100)/fila2)
                fila32 = round((int(df['Puntaje'][7])*100)/fila3)
                fila42 = round((int(df['Puntaje'][4])*100)/fila4)

                lista = [f"{fila12}%",f"{fila22}%",f"{fila32}%", f"{fila42}%"]
                dfEspejos['Aporte N6,N7,N8,N5 (%)'] = lista

                resultado = lambda x: "Minimizado" if x < 30 else ("Maximizado" if x > 36 else "Óptimo")
                lista = [resultado(fila1),resultado(fila2),resultado(fila3), resultado(fila4)]
                dfEspejos['Espejo'] = lista

                columnas = dfEspejos.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaEspejo.setColumnCount(len(columnas))
                self.tablaEspejo.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaEspejo.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfEspejos.iterrows():
                    self.tablaEspejo.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        if cell_data == "Óptimo":
                            item.setBackground(QColor(132, 239, 26))  # Color rojo para valores menores a 30
                        elif cell_data == "Minimizado":
                            item.setBackground(QColor(240, 62, 24))  # Color verde para valores mayores a 30
                        elif cell_data == "Maximizado":
                            item.setBackground(QColor(255, 80, 40)) 
                        self.tablaEspejo.setItem(index, col_idx, item)

                self.tablaEspejo.horizontalHeader().setStretchLastSection(True)
                self.tablaEspejo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #########################################################
    #### Antagonismos ############

                dfAntagonismos = pd.DataFrame()
                dfAntagonismos['Antagonismos'] = ['Libertad vs Autenticidad','Calidad vs Oportunidad','Dirección vs Seguimiento','Socialización vs Aislamiento']

                fila1 = abs(int(df['Puntaje'][6])-int(df['Puntaje'][3]))
                fila2 = abs(int(df['Puntaje'][2])-int(df['Puntaje'][0]))
                fila3 = abs(int(df['Puntaje'][5])-int(df['Puntaje'][7]))
                fila4 = abs(int(df['Puntaje'][1])-int(df['Puntaje'][4]))

                lista = [fila1,fila2,fila3,fila4]
                dfAntagonismos['Diferencia'] = lista

                fila1 = df['Dispersión'][6]
                fila2 = df['Dispersión'][0]
                fila3 = df['Dispersión'][7]
                fila4 = df['Dispersión'][1]

                lista = [fila1,fila2,fila3,fila4]
                dfAntagonismos['Estado N7,N1,N8,N2'] = lista

                fila12 = df['Dispersión'][3]
                fila22 = df['Dispersión'][2]
                fila32 = df['Dispersión'][5]
                fila42 = df['Dispersión'][4]

                lista = [fila12,fila22,fila32,fila42]
                dfAntagonismos['Estado N4,N3,N6,N5'] = lista

                resultado = lambda x, y: "Tensión" if x == "Presente" and y == "Presente" else "No tensión"

                lista = [resultado(fila1, fila12),resultado(fila2, fila22),resultado(fila3, fila32),resultado(fila4, fila42)]

                dfAntagonismos['Resultado'] = lista

                dfAntagonismos['N9'] = df['Dispersión'][8]

                print(dfAntagonismos['N9'])

                columnas = dfAntagonismos.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaAntagonismo.setColumnCount(len(columnas))
                self.tablaAntagonismo.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaAntagonismo.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfAntagonismos.iterrows():
                    self.tablaAntagonismo.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        if cell_data == "No tensión":
                            item.setBackground(QColor(132, 239, 26))
                        elif cell_data == "Tensión":
                            item.setBackground(QColor(240, 62, 24))

                        self.tablaAntagonismo.setItem(index, col_idx, item)

                self.tablaAntagonismo.horizontalHeader().setStretchLastSection(True)
                self.tablaAntagonismo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    #########################################################
    #### Eneatipo 2 ############

                dfEneatipos = pd.DataFrame()

                dfEneatipos.index.name = 'Eneatipos'
                dfEneatipos['Denominación'] = df['Eneatipo']
                dfEneatipos['Resultado'] = df['Puntaje']
                dfEneatipos['Integración'] = [7, 4, 6, 1, 8, 9, 5, 2, 3]
                dfEneatipos['Desintegración'] = [4, 8, 9, 2, 7, 3, 1, 5, 6]
                dfEneatipos['Centro'] = ['Físico', 'Emocional', 'Emocional', 'Emocional', 'Intelectual', 'Intelectual', 'Intelectual', 'Físico', 'Físico']
                dfEneatipos['Energía'] = ['Interna', 'Externa', 'Equilibrio', 'Interna', 'Interna', 'Equilibrio', 'Externa', 'Externa', 'Equilibrio']

                columnas = dfEneatipos.columns.tolist()

                # Configura el número de columnas y sus etiquetas en la QTableWidget
                self.tablaEneatipos.setColumnCount(len(columnas))
                self.tablaEneatipos.setHorizontalHeaderLabels(columnas)

                # Limpia la tabla
                self.tablaEneatipos.setRowCount(0)

                # Agrega los datos del DataFrame a la QTableWidget
                for index, row_data in dfEneatipos.iterrows():
                    self.tablaEneatipos.insertRow(index)
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data))
                        
                        self.tablaEneatipos.setItem(index, col_idx, item)

                self.tablaEneatipos.horizontalHeader().setStretchLastSection(True)
                self.tablaEneatipos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)





            



        except Exception as e:
            QMessageBox.critical(self, 'Error al cargar datos desde Excel', f'{str(e)}')
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
