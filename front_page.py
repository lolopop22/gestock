import sys
import back_logicel_gestion_stock as bk

from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PySide6.QtGui import QAction, QIcon

from ui_index import Ui_MainWindow


class FrontPage(QMainWindow, Ui_MainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GeStock")

        # GUI initialisation
        self.set_initial_gui_state()

        # Connect Buttons to switch to different pages
        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboard_tab)
        self.btn_dashboard_2.clicked.connect(self.switch_to_dashboard_tab)

        self.btn_ref_clients.clicked.connect(self.switch_to_referentiel_clients_tab)
        self.btn_ref_entrepots.clicked.connect(self.switch_to_referentiel_entrepots_tab)
        self.btn_ref_fournisseurs.clicked.connect(self.switch_to_referentiel_fournisseurs_tab)
        self.btn_ref_matieres_premieres.clicked.connect(self.switch_to_referentiel_matieres_premieres_tab)
        self.btn_ref_produits.clicked.connect(self.switch_to_referentiel_produits_tab)
        
        self.btn_inventaire.clicked.connect(self.switch_to_inventaire_tab)
        self.btn_mvts_des_stocks.clicked.connect(self.switch_to_mvt_des_stocks_tab)
        
        # self.btn_paiements_factures.clicked.connect(self.switch_to_paiements_et_factures_tab)
        self.btn_livraisons.clicked.connect(self.switch_to_livraisons_tab)
        self.btn_ventes_retours.clicked.connect(self.switch_to_ventes_et_retours_tab)

        # self.btn_depenses.clicked.connect(self.switch_to_depenses_tab)
        self.btn_flux_monetaires.clicked.connect(self.switch_to_flux_monetaires_tab)
        self.btn_rapports_financiers.clicked.connect(self.switch_to_rapports_financiers_tab)
        
        # self.parametre_1.clicked.connect(self.switch_to_parametres_page)
        # self.parametre_2.clicked.connect(self.switch_to_parametres_page)

        # Connect Buttons to respective context menus
        self.btn_gestion_referentiels_1.clicked.connect(self.gestion_referentiels_context_menu)
        self.btn_gestion_stock_1.clicked.connect(self.gestion_stock_context_menu)
        self.btn_gestion_operations_1.clicked.connect(self.gestion_operations_context_menu)
        self.btn_gestion_compta_1.clicked.connect(self.gestion_comptabilite_context_menu)

        # Open add client, fournisseur
        self.btn_ajout_client.clicked.connect(self.open_client_dialog)
        self.btn_ajout_fournisseur.clicked.connect(self.open_fournisseur_dialog)

        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # Load clients information to QTable
        self.load_clients_info()
        self.cherche_client.textChanged.connect(self.search_clients)

        # Load fournisseurs information to QTable
        self.load_fournisseurs_info()


        # Connect Buttons to respective context menus
        self.btn_gestion_referentiels_2.clicked.connect(self.open_dropdown_referentiel)
        self.btn_gestion_stock_2.clicked.connect(self.open_dropdown_stock)
        self.btn_gestion_operations_2.clicked.connect(self.open_dropdown_operations)
        self.btn_gestion_compta_2.clicked.connect(self.open_dropdown_compta)

    def set_initial_gui_state(self):
        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)

        # Hide Dropdowns
        self.dropdown_gestion_compta.setHidden(True)
        self.dropdown_gestion_operations.setHidden(True)
        self.dropdown_gestion_referentiels.setHidden(True)
        self.dropdown_gestion_stocks.setHidden(True)

        # Tab visibility settings
        self.tab_widget.setCurrentIndex(0)
        nb_tabs = self.tab_widget.count()
        for index in range(1, nb_tabs):
            self.tab_widget.setTabVisible(index, False)
        
        self.table_infos_clients.setColumnWidth(0, 80)
        self.table_infos_clients.setColumnWidth(3, 180)
        
        self.table_infos_fournisseurs.setColumnWidth(0, 80)

    def open_dropdown_referentiel(self):
        self.btn_dashboard_2.setChecked(False)
        if self.dropdown_gestion_referentiels.isHidden():
            self.dropdown_gestion_referentiels.setHidden(False)
        else:
            self.dropdown_gestion_referentiels.setHidden(True)


    def open_dropdown_stock(self):
        self.btn_dashboard_2.setChecked(False)
        if self.dropdown_gestion_stocks.isHidden():
            self.dropdown_gestion_stocks.setHidden(False)
        else:
            self.dropdown_gestion_stocks.setHidden(True)

    def open_dropdown_operations(self):
        self.btn_dashboard_2.setChecked(False)
        if self.dropdown_gestion_operations.isHidden():
            self.dropdown_gestion_operations.setHidden(False)
        else:
            self.dropdown_gestion_operations.setHidden(True)

    def open_dropdown_compta(self):
        self.btn_dashboard_2.setChecked(False)
        if self.dropdown_gestion_compta.isHidden():
            self.dropdown_gestion_compta.setHidden(False)
        else:
            self.dropdown_gestion_compta.setHidden(True)

    def switch_to_dashboard_tab(self):

        self.tab_widget.insertTab(-1, self.tab_dashboard, 'Tableau de bord')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Référentiel Clients
    def switch_to_referentiel_clients_tab(self):
        self.tab_widget.insertTab(-1, self.tab_clients, 'Clients')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Référentiel Entrepôts
    def switch_to_referentiel_entrepots_tab(self):
        self.tab_widget.insertTab(-1, self.tab_entrepots, 'Entrepôts')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Référentiel Fournisseurs
    def switch_to_referentiel_fournisseurs_tab(self):
        self.tab_widget.insertTab(-1, self.tab_fournisseurs, 'Fournisseurs')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    def switch_to_referentiel_matieres_premieres_tab(self):
        self.tab_widget.insertTab(-1, self.tab_matieres_premieres, 'Matières premières')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb-1)
    
    # Référentiel Produits
    def switch_to_referentiel_produits_tab(self):
        self.tab_widget.insertTab(-1, self.tab_produits, 'Produits')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb-1)

    # Gestion Produits - Inventaire
    def switch_to_inventaire_tab(self):
        # self.tab_widget.setCurrentIndex(5)
        self.tab_widget.insertTab(-1, self.tab_inventaires, 'Inventaire')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Produits - Mvt des stocks
    def switch_to_mvt_des_stocks_tab(self):
        # self.tab_widget.setCurrentIndex(6)
        self.tab_widget.insertTab(-1, self.tab_mvts_stocks, 'Mouvements de stock')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Opérations - Ventes et Retours
    def switch_to_ventes_et_retours_tab(self):
        # self.tab_widget.setCurrentIndex(7)
        self.tab_widget.insertTab(-1, self.tab_vente_retour, 'Ventes et retours')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Opérations - Paiements et Factures
    # def switch_to_paiements_et_factures_tab(self):
    #     # self.tab_widget.setCurrentIndex(8)
    #     self.tab_widget.insertTab(-1, self.tab_produits, 'Produits')
    #     nb = self.tab_widget.count()
    #     self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Opérations - Livraisons
    def switch_to_livraisons_tab(self):
        self.tab_widget.insertTab(-1, self.tab_livraisons, 'Livraisons')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Comptabilité - Dépenses
    # def switch_to_depenses_tab(self):
    #     self.tab_widget.setCurrentIndex(10)

    # Gestion Comptabilité - Flux monétaires
    def switch_to_flux_monetaires_tab(self):
        self.tab_widget.insertTab(-1, self.tab_flux_monetaires, 'Flux monétaires')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Gestion Comptabiltié - Rapports financiers
    def switch_to_rapports_financiers_tab(self):
        self.tab_widget.insertTab(-1, self.tab_rapports_financiers, 'Rapports financiers')
        nb = self.tab_widget.count()
        self.tab_widget.setCurrentIndex(nb - 1)

    # Methods to show context menus
    def gestion_referentiels_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_referentiels_1, ["Matières premières", "Produits", "Fournisseurs", "Entrepôts", "Clients"])
    
    def gestion_stock_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_stock_1, ["Inventaire", "Mouvements des stocks"])

    def gestion_operations_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_operations_1, ["Ventes et Retours", "Paiements et Factures", "Livraisons"])
    
    def gestion_comptabilite_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_compta_1, ["Dépenses", "Flux monétaires", "Rapports financiers"])


    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)
        
        # Set style for the menu
        menu.setStyleSheet("""
QMenu{
                           background-color: black;
                           color: white;
}
QMenu:selected{ 
                           background-color: white;
                           color: #2672CC;
}""") 
        
        # Add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
        
        # Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()
        if text == "Produits":
            self.switch_to_referentiel_produits_tab()
        elif text == "Matières premières":
            self.switch_to_referentiel_matieres_premieres_tab()
        elif text == "Fournisseurs":
            self.switch_to_referentiel_fournisseurs_tab()
        elif text == "Entrepôts":
            self.switch_to_referentiel_entrepots_tab()
        elif text == "Clients":
            self.switch_to_referentiel_clients_tab()
        elif text == "Inventaire":
            self.switch_to_inventaire_tab()
        elif text == "Mouvements des stocks":
            self.switch_to_mvt_des_stocks_tab()
        elif text == "Ventes et Retours":
            self.switch_to_ventes_et_retours_tab()
        # elif text == "Paiements et Factures":
        #     self.switch_to_paiements_et_factures_tab()
        elif text == "Livraisons":
            self.switch_to_livraisons_tab()
        # elif text == "Dépenses":
        #     self.switch_to_depenses_tab()
        elif text == "Flux monétaires":
            self.switch_to_flux_monetaires_tab()
        elif text == "Rapports financiers":
            self.switch_to_rapports_financiers_tab()

    # Close tabs
    def close_tab(self, index):
        self.tab_widget.removeTab(index)

    # OPEN DIALOG FOR INSETING NEW CLIENT
    def open_client_dialog(self):

        from ui_client_dialog import Ui_client_dialog
        
        client_dialog = Ui_client_dialog(self)
        result = client_dialog.exec()  # This will block the front page gui until the dialog is closed
        print(f"dialog result: {result}")
        print(f"Ui_client_dialog.Accepted: {Ui_client_dialog.Accepted}")

        if result == Ui_client_dialog.Accepted:
            # if the dialog was accepted (user clicked add client btn)
            print("accepted")
            self.reload_clients_table_data()

    # OPEN DIALOG FOR INSETING NEW FOURNISSEUR
    def open_fournisseur_dialog(self):

        from ui_fournisseur_dialog import Ui_fournisseur_dialog
        
        fournisseur_dialog = Ui_fournisseur_dialog(self)
        result = fournisseur_dialog.exec()  # This will block the front page gui until the dialog is closed

        if result == Ui_fournisseur_dialog.Accepted:
            # if the dialog was accepted (user clicked add client btn)
            self.reload_fournisseurs_table_data()
    
    def reload_clients_table_data(self):
        # This method is called to reload the clients table data
        self.load_clients_info()
    
    def reload_fournisseurs_table_data(self):
        # This method is called to reload the fournisseurs table data
        self.load_fournisseurs_info()
    
    # LOAD CLIENTS INFORMATION to QTABLE
    def load_clients_info(self):
        # Effacer toutes les lignes actuelles du tableau
        self.table_infos_clients.setRowCount(0)

        # Récupération des données depuis la base de données
        data = bk.get_all_clients()

        # Insérer les nouvelles données dans le tableau
        for row_index, row_data in enumerate(data):
            self.table_infos_clients.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):  # client.values()
                item = QTableWidgetItem(str(cell_data))
                self.table_infos_clients.setItem(row_index, col_index, item)

                # Create a custom widget with 2 btns lined up horizontally for the actions column
                double_button_widget = DoubleButtonWidgetClients(row_index, row_data)

                # Set the custom widget with 2 btns as teh cell widget for the actions column
                self.table_infos_clients.setCellWidget(row_index, 6, double_button_widget)
                self.table_infos_clients.setRowHeight(row_index, 50)
    
    def load_fournisseurs_info(self):
        # Effacer toutes les lignes actuelles du tableau
        self.table_infos_fournisseurs.setRowCount(0)

        # Récupération des données depuis la base de données
        data = bk.get_all_fournisseurs()

        # Insérer les nouvelles données dans le tableau
        for row_index, row_data in enumerate(data):
            self.table_infos_fournisseurs.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_infos_fournisseurs.setItem(row_index, col_index, item)

                # Create a custom widget with 2 btns lined up horizontally for the actions column
                double_button_widget = DoubleButtonWidgetClients(row_index, row_data)

                # Set the custom widget with 2 btns as teh cell widget for the actions column
                self.table_infos_fournisseurs.setCellWidget(row_index, 5, double_button_widget)
                self.table_infos_fournisseurs.setRowHeight(row_index, 50)
    
    def search_clients(self):
        # Clear previous table results
        self.table_infos_clients.setRowCount(0)

        # Get the searched clients from que the search Qlineedit
        searched_nom_client = self.cherche_client.text()
        data = bk.search_client(searched_nom_client)

        # Insérer les nouvelles données dans le tableau
        for row_index, row_data in enumerate(data):
            self.table_infos_clients.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_infos_clients.setItem(row_index, col_index, item)

                # Create a custom widget with 2 btns lined up horizontally for the actions column
                double_button_widget = DoubleButtonWidgetClients(row_index, row_data)

                # Set the custom widget with 2 btns as teh cell widget for the actions column
                self.table_infos_clients.setCellWidget(row_index, 6, double_button_widget)
                self.table_infos_clients.setRowHeight(row_index, 50)
    
    def search_fournisseurs(self):
        # Clear previous table results
        self.table_infos_fournisseurs.setRowCount(0)

        # Get the searched providers from que the search Qlineedit
        searched_nom_fournisseur = self.cherche_fournisseur.text()
        data = bk.search_fournisseur(searched_nom_fournisseur)

        # Insérer les nouvelles données dans le tableau
        for row_index, row_data in enumerate(data):
            self.table_infos_fournisseurs.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_infos_fournisseurs.setItem(row_index, col_index, item)

                # Create a custom widget with 2 btns lined up horizontally for the actions column
                double_button_widget = DoubleButtonWidgetClients(row_index, row_data)

                # Set the custom widget with 2 btns as teh cell widget for the actions column
                self.table_infos_fournisseurs.setCellWidget(row_index, 5, double_button_widget)
                self.table_infos_fournisseurs.setRowHeight(row_index, 50)

        





class DoubleButtonWidgetClients(QWidget):
    def __init__(self, row_index, row_data):
        super().__init__()

        self.row_index = row_index
        self.row_data = row_data

        # Get client variables from the tuple row_data
        # print(row_data)
        self.id = self.row_data[0]
        self.nom = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create blue Edit btn
        self.btn_mise_a_jour = QPushButton("", self)
        self.btn_mise_a_jour.setStyleSheet("background-color: blue;")
        self.btn_mise_a_jour.setFixedSize(60, 30)

        # Create red Delete btn
        self.btn_suppr = QPushButton("", self)
        self.btn_suppr.setStyleSheet("background-color: red;")
        self.btn_suppr.setFixedSize(60, 30)

        # Set icons for the buttons
        icon_edit = QIcon(":/icones/edit.png")
        self.btn_mise_a_jour.setIcon(icon_edit)

        icon_del = QIcon(":/icones/delete.png")
        self.btn_suppr.setIcon(icon_del)

        layout.addWidget(self.btn_mise_a_jour)
        layout.addWidget(self.btn_suppr)

