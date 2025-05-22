import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, QMenu,
                             QFileDialog, QMessageBox, QFontDialog, QFontComboBox,
                             QSpinBox, QHBoxLayout, QWidget, QVBoxLayout, QPushButton,
                             QInputDialog)
from PyQt6.QtGui import QAction, QKeySequence, QFont
from PyQt6.QtCore import Qt

class NotDefteri(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Not Defteri")
        self.setGeometry(100, 100, 800, 600)

        self.metin_alani = QTextEdit()
        self.setCentralWidget(self.metin_alani)

        self._create_menu_bar()
        self._create_toolbar()
        self._create_context_menu()

        self.dosya_adi = None

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        # Dosya Menüsü
        dosya_menu = QMenu("Dosya", self)
        yeni_action = QAction("Yeni", self)
        yeni_action.setShortcut(QKeySequence.StandardKey.New)
        yeni_action.triggered.connect(self.yeni_dosya)
        ac_action = QAction("Aç...", self)
        ac_action.setShortcut(QKeySequence.StandardKey.Open)
        ac_action.triggered.connect(self.dosya_ac)
        kaydet_action = QAction("Kaydet", self)
        kaydet_action.setShortcut(QKeySequence.StandardKey.Save)
        kaydet_action.triggered.connect(self.dosya_kaydet)
        farkli_kaydet_action = QAction("Farklı Kaydet...", self)
        farkli_kaydet_action.triggered.connect(self.dosya_farkli_kaydet)
        kapat_action = QAction("Kapat", self)
        kapat_action.setShortcut(QKeySequence.StandardKey.Close)
        kapat_action.triggered.connect(self.close)

        dosya_menu.addAction(yeni_action)
        dosya_menu.addAction(ac_action)
        dosya_menu.addAction(kaydet_action)
        dosya_menu.addAction(farkli_kaydet_action)
        dosya_menu.addSeparator()
        dosya_menu.addAction(kapat_action)
        menu_bar.addMenu(dosya_menu)

        # Düzen Menüsü
        duzen_menu = QMenu("Düzen", self)
        kes_action = QAction("Kes", self)
        kes_action.setShortcut(QKeySequence.StandardKey.Cut)
        kes_action.triggered.connect(self.metin_alani.cut)
        kopyala_action = QAction("Kopyala", self)
        kopyala_action.setShortcut(QKeySequence.StandardKey.Copy)
        kopyala_action.triggered.connect(self.metin_alani.copy)
        yapistir_action = QAction("Yapıştır", self)
        yapistir_action.setShortcut(QKeySequence.StandardKey.Paste)
        yapistir_action.triggered.connect(self.metin_alani.paste)

        duzen_menu.addAction(kes_action)
        duzen_menu.addAction(kopyala_action)
        duzen_menu.addAction(yapistir_action)
        menu_bar.addMenu(duzen_menu)

        # Biçim Menüsü
        bicim_menu = QMenu("Biçim", self)
        yazi_tipi_action = QAction("Yazı Tipi...", self)
        yazi_tipi_action.triggered.connect(self.yazi_tipini_degistir)
        bicim_menu.addAction(yazi_tipi_action)
        menu_bar.addMenu(bicim_menu)

        self.setMenuBar(menu_bar)

    def _create_toolbar(self):
        toolbar = self.addToolBar("Araç Çubuğu")

        # Yeni Dosya Butonu
        yeni_btn = QPushButton("Yeni")
        yeni_btn.clicked.connect(self.yeni_dosya)
        toolbar.addWidget(yeni_btn)

        # Aç Butonu
        ac_btn = QPushButton("Aç")
        ac_btn.clicked.connect(self.dosya_ac)
        toolbar.addWidget(ac_btn)

        # Kaydet Butonu
        kaydet_btn = QPushButton("Kaydet")
        kaydet_btn.clicked.connect(self.dosya_kaydet)
        toolbar.addWidget(kaydet_btn)

        # Kapat Butonu
        kapat_btn = QPushButton("Kapat")
        kapat_btn.clicked.connect(self.close)
        toolbar.addWidget(kapat_btn)

        toolbar.addSeparator()

        # Kes Butonu
        kes_btn = QPushButton("Kes")
        kes_btn.clicked.connect(self.metin_alani.cut)
        toolbar.addWidget(kes_btn)

        # Kopyala Butonu
        kopyala_btn = QPushButton("Kopyala")
        kopyala_btn.clicked.connect(self.metin_alani.copy)
        toolbar.addWidget(kopyala_btn)

        # Yapıştır Butonu
        yapistir_btn = QPushButton("Yapıştır")
        yapistir_btn.clicked.connect(self.metin_alani.paste)
        toolbar.addWidget(yapistir_btn)

        toolbar.addSeparator()

        # Yazı Tipi Seçici
        font_combo = QFontComboBox()
        font_combo.currentFontChanged.connect(self.metin_alani.setCurrentFont)
        toolbar.addWidget(font_combo)

        # Yazı Boyutu Seçici
        size_spin = QSpinBox()
        size_spin.setRange(8, 48)
        size_spin.setValue(12)
        size_spin.valueChanged.connect(lambda s: self.metin_alani.setFontPointSize(s))
        toolbar.addWidget(size_spin)

    def _create_context_menu(self):
        self.metin_alani.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.metin_alani.customContextMenuRequested.connect(self._show_context_menu)

        self.context_menu = QMenu(self)
        kes_action = QAction("Kes", self)
        kes_action.triggered.connect(self.metin_alani.cut)
        kopyala_action = QAction("Kopyala", self)
        kopyala_action.triggered.connect(self.metin_alani.copy)
        yapistir_action = QAction("Yapıştır", self)
        yapistir_action.triggered.connect(self.metin_alani.paste)

        self.context_menu.addAction(kes_action)
        self.context_menu.addAction(kopyala_action)
        self.context_menu.addAction(yapistir_action)

    def _show_context_menu(self, pos):
        self.context_menu.popup(self.metin_alani.mapToGlobal(pos))

    def yeni_dosya(self):
        self.metin_alani.clear()
        self.dosya_adi = None
        self.setWindowTitle("PyQt6 Not Defteri")

    def dosya_ac(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)")
        if dosya_adi:
            try:
                with open(dosya_adi, 'r', encoding='utf-8') as f:
                    icerik = f.read()
                    self.metin_alani.setText(icerik)
                    self.dosya_adi = dosya_adi
                    self.setWindowTitle(f"{self.dosya_adi} - PyQt6 Not Defteri")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Dosya okuma hatası: {e}")

    def dosya_kaydet(self):
        if self.dosya_adi:
            self._dosyaya_kaydet(self.dosya_adi)
        else:
            self.dosya_farkli_kaydet()

    def dosya_farkli_kaydet(self):
        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)")
        if dosya_adi:
            self._dosyaya_kaydet(dosya_adi)

    def _dosyaya_kaydet(self, dosya_adi):
        try:
            with open(dosya_adi, 'w', encoding='utf-8') as f:
                metin = self.metin_alani.toPlainText()
                f.write(metin)
            self.dosya_adi = dosya_adi
            self.setWindowTitle(f"{self.dosya_adi} - PyQt6 Not Defteri")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya yazma hatası: {e}")

    def yazi_tipini_degistir(self):
        font, ok = QFontDialog.getFont(self.metin_alani.currentFont(), self)
        if ok:
            self.metin_alani.setCurrentFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    not_defteri = NotDefteri()
    not_defteri.show()
    sys.exit(app.exec())