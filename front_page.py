
from mysql import connector

from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow


class FrontPage(QMainWindow, Ui_MainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("GeStock")

        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)

        # Hide Dropdowns
        self.clients_dropdown.setHidden(True)
        self.entrepots_dropdown.setHidden(True)
        self.fournisseurs_dropdown.setHidden(True)
        self.comptabilite_dropdown.setHidden(True)

        self.stackedWidget.setCurrentIndex(0)

        # Connect Buttons to switch to different pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)
        
        self.parametre_1.clicked.connect(self.switch_to_parametres_page)
        self.parametre_2.clicked.connect(self.switch_to_parametres_page)

        self.entrepots_2.clicked.connect(self.switch_to_entrepots_marchandise_page)
        self.clients_2.clicked.connect(self.switch_to_clients_info_page)
        self.fournisseurs_2.clicked.connect(self.switch_to_fournisseurs_info_page)
        self.comptabilite_2.clicked.connect(self.switch_to_comptabilite_budget_page)
        
        self.entrepots_marchandise.clicked.connect(self.switch_to_entrepots_marchandise_page)
        self.entrepots_commande.clicked.connect(self.switch_to_entrepots_commande_page)
        
        self.client_info.clicked.connect(self.switch_to_clients_info_page)
        self.client_transaction.clicked.connect(self.switch_to_clients_transaction_page)
        
        self.fournisseurs_info.clicked.connect(self.switch_to_fournisseurs_info_page)
        self.fournisseurs_transaction.clicked.connect(self.switch_to_fournisseurs_transaction_page)
        
        self.comptabilite_budget.clicked.connect(self.switch_to_comptabilite_budget_page)
        self.comptabilite_depense.clicked.connect(self.switch_to_comptabilite_depense_page)

        # Connect Buttons to respective context menus
        self.entrepots_1.clicked.connect(self.entrepots_context_menu)
        self.clients_1.clicked.connect(self.clients_context_menu)
        self.fournisseurs_1.clicked.connect(self.fournisseurs_context_menu)
        self.comptabilite_1.clicked.connect(self.comptabilite_context_menu)

        # Connect to mysql server and create database if it doesn't exist
        # self.create_connection()

        # Create clients table
        # self.create_clients_table()

        # Open add client dialog
        self.ajout_client_btn.clicked.connect(self.open_add_client_student_dialog)

    # Methods to switch to different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_parametres_page(self):
        self.stackedWidget.setCurrentIndex(9)

        # Entrepôts
    def switch_to_entrepots_marchandise_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_entrepots_commande_page(self):
        self.stackedWidget.setCurrentIndex(2)

        # Clients
    def switch_to_clients_info_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_clients_transaction_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_fournisseurs_info_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_fournisseurs_transaction_page(self):
        self.stackedWidget.setCurrentIndex(6)

        # Comptabilité
    def switch_to_comptabilite_budget_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_comptabilite_depense_page(self):
        self.stackedWidget.setCurrentIndex(8)

    # Methods to show context menus
    def entrepots_context_menu(self):
        self.show_custom_context_menu(self.entrepots_1, ["Marchandises", "Commandes"])
    
    # Methods to show context menus
    def clients_context_menu(self):
        self.show_custom_context_menu(self.clients_1, ["Informations clients", "Transactions clients"])

    # Methods to show context menus
    def fournisseurs_context_menu(self):
        self.show_custom_context_menu(self.fournisseurs_1, ["Informations fournisseurs", "Transactions fournisseurs"])
    
    # Methods to show context menus
    def comptabilite_context_menu(self):
        self.show_custom_context_menu(self.comptabilite_1, ["Budget", "Dépenses"])



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
        if text == "Marchandises":
            self.switch_to_entrepots_marchandise_page()
        elif text == "Commandes":
            self.switch_to_entrepots_commande_page()
        elif text == "Informations clients":
            self.switch_to_clients_info_page()
        elif text == "Transactions clients":
            self.switch_to_clients_transaction_page()
        elif text == "Informations fournisseurs":
            self.switch_to_fournisseurs_transaction_page()
        elif text == "Transactions fournisseurs":
            self.switch_to_entrepots_commande_page()
        elif text == "switch_to_comptabilite_page":
            self.switch_to_entrepots_commande_page()
        elif text == "Dépenses":
            self.switch_to_comptabilite_depense_page()

    # CREATE DATABASE CONNECTION
    def create_connection(self):

        host_name = "localhost"
        user_name = "root"
        pass_word = "root"
        database_name = "gestock_db"

        # Establish conection to mysql server
        self.mydb = connector.connect(
            host = host_name,
            user = user_name,
            password = pass_word
        )

        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Connect to the created database
        self.mydb = connector.connect(
            host = host_name,
            user = user_name,
            password = pass_word,
            database = database_name
        )

        return self.mydb

    # CREATE CLIENTS TABLE
    def create_clients_table(self):
        
        # Create a cursor for executing SQL queries
        cursor = self.create_connection().cursor()

        # The query
        create_clients_table_query = f"""
CREATE TABLE IF NOT EXISTS clients_table(
    prenom TEXT,
    nom TEXT,
    client_id VARCHAR(15) PRIMARY KEY,
    entreprise TEXT,
    adresse TEXT,
    telephone VARCHAR(15),
    genre TEXT
)"""
        
        cursor.execute(create_clients_table_query)

        # Commit changes and close the connection
        self.mydb.commit()
        self.mydb.close()
    
    # Open Dialog for inserting new client
    def open_add_client_student_dialog(self):

        from ui_add_client import Ui_clients_dialog

        add_client = Ui_clients_dialog(self)
        result = add_client.exec()

        if result == Ui_clients_dialog.accepted:
            pass

    
