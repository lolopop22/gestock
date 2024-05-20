import back_logicel_gestion_stock as bk

from PySide6.QtWidgets import QMessageBox, QDialog
from PySide6.QtCore import Signal

from ui_files.ui_client_dialog import Ui_client_dialog


class DialogProduit(Ui_client_dialog, QDialog):

    # Define a custom signal as a class variable
    data_updated = Signal()

    def __init__(self, parent=None, row_index=None, row_data=None, type=None):
        # super().__init__(parent)

        super().__init__()
        self.setupUi(self)

        self.type = type
        # store row_index and row_data as instance variables
        self.row_index = row_index
        self.row_data = row_data

        self.client_info = self.select_client()[0]
        print(f"self.client_info: {self.client_info}")

        self.id_client_info = self.client_info[0]
        self.nom_client_info = self.client_info[1]
        self.entreprise_client_info = self.client_info[2]
        self.adresse_client_info = self.client_info[3]
        self.contact_client_info = self.client_info[4]
        self.email_client_info = self.client_info[5]
        self.utilisateur_id_client_info = self.client_info[6]

        if self.type == "update":  # Update client when the ok btn is pressed
            self.setWindowTitle("Mise à jour")
            self.label.setText("Mettre à jour les informations du client")
            self.ok_bouton.clicked.connect(self.update_client)
        elif self.type == "Add":  # Add new client when you press on the ok btn
            self.setWindowTitle("Ajout")
            self.label.setText("Mettre à jour les informations du client")
            self.ok_bouton.clicked.connect(self.add_client)

        print(self.type)
        print(self.windowTitle())
        self.annule_buton.clicked.connect(self.close)

        self.line_edit_nom.setText(str(self.nom_client_info))
        self.line_edit_entreprise.setText(str(self.entreprise_client_info))
        self.line_edit_adresse.setText(str(self.adresse_client_info))
        self.line_edit_contact.setText(str(self.contact_client_info))
        self.line_edit_email.setText(str(self.email_client_info))

    # INSERT NEW CLIENT
    def insert_new_client(self):
        # :TODO: Gérer le cas de l'ID utilisateur...
        utilisateur_id = 00
        
        try:
            nom_client = self.line_edit_nom.text()
            entreprise_client = self.line_edit_entreprise.text()
            adresse_client = self.line_edit_adresse.text()
            contact_client = int(self.line_edit_contact.text())
            email_client = self.line_edit_email.text()

            added = bk.add_client(nom_client, entreprise_client, adresse_client, contact_client, email_client, utilisateur_id)
            
            self.show_message(added)
        except Exception as e:
            print(f"Error: {e}")

    def show_message(self, retour):
        msg_box = QMessageBox(self)

        # :TODO: the window title doesn't show. Correct it!!

        if retour == "Client ajouté":
            msg_box.setWindowTitle("Succès")
            # msg_box.setIcon(QMessageBox.information)
            msg_box.setText(f"Le client {self.line_edit_nom.text()} a été bien ajouté !")
            msg_box.exec()
        elif retour == "Client mis-à-jour":
            msg_box.setWindowTitle("Succès")
            msg_box.setText(f"Les informations du client {self.nom_client_info} ont été bien mises-à-jour !")
            msg_box.exec()
        else:
            msg_box.setWindowTitle("Echec")
            # msg_box.setIcon(QMessageBox.warning)
            msg_box.setText(f"Le client {self.line_edit_nom.text()} n'a pas été ajouté/mis-à-jour.")
            msg_box.exec()
    
    # Signal sent to the front_page.py that says the user has clicked on the ok button and that
    # it is now ok to insert the client in the db and display it on the front page.
    def add_client(self):
        self.insert_new_client()
        self.accept()  # signal sent every time we clicked on the ok btn
    
    def select_client(self):
        self.id_client = self.row_data[0]
        self.nom_client = self.row_data[1]
        return bk.get_client(self.id_client, self.nom_client)

    def update_client(self):
        # :TODO: Gérer le cas de l'ID utilisateur...
        updated_utilisateur_id = 00

        updated_nom_client = self.line_edit_nom.text()
        updated_entreprise_client = self.line_edit_entreprise.text()
        updated_adresse_client = self.line_edit_adresse.text()
        updated_contact_client = int(self.line_edit_contact.text())
        updated_email_client = self.line_edit_email.text()

        updated = bk.update_client(self.id_client_info, updated_nom_client, updated_entreprise_client, updated_adresse_client, updated_contact_client, updated_email_client, updated_utilisateur_id)
        print(f"updated: {updated}")

        self.show_message(updated)
        self.close()  # Close the Dialog

        self.data_updated.emit()

        

