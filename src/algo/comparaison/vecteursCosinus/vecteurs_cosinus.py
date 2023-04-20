#similatiré cosinus entre deux fichiers texte.
import numpy as np

class VecteurCos:

    def compare(text1, text2):
        # On commence par créer un vecteur de mots pour chaque texte.
        # On utilise la fonction set() pour supprimer les doublons.
        words = set(text1.split() + text2.split())
        # On crée un vecteur de comptage pour chaque texte.
        vector1 = [text1.count(word) for word in words]
        vector2 = [text2.count(word) for word in words]
        # On calcule la similarité cosinus.
        sim = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        res = {"algo" : "vecteur cosinus", "similarity" : sim, "result" : False}

        if sim < 0.5:
            res["result"] = False
        else:
            res["result"] = True

        return res
