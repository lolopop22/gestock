import sys

from mysql import connector
# from back_logicel_gestion_stock import 
import back_logicel_gestion_stock as bk
from PySide6.QtWidgets import QMainWindow, QMenu, QApplication, QDialog, QTableWidgetItem
from PySide6.QtGui import QAction

import ui_client_dialog
from ui_index import Ui_MainWindow
from ui_produit_dialog import Ui_dialog_produit
from ui_client_dialog import Ui_clients_dialog


class FrontPage(QMainWindow, Ui_MainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GeStock")

        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)

        # Hide Dropdowns
        self.dropdown_gestion_referentiels_3.setHidden(True)
        self.dropdown_gestion_produits_3.setHidden(True)
        self.dropdown_gestion_operations_3.setHidden(True)
        self.dropdown_gestion_compta_3.setHidden(True)

        self.tabWidget.setCurrentIndex(0)

        # Connect Buttons to switch to different pages
        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboard_tab)
        self.btn_dashboard_4.clicked.connect(self.switch_to_dashboard_tab)

        self.btn_ref_produits_3.clicked.connect(self.switch_to_referentiel_produits_tab)
        self.btn_ref_fournisseurs_3.clicked.connect(self.switch_to_referentiel_fournisseurs_tab)
        self.btn_ref_entrepots_3.clicked.connect(self.switch_to_referentiel_entrepots_tab)
        self.btn_ref_clients_3.clicked.connect(self.switch_to_referentiel_clients_tab)
        
        self.btn_inventaire_3.clicked.connect(self.switch_to_inventaire_tab)
        self.btn_mvts_des_stocks_3.clicked.connect(self.switch_to_mvt_des_stocks_tab)
        
        self.btn_inventaire_3.clicked.connect(self.switch_to_inventaire_tab)
        self.btn_mvts_des_stocks_3.clicked.connect(self.switch_to_mvt_des_stocks_tab)
        
        self.btn_ventes_retours_3.clicked.connect(self.switch_to_ventes_et_retours_tab)
        #self.btn_paiements_factures.clicked.connect(self.switch_to_paiements_et_factures_tab)
        self.btn_livraisons_3.clicked.connect(self.switch_to_livraisons_tab)

        #self.btn_rapports_financiers_3.clicked.connect(self.switch_to_depenses_tab)
        self.btn_flux_monetaires_3.clicked.connect(self.switch_to_flux_monetaires_tab)
        self.btn_rapports_financiers_3.clicked.connect(self.switch_to_rapports_financiers_tab)
        
#         self.parametre_1.clicked.connect(self.switch_to_parametres_page)
#         self.parametre_2.clicked.connect(self.switch_to_parametres_page)

        # Connect Buttons to respective context menus
        self.btn_gestion_referentiels_1.clicked.connect(self.gestion_referentiels_context_menu)
        self.btn_gestion_produits_1.clicked.connect(self.gestion_produit_context_menu)
        self.btn_gestion_operations_1.clicked.connect(self.gestion_operations_context_menu)
        self.btn_gestion_compta_1.clicked.connect(self.gestion_comptabilite_context_menu)

        # Connect Buttons to respective context menus
        self.btn_gestion_referentiels_4.clicked.connect(self.open_dropdown_referential)
        self.btn_gestion_produits_4.clicked.connect(self.open_dropdown_stock)
        self.btn_gestion_operations_4.clicked.connect(self.open_dropdown_operations)
        self.btn_gestion_compta_4.clicked.connect(self.open_dropdown_compta)

        self.btn_ajout_produit.clicked.connect(self.open_produit_dialog)
        self.btn_ajout_client.clicked.connect(self.open_client_dialog)
        self.refresh_table_client()
        self.tabWidget.tabCloseRequested.connect(self.closeTab)



    def open_dropdown_referential(self):
        if self.dropdown_gestion_referentiels_3.isHidden():
            self.dropdown_gestion_referentiels_3.setHidden(False)
        else:
            self.dropdown_gestion_referentiels_3.setHidden(True)


    def open_dropdown_stock(self):


        if self.dropdown_gestion_produits_3.isHidden():
            self.dropdown_gestion_produits_3.setHidden(False)
        else:
            self.dropdown_gestion_produits_3.setHidden(True)

    def open_dropdown_operations(self):

        self.dropdown_gestion_compta_3.setHidden(True)
        if self.dropdown_gestion_operations_3.isHidden():
            self.dropdown_gestion_operations_3.setHidden(False)
        else:
            self.dropdown_gestion_operations_3.setHidden(True)

    def open_dropdown_compta(self):

        if self.dropdown_gestion_compta_3.isHidden():
            self.dropdown_gestion_compta_3.setHidden(False)
        else:
            self.dropdown_gestion_compta_3.setHidden(True)

    def switch_to_dashboard_tab(self):

        self.tabWidget.insertTab(-1, self.tab_dashboard, 'Dashboard')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)
    
#     def switch_to_parametres_page(self):
#         self.stackedWidget.setCurrentIndex(9)

        # Référentiel Produits
    def switch_to_referentiel_produits_tab(self):

        self.tabWidget.insertTab(-1, self.tab_produits, 'Produits')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb-1)

        # Référentiel Fournisseurs
    def switch_to_referentiel_fournisseurs_tab(self):
        #self.tabWidget.setCurrentIndex(2)
        self.tabWidget.insertTab(-1, self.tab_fournisseurs, 'Fournisseurs')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Référentiel Entrepôts
    def switch_to_referentiel_entrepots_tab(self):
        # self.tabWidget.setCurrentIndex(3)
        self.tabWidget.insertTab(-1, self.tab_entrepots, 'Entrepôts')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Référentiel Clients
    def switch_to_referentiel_clients_tab(self):
        # self.tabWidget.setCurrentIndex(4)
        self.tabWidget.insertTab(-1, self.tab_client, 'Clients')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Produits - Inventaire
    def switch_to_inventaire_tab(self):
        # self.tabWidget.setCurrentIndex(5)
        self.tabWidget.insertTab(-1, self.tab_inventaires, 'Inventaire')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Produits - Mvt des stocks
    def switch_to_mvt_des_stocks_tab(self):
        # self.tabWidget.setCurrentIndex(6)
        self.tabWidget.insertTab(-1, self.tab_mvt_stock, 'Mouvements de stock')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Opérations - Ventes et Retours
    def switch_to_ventes_et_retours_tab(self):
        # self.tabWidget.setCurrentIndex(7)
        self.tabWidget.insertTab(-1, self.tab_vente_retour, 'Ventes et retours')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Opérations - Paiements et Factures
    def switch_to_paiements_et_factures_tab(self):
        # self.tabWidget.setCurrentIndex(8)
        self.tabWidget.insertTab(-1, self.tab_produits, 'Produits')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Opérations - Livraisons
    def switch_to_livraisons_tab(self):
        # self.tabWidget.setCurrentIndex(9)
        self.tabWidget.insertTab(-1, self.tab_livraison, 'Livraisons')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Comptabilité - Dépenses
    def switch_to_depenses_tab(self):
        self.tabWidget.setCurrentIndex(10)

        # Gestion Comptabilité - Flux monétaires
    def switch_to_flux_monetaires_tab(self):
        # self.tabWidget.setCurrentIndex(11)
        self.tabWidget.insertTab(-1, self.tab_flux_monetaire, 'Flux monétaires')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

        # Gestion Comptabiltié - Rapports financiers
    def switch_to_rapports_financiers_tab(self):
        # self.tabWidget.setCurrentIndex(12)
        self.tabWidget.insertTab(-1, self.tab_rapports_financiers, 'Rapports financiers')
        nb = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(nb - 1)

#     # Methods to show context menus
    def gestion_referentiels_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_referentiels_1, ["Produits", "Fournisseurs", "Entrepôts", "Clients"])
    
    # Methods to show context menus
    def gestion_produit_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_produits_1, ["Inventaire", "Mouvements des stocks"])

    # Methods to show context menus
    def gestion_operations_context_menu(self):
        self.show_custom_context_menu(self.btn_gestion_operations_1, ["Ventes et Retours", "Paiements et Factures", "Livraisons"])
    
#     # Methods to show context menus
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
        elif text == "Paiements et Factures":
            self.switch_to_paiements_et_factures_tab()
        elif text == "Livraisons":
            self.switch_to_livraisons_tab()
        elif text == "Dépenses":
            self.switch_to_depenses_tab()
        elif text == "Flux monétaires":
            self.switch_to_flux_monetaires_tab()
        elif text == "Rapports financiers":
            self.switch_to_rapports_financiers_tab()

    def open_client_dialog(self):


        clients_dialog = QDialog()
        ui = Ui_clients_dialog()
        ui.setupUi(clients_dialog)
        clients_dialog.exec_()

        return ui
        print("hey")

    def open_produit_dialog(self):


        produits_dialog = QDialog()
        ui = Ui_dialog_produit()
        ui.setupUi(produits_dialog)
        produits_dialog.exec_()
        print("hey")

    def refresh_table_client(self):
        # Récupération des données depuis la base de données
        data = bk.get_all_clients()

        # Effacer toutes les lignes actuelles du tableau
        self.table_infos_client_2.setRowCount(0)

        # Insérer les nouvelles données dans le tableau
        for row, client in enumerate(data):
            self.table_infos_client_2.insertRow(row)
            for col, value in enumerate(client.values()):
                item = QTableWidgetItem(str(value))
                self.table_infos_client_2.setItem(row, col, item)

    def closeTab(self, index):
            # Fonction pour fermer les onglets
            self.tabWidget.removeTab(index)