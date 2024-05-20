import back_logicel_gestion_stock as bk

from PySide6.QtWidgets import QMessageBox, QDialog

from ui_files.ui_fournisseur_dialog import Ui_fournisseur_dialog


class DialogFournisseur(Ui_fournisseur_dialog, QDialog):
    def __init__(self, parent=None):
        # super().__init__(parent)

        super().__init__()
        self.setupUi(self)
        
    # Add new provider when you press on the ok btn
        self.ok_bouton.clicked.connect(self.add_fournisseur)
        self.annule_buton.clicked.connect(self.close)

    # INSERT NEW CLIENT
    def insert_new_fournisseur(self):
        utilisateur_id = 00
        
        # try:
        nom_fournisseur = self.line_edit_nom.text()
        adresse_fournisseur = self.line_edit_adresse.text()
        contact_fournisseur= int(self.line_edit_contact.text())
        email_fournisseur = self.line_edit_email.text()

        insert = bk.add_fournisseur(nom_fournisseur, adresse_fournisseur, contact_fournisseur, email_fournisseur, utilisateur_id)
        
        self.show_inserted_message(insert)

        # except Exception as e:
        #     print(f"Error: {e}")

    def show_inserted_message(self, ret_insert):
        msg_box = QMessageBox(self)

        # :TODO: the window title doesn't show. Correct it!!

        if ret_insert == "Client ajouté":
            msg_box.setWindowTitle("Succès")
            # msg_box.setIcon(QMessageBox.information)
            msg_box.setText(f"Le client {self.line_edit_nom.text()} a été bien ajouté !")
            msg_box.exec()
        else:
            msg_box.setWindowTitle("Echec")
            # msg_box.setIcon(QMessageBox.warning)
            msg_box.setText(f"Le fournisseur {self.line_edit_nom.text()} n'a pas été ajouté.")
            msg_box.exec()
    
    # Signal sent to the front_page.py that says the user has clicked on the ok button and that
    # it is now ok to insert the fprovider in the db and display it on the front page.
    def add_fournisseur(self):
        self.insert_new_fournisseur()
        self.accept()  # signal sent every time we clicked on the ok btn
