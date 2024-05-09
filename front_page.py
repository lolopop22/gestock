
from mysql import connector
# from back_logicel_gestion_stock import 

from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
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
        self.dropdown_gestion_referentiels.setHidden(True)
        self.dropdown_gestion_produits.setHidden(True)
        self.dropdown_gestion_operations.setHidden(True)
        self.dropdown_gestion_compta.setHidden(True)

        self.tabWidget.setCurrentIndex(0)

        # Connect Buttons to switch to different pages
        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboard_tab)
        self.btn_dashboard_2.clicked.connect(self.switch_to_dashboard_tab)

        self.btn_ref_produits.clicked.connect(self.switch_to_referentiel_produits_tab)
        self.btn_ref_fournisseurs.clicked.connect(self.switch_to_referentiel_fournisseurs_tab)
        self.btn_ref_entrepots.clicked.connect(self.switch_to_referentiel_entrepots_tab)
        self.btn_ref_clients.clicked.connect(self.switch_to_referentiel_clients_tab)
        
        self.btn_inventaire.clicked.connect(self.switch_to_inventaire_tab)
        self.btn_mvts_des_stocks.clicked.connect(self.switch_to_mvt_des_stocks_tab)
        
        self.btn_inventaire.clicked.connect(self.switch_to_inventaire_tab)
        self.btn_mvts_des_stocks.clicked.connect(self.switch_to_mvt_des_stocks_tab)
        
        self.btn_ventes_retours.clicked.connect(self.switch_to_ventes_et_retours_tab)
        self.btn_paiements_factures.clicked.connect(self.switch_to_paiements_et_factures_tab)
        self.btn_livraisons.clicked.connect(self.switch_to_livraisons_tab)

        self.btn_depenses.clicked.connect(self.switch_to_depenses_tab)
        self.btn_flux_monetaires.clicked.connect(self.switch_to_flux_monetaires_tab)
        self.btn_rapports_financiers.clicked.connect(self.switch_to_rapports_financiers_tab)
        
#         self.parametre_1.clicked.connect(self.switch_to_parametres_page)
#         self.parametre_2.clicked.connect(self.switch_to_parametres_page)

        # Connect Buttons to respective context menus
        self.btn_gestion_referentiels_1.clicked.connect(self.gestion_referentiels_context_menu)
        self.btn_gestion_produits_1.clicked.connect(self.gestion_produit_context_menu)
        self.btn_gestion_operations_1.clicked.connect(self.gestion_operations_context_menu)
        self.btn_gestion_compta_1.clicked.connect(self.gestion_comptabilite_context_menu)

        self.btn_ajout_produit.clicked.connect(self.open_client_dialog)

#         # Connect to mysql server and create database if it doesn't exist
#         # self.create_connection()

#         # Create clients table
#         # self.create_clients_table()

#         # Open add client dialog
#         self.ajout_client_btn.clicked.connect(self.open_add_client_student_dialog)

    # Methods to switch to different tabs
    def switch_to_dashboard_tab(self):
        self.tabWidget.setCurrentIndex(0)
    
#     def switch_to_parametres_page(self):
#         self.stackedWidget.setCurrentIndex(9)

        # Référentiel Produits
    def switch_to_referentiel_produits_tab(self):
        self.tabWidget.setCurrentIndex(1)

        # Référentiel Fournisseurs
    def switch_to_referentiel_fournisseurs_tab(self):
        self.tabWidget.setCurrentIndex(2)

        # Référentiel Entrepôts
    def switch_to_referentiel_entrepots_tab(self):
        self.tabWidget.setCurrentIndex(3)

        # Référentiel Clients
    def switch_to_referentiel_clients_tab(self):
        self.tabWidget.setCurrentIndex(4)

        # Gestion Produits - Inventaire
    def switch_to_inventaire_tab(self):
        self.tabWidget.setCurrentIndex(5)

        # Gestion Produits - Mvt des stocks
    def switch_to_mvt_des_stocks_tab(self):
        self.tabWidget.setCurrentIndex(6)

        # Gestion Opérations - Ventes et Retours
    def switch_to_ventes_et_retours_tab(self):
        self.tabWidget.setCurrentIndex(7)

        # Gestion Opérations - Paiements et Factures
    def switch_to_paiements_et_factures_tab(self):
        self.tabWidget.setCurrentIndex(8)

        # Gestion Opérations - Livraisons
    def switch_to_livraisons_tab(self):
        self.tabWidget.setCurrentIndex(9)

        # Gestion Comptabilité - Dépenses
    def switch_to_depenses_tab(self):
        self.tabWidget.setCurrentIndex(10)

        # Gestion Comptabilité - Flux monétaires
    def switch_to_flux_monetaires_tab(self):
        self.tabWidget.setCurrentIndex(11)

        # Gestion Comptabiltié - Rapports financiers
    def switch_to_rapports_financiers_tab(self):
        self.tabWidget.setCurrentIndex(12)

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
        print("hey")
        clients_dialog = Ui_clients_dialog()
        clients_dialog.open()

#     # CREATE DATABASE CONNECTION
#     def create_connection(self):

#         host_name = "localhost"
#         user_name = "root"
#         pass_word = "root"
#         database_name = "gestock_db"

#         # Establish conection to mysql server
#         self.mydb = connector.connect(
#             host = host_name,
#             user = user_name,
#             password = pass_word
#         )

#         # Create a cursor to execute SQL queries
#         cursor = self.mydb.cursor()

#         # Create database if it doesn't exist
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

#         # Connect to the created database
#         self.mydb = connector.connect(
#             host = host_name,
#             user = user_name,
#             password = pass_word,
#             database = database_name
#         )

#         return self.mydb

#     # CREATE CLIENTS TABLE
#     def create_clients_table(self):
        
#         # Create a cursor for executing SQL queries
#         cursor = self.create_connection().cursor()

#         # The query
#         create_clients_table_query = f"""
# CREATE TABLE IF NOT EXISTS clients_table(
#     prenom TEXT,
#     nom TEXT,
#     client_id VARCHAR(15) PRIMARY KEY,
#     entreprise TEXT,
#     adresse TEXT,
#     telephone VARCHAR(15),
#     genre TEXT
# )"""
        
#         cursor.execute(create_clients_table_query)

#         # Commit changes and close the connection
#         self.mydb.commit()
#         self.mydb.close()
    
#     # Open Dialog for inserting new client
#     def open_add_client_student_dialog(self):

#         from ui_add_client import Ui_clients_dialog

#         add_client = Ui_clients_dialog(self)
#         result = add_client.exec()

#         if result == Ui_clients_dialog.accepted:
#             pass

    
