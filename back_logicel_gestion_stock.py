import sqlite3 as server
import sys
import os

path_db = r'DB_gestion_stock.db'


def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:

        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def connexion():
    conn = server.connect(resource_path(path_db))
    cur = conn.cursor()

    return conn, cur


def deconnexion(conn):
    conn.commit()
    conn.close()


def requetage(req):
    conn, cur = connexion()
    cur.execute(req)
    resultat = cur.fetchone()
    print(resultat)
    deconnexion(conn)

    return resultat


# Produits

def add_produit(code_article, label, fournisseur_id, prix_revient, prix_vente, description, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_article" (code_article, label_article, fournisseur_id, prix_revient, prix_vente, description, utilisateur_id) values (?,?,?,?,?,?,?)'
        cur.execute(req, (code_article, label, fournisseur_id, prix_revient, prix_vente, description, utilisateur_id))
        deconnexion(conn)
        return 'Produit Ajouté'
    except:
        deconnexion(conn)
        return 'Produit déjà existant'


def update_article(label, fournisseur_id, prix_revient, prix_vente, description, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_article" set label_article=?, fournisseur_id=?, prix_revient=?, prix_vente=?, description=?, utilisateur_id=? where article_id = {id_article}'

    cur.execute(req, (label, fournisseur_id, prix_revient, prix_vente, description, utilisateur_id))

    deconnexion(conn)


def delete_article(id_article):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_article" where article_id = {id_article}'

    cur.execute(req, ())

    deconnexion(conn)


# Approvisionnement

def add_approvisionnement(fournisseur_id, date_approvisionnement, matiere_premiere_id,
                          quantite, utilisateur_id):
    # try:
    dernier_stock = requetage(
        fr'select max(stock_id), quantite from t_audit_stock_matieres_premieres where matiere_premiere_id = {matiere_premiere_id}')
    dernier_qte = dernier_stock[1]
    if type(dernier_qte) is not int:
        dernier_qte = 0

    add_audit_stock_matiere_premiere(matiere_premiere_id, quantite, date_approvisionnement,
                                     utilisateur_id)

    conn, cur = connexion()
    req = fr'INSERT INTO "t_approvisionnement" (fournisseur_id, date_approvisionnement, matiere_premiere_id, quantite, utilisateur_id) values (?,?,?,?,?)'
    cur.execute(req, (
        fournisseur_id, date_approvisionnement, matiere_premiere_id, quantite + dernier_qte, utilisateur_id))
    deconnexion(conn)
    return 'Stock modifié'


def update_approvisionnement(fournisseur_id, date_approvisionnement, matiere_premiere_id, quantite, utilisateur_id):
    dernier_stock = requetage(
        fr'select max(stock_id), quantite from t_audit_stock_articles where matiere_premiere_id = {matiere_premiere_id}')
    dernier_qte = dernier_stock[1]

    conn, cur = connexion()
    req = fr'UPDATE "t_approvisionnement" set quantite=?, utilisateur_id=? where matiere_premiere_id = {matiere_premiere_id} and date_approvisionnement={date_approvisionnement} and fournisseur_id={fournisseur_id}'
    print(req)
    cur.execute(req, (quantite, utilisateur_id))

    deconnexion(conn)


def delete_approvisionnement(id_approvisionnement, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_approvisionnement" where approvisionnement_id = {id_approvisionnement}'

    cur.execute(req, ())
    deconnexion(conn)


# Audit stock

def add_audit_stock(article_id, quantite, date_mouvement, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_audit_stock_articles" (article_id, quantite,date_mouvement,utilisateur_id) values (?,?,?,?,?)'
        cur.execute(req, (article_id, quantite, date_mouvement, utilisateur_id))
        deconnexion(conn)
        return 'Audit du stock mis à jour'
    except:
        deconnexion(conn)
        return 'Error'


def add_audit_stock_matiere_premiere(matiere_premier_id, quantite, date_mouvement, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_audit_stock_matieres_premieres" (matiere_premiere_id, quantite,date_de_mouvement,utilisateur_id) values (?,?,?,?)'
        cur.execute(req, (matiere_premier_id, quantite, date_mouvement, utilisateur_id))
        deconnexion(conn)
        return 'Audit du stock mis à jour'
    except:
        deconnexion(conn)
        return 'Error'


# Compositions


def add_composition_matieres_premieres(id_article, matiere_premiere_id, quantite, utilisateur_id):
    conn, cur = connexion()
    try:
        req = fr'INSERT INTO "t_composition_matieres_premieres" (article_id, matieres_premieres_id, quantite, utilisateur_id) values (?,?,?,?)'
        cur.execute(req, (id_article, matiere_premiere_id, quantite, utilisateur_id))
        deconnexion(conn)
        return 'Composition ajoutée'
    except:
        deconnexion(conn)
        return 'Composition existante'


def update_composition_matieres_premieres(id_article, matiere_premiere_id, quantite, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_composition_matieres_premieres" set quantite=?, utilisateur_id=? where matieres_premieres_id = {matiere_premiere_id} and article_id= {id_article}'

    cur.execute(req, (quantite, utilisateur_id))

    deconnexion(conn)


def delete_composition_matieres_premieres(id_article, matiere_premiere_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_composition_matieres_premieres" where matieres_premieres_id = {matiere_premiere_id} and article_id= {id_article}'

    cur.execute(req, ())

    deconnexion(conn)


# Clients

def get_all_clients():


    try:
        conn, cur = connexion()
        req = fr'SELECT id_client, nom, entreprise, adresse, contact, email FROM "t_clients"'
        cur.execute(req, ())
        results = cur.fetchall()
        # dictionnaire = [(result[0], result[1], result[2], result[3], result[4], result[5]) for result in results]
        # dictionnaire = [{"id": result[0], "nom": result[1], "entreprise": result[2], "adresse": result[3], "contact": result[4], "email": result[5]} for result in results]
        deconnexion(conn)
        # return dictionnaire
        return results
    except:
        return 'Erreur'
    
def get_client(id_client, nom_client):
    try:
        conn, cur = connexion()
        req = fr'SELECT * FROM "t_clients" WHERE id_client = {id_client} AND nom = "{nom_client}"'
        cur.execute(req, ())
        results = cur.fetchall()
        deconnexion(conn)
        return results
    except:
        return 'Erreur'



def add_client(nom_client, entreprise_client, adresse_client, contact_client, email_client, utilisateur_id):
    
    # :TODO: Vérifier si le client existe déjà avant insertion....
    
    try:
        conn, cur = connexion()
        req = fr'INSERT INTO "t_clients" (nom, entreprise, adresse, contact, email, utilisateur_id) values (?,?,?,?,?,?)'
        cur.execute(req, (nom_client, entreprise_client, adresse_client, contact_client, email_client, utilisateur_id))
        deconnexion(conn)
        return 'Client ajouté'
    except:
        return 'Erreur'


def update_client(id_client, nom, entreprise, adresse, contact, email, utilisateur_id):
    # try:
    conn, cur = connexion()
    req = fr'UPDATE "t_clients" set id_client = ?, nom=?, entreprise=?, adresse=?, contact=?, email=?, utilisateur_id=? where id_client = {id_client}'
    cur.execute(req, (id_client, nom, entreprise, adresse, contact, email, utilisateur_id))
    deconnexion(conn)
    return 'Client mis-à-jour'
    # except:
    #     return 'Erreur'

def delete_client(id_client):  # utilisateur_id=None):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_clients" where id_client = {id_client}'

    cur.execute(req, ())

    deconnexion(conn)

def search_client(nom_client):
    try:
        conn, cur = connexion()
        req = fr'SELECT id_client, nom, entreprise, adresse, contact, email FROM "t_clients" WHERE nom LIKE ?'
        cur.execute(req, ('%'+nom_client+'%',))
        results = cur.fetchall()
        print(f"results: {results}")
        deconnexion(conn)
        return results
    except:
        return 'Erreur'


# Expéditions


def add_expedition(expedition_id, vente_id, date_expedition, livreur, adresse_livraison, statut, utilisateur_id):
    conn, cur = connexion()
    try:
        req = fr'INSERT INTO "t_expedition" (expedition_id, vente_id, date_expedition, livreur, adresse_livraison, statut, utilisateur_id) values (?,?,?,?,?,?,?)'
        cur.execute(req, (expedition_id, vente_id, date_expedition, livreur, adresse_livraison, statut, utilisateur_id))
        deconnexion(conn)
        return 'Livraison enregistrée'
    except:
        deconnexion(conn)
        return 'Vente déjà livrée'


def update_expedition(vente_id, date_expedition, livreur, adresse_livraison, statut, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_expedition" set vente_id=?, date_expedition=?, livreur=?, adresse_livraison=?, statut=?, utilisateur_id=? where fournisseur_id = {expedition_id}'

    cur.execute(req, (vente_id, date_expedition, livreur, adresse_livraison, statut, utilisateur_id))

    deconnexion(conn)


def delete_expedition(expedition_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_expedition" where fournisseur_id = {expedition_id}'

    cur.execute(req, ())

    deconnexion(conn)


# Fournisseurs

def get_all_fournisseurs():


    try:
        conn, cur = connexion()
        req = fr'SELECT fournisseur_id, nom, adresse, contact, email from "t_fournisseur"'
        cur.execute(req, ())
        results = cur.fetchall()
        # dictionnaire = [{"id": result[0], "nom": result[1], "adresse": result[2], "contact": result[3], "utilisateur": result[4]} for result in results]
        deconnexion(conn)
        return results
    except:
        return 'Erreur'

def search_fournisseur(nom_fournisseur):
    try:
        conn, cur = connexion()
        req = fr'SELECT fournisseur_id, nom, adresse, contact, email FROM "t_fournisseur" WHERE nom LIKE ?'
        cur.execute(req, ('%'+nom_fournisseur+'%',))
        results = cur.fetchall()
        print(f"results: {results}")
        deconnexion(conn)
        return results
    except:
        return 'Erreur'

def add_fournisseur(nom, adresse, contact, email, utilisateur_id):

# :TODO: Traister le cas de id_fournisseur...

    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_fournisseur" (nom, adresse, contact, email, utilisateur_id) values (?,?,?,?,?)'
        cur.execute(req, (nom, adresse, contact, email, utilisateur_id))
        deconnexion(conn)
        return 'Fournisseur enregistré'
    except:
        deconnexion(conn)
        return 'Erreur'


def update_fournisseur(id_fournisseur, nom, adresse, contact, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_fournisseur" set nom=?, adresse=?, contact=?, utilisateur_id=? where fournisseur_id = {id_fournisseur}'

    cur.execute(req, (nom, adresse, contact, utilisateur_id))

    deconnexion(conn)


def delete_fournisseur(id_fournisseur, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_fournisseur" where fournisseur_id = {id_fournisseur}'

    cur.execute(req, ())

    deconnexion(conn)


# Inventaire

def add_inventaire(id_inventaire, date_inventaire, article_id, quantite_theorique, quantite_reelle, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_inventaire" (inventaire_id, date_inventaire, article_id, quantite_theorique, quantite_reelle, utilisateur_id) values (?,?,?,?,?,?)'
        cur.execute(req,
                    (id_inventaire, date_inventaire, article_id, quantite_theorique, quantite_reelle, utilisateur_id))
        deconnexion(conn)
        return 'Inventaire mis à jour'
    except:
        deconnexion(conn)
        return 'Inventaire existant'


def update_inventaire(date_inventaire, article_id, quantite_theorique, quantite_reelle, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_inventaire" set date_inventaire=?, article_id=?, quantite_theorique=?, quantite_reelle=?, utilisateur_id=? where article_id = {article_id} and date_inventaire={date_inventaire}'

    cur.execute(req, (date_inventaire, article_id, quantite_theorique, quantite_reelle, utilisateur_id))

    deconnexion(conn)


def delete_inventaire(date_inventaire, article_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_inventaire" where article_id = {article_id} and date_inventaire={date_inventaire}'

    cur.execute(req, ())

    deconnexion(conn)


# Matières premières


def add_matieres_premieres(matieres_premieres_id, label, unite, fournisseur_id, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_matieres_premieres" (matieres_premieres_id, label, unite, fournisseur_id, utilisateur_id) values (?,?,?,?,?)'
        cur.execute(req, (matieres_premieres_id, label, unite, fournisseur_id, utilisateur_id))
        deconnexion(conn)
        return 'Matière première ajoutée'
    except:
        deconnexion(conn)
        return 'Erreur'


def update_matieres_premieres(matieres_premieres_id, label, unite, fournisseur_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_matieres_premieres" set label=?, unite=?, fournisseur_id=?, utilisateur_id=? where matieres_premieres_id={matieres_premieres_id}'

    cur.execute(req, (label, unite, fournisseur_id, utilisateur_id))

    deconnexion(conn)


def delete_matieres_premieres(matieres_premieres_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_matieres_premieres" where matieres_premieres_id = {matieres_premieres_id}'

    cur.execute(req, ())

    deconnexion(conn)


# Paiements


def add_paiement(paiement_id, type_paiement, montant, vente_id, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_paiement" (paiement_id, type_paiement, montant, vente_id, utilisateur_id) values (?,?,?,?,?)'
        cur.execute(req, (paiement_id, type_paiement, montant, vente_id, utilisateur_id))
        deconnexion(conn)
        return 'Paiement ajouté'
    except:
        deconnexion(conn)
        return 'Erreur'


def update_paiement(paiement_id, type_paiement, montant, vente_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_paiement" set type_paiement, montant, vente_id=?, utilisateur_id=? where matieres_premieres_id={paiement_id}'

    cur.execute(req, (type_paiement, montant, vente_id, utilisateur_id))

    deconnexion(conn)


def delete_paiement(paiement_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_paiement" where paiement_id = {paiement_id}'

    cur.execute(req, ())

    deconnexion(conn)


# Ventes


def add_vente(vente_id, date_vente, article_id, quantite, id_client, utilisateur_id):
    conn, cur = connexion()

    try:
        req = fr'INSERT INTO "t_ventes" (vente_id, date_vente, article_id, quantite, id_client, utilisateur_id) values (?,?,?,?,?,?)'
        cur.execute(req, (vente_id, date_vente, article_id, quantite, id_client, utilisateur_id))

        # Update audit
        dernier_stock = requetage(
            fr'select max(stock_id), quantite from t_audit_stock_articles where article_id = {article_id}')
        dernier_qte = dernier_stock[1]
        # Update du stock
        add_audit_stock(article_id, dernier_qte - quantite, date_vente, utilisateur_id)

        deconnexion(conn)

        return 'Vente ajoutée'

    except:
        deconnexion(conn)
        return 'Error'


def update_vente(vente_id, date_vente, article_id, quantite, id_client, utilisateur_id):
    conn, cur = connexion()
    req = fr'UPDATE "t_ventes" set article_id=?, date_vente=?, quantite=?, id_client=?, utilisateur_id=? where vente_id={vente_id} and article_id={article_id}'

    cur.execute(req, (date_vente, article_id, quantite, id_client, utilisateur_id))

    deconnexion(conn)


def delete_vente(vente_id, utilisateur_id):
    conn, cur = connexion()
    req = fr'DELETE FROM "t_ventes" where vente_id = {vente_id}'
    cur.execute(req, ())

    deconnexion(conn)


print(get_all_clients())
# print(add_approvisionnement(1, '06/04/2024', 3, 10, 1))
# add_paiement(2, 'Carte', 10000,1)
