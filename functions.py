import time

def getcategory(df_tblGymnastes):

    ######### program, uncomment the current category
    ### Saturday from 9am to 12pm
    categorieSelected = ((df_tblGymnastes['Categorie'] == "Niveau 3 U13") |
    (df_tblGymnastes['Categorie'] == "Niveau 3 13+") |
    (df_tblGymnastes['Categorie'] == "Élite 3"))
    ### Saturday from 1pm to 5pm
    # categorieSelected = ((df_tblGymnastes['Categorie'] == "Niveau 5") |
    # (df_tblGymnastes['Categorie'] == "National Ouvert") |
    # (df_tblGymnastes['Categorie'] == "Junior") |
    # (df_tblGymnastes['Categorie'] == "Senior"))
    # # Saturday from 5h45pm to 8pm
    # categorieSelected = ((df_tblGymnastes['Categorie'] == "Niveau 4 U13") |
    # (df_tblGymnastes['Categorie'] == "Niveau 4 13+")
    ### Sunday 8am to 12pm
    # categorieSelected = ((df_tblGymnastes['Categorie'] == "Niveau 2A") |
    #(df_tblGymnastes['Categorie'] == "Niveau 2C")
    ### Sunday 12.30pm to 3.45pm
    # categorieSelected = ((df_tblGymnastes['Categorie'] == "Niveau 2B") |
    #(df_tblGymnastes['Categorie'] == "Niveau 2D")
    ### Sunday 4pm to 8pm
    # categorieSelected = ((df_tblGymnastes['Categorie'] == "Capital City")


    return categorieSelected