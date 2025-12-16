-- Exercices
-- 1. a) Créer une fonction qui renvoie la moyenne des superficies.
DELIMITER ?
CREATE FUNCTION medSup() RETURNS decimal(10,2)
BEGIN
    return (SELECT AVG(Superficie) FROM P301T_Biens);
END?
DELIMITER ;
-- b) Utiliser cette fonction pour afficher tous les biens dont la superficie est inférieure à la superficie
-- moyenne
SELECT * FROM P301T_Biens WHERE Superficie < medSup();

-- 2. a) Créer une fonction qui renvoie la moyenne des superficies pour un type de bien fourni en
-- paramètre.
    DELIMITER #
CREATE FUNCTION supType(typebien varchar(15)) RETURNS decimal(10,2)
BEGIN
    return(SELECT AVG(Superficie) FROM P301T_Biens b WHERE b.idTypeBien IN ( SELECT tb.idTypeBien FROM P301T_TypesBiens tb WHERE tb.Libelle = typebien)  );
END#
    DELIMITER ;
-- b) Utilisez cette fonction pour afficher pour chaque bien, sa référence, son titre, sa superficie, son
-- type de bien, et la superficie moyenne de son type de bien.
SELECT b.refBien,b.Titre,b.Superficie,tb.Libelle,supType(tb.Libelle)
FROM P301T_Biens b, P301T_TypesBiens tb
WHERE b.idTypeBien = tb.idTypeBien;
-- c) Utilisez cette fonction pour afficher tous les biens dont la superficie est inférieure à la superficie
-- moyenne des biens de leur type de bien
SELECT b.refBien,b.Titre,b.Superficie,tb.Libelle,supType(tb.Libelle) AS Moyenne_Type_Bien
FROM P301T_Biens b,P301T_TypesBiens tb
WHERE  b.idTypeBien = tb.idTypeBien AND b.Superficie <= supType(tb.Libelle);

