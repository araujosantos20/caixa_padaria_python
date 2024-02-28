import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap


class GuiDuasColunas(QWidget):

    

    def __init__(self):
        super().__init__()
        self.total = 0.0
        self.linha = 0

        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa da Padaria")

        layoutVerEs = QVBoxLayout()
        layoutVerDI = QVBoxLayout()
        layoutHor = QHBoxLayout()

        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#0E4B20}")
        labelColEsq.setFixedWidth(800)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#683127}")
        labelColDir.setFixedWidth(800)

        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("logo_padaria.jpg"))
        labelLogo.setScaledContents(True)
        layoutVerEs.addWidget(labelLogo)

        labelCodigo = QLabel("Código do produto:")
        labelCodigo.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelNomeProduto = QLabel("Nome do produto:")
        labelNomeProduto.setStyleSheet("QLabel{color:white;font-size:15pt; width:400}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelDescricaoProduto = QLabel("Descrição do produto:")
        labelDescricaoProduto.setStyleSheet("QLabel{color:white;font-size:15pt; width:400}")
        self.descricaoProdutoEdit = QLineEdit()
        self.descricaoProdutoEdit.setFixedHeight(100)
        self.descricaoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelQuantidadeProduto = QLabel("Quantidade do produto:")
        labelQuantidadeProduto.setStyleSheet("QLabel{color:white;font-size:15pt; width:400}")
        self.quantidadeProdutoEdit = QLineEdit()
        self.quantidadeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelPrecoProduto = QLabel("Preço Unitário do produto:")
        labelPrecoProduto.setStyleSheet("QLabel{color:white;font-size:15pt; width:400}")
        self.precoProdutoEdit = QLineEdit()
        self.precoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        labelSubtotalProduto = QLabel("Sub Total:")
        labelSubtotalProduto.setStyleSheet("QLabel{color:white;font-size:15pt; width:400}")
        self.subtotalProdutoEdit = QLineEdit("Tecle F3 para calcular o subtotal")
        # Desabilitar a caixa do subtotal
        self.subtotalProdutoEdit.setEnabled(False)
        self.subtotalProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt; width:400}")

        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)

        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)

        layoutVerEs.addWidget(labelDescricaoProduto)
        layoutVerEs.addWidget(self.descricaoProdutoEdit)

        layoutVerEs.addWidget(labelQuantidadeProduto)
        layoutVerEs.addWidget(self.quantidadeProdutoEdit)

        layoutVerEs.addWidget(labelPrecoProduto)
        layoutVerEs.addWidget(self.precoProdutoEdit)

        layoutVerEs.addWidget(labelSubtotalProduto)
        layoutVerEs.addWidget(self.subtotalProdutoEdit)

        labelColEsq.setLayout(layoutVerEs)

        # Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)

        # Criando o cabeçalho para a tabela resumo
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitário","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        labelTotalPagar = QLabel("Total a Pagar")
        labelTotalPagar.setStyleSheet("QLabel{color:#0F1189;font-size:25pt}")
        self.totalPagarEdit = QLineEdit("0,00")
        self.totalPagarEdit.setEnabled(False)
        self.totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:50pt; width:400}")

        layoutVerDI.addWidget(self.tbResumo)
        layoutVerDI.addWidget(labelTotalPagar)
        layoutVerDI.addWidget(self.totalPagarEdit)

        labelColDir.setLayout(layoutVerDI)



        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)

        self.setLayout(layoutHor)

        # Capturando a tecla que o usuário está digitando e
        # Chamando a função(keyPressEvent) para exevutar um comando quando está tecla
        # for acionada.
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self, e):

        if (e.key() == Qt.Key_F2):
            print("Você teclou F2")
            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.quantidadeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.precoProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.subtotalProdutoEdit.text())))
            self.linha+=1

            self.total+=float(self.subtotalProdutoEdit.text())
            self.totalPagarEdit.setText(str(self.total))

            # Limpar os lineEdit
            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.descricaoProdutoEdit.setText("")
            self.quantidadeProdutoEdit.setText("")
            self.precoProdutoEdit.setText("")
            self.subtotalProdutoEdit.setText("Tecle F3 para calcular o subtotal")
        elif(e.key() == Qt.Key_F3):
            qtd = self.quantidadeProdutoEdit.text()
            prc = self.precoProdutoEdit.text()
            res = float(qtd) * float(prc)
            self.subtotalProdutoEdit.setText(str(res))

app = QApplication(sys.argv)
janela = GuiDuasColunas()
janela.show()
app.exec_()