DELIMITER #
Create procedure ajouterEnseignant(p_nom varchar(40), p_prenom varchar(40), p_date date)
BEGIN
INSERT INTO C301T_Enseignants (nom,prenom,dateNaiss) VALUES(p_nom,p_prenom,p_date);
END#
DELIMITER ;

DELIMITER #

Create procedure suppEns(p_nom,p_prenom)
BEGIN
DELETE FROM C301T_Enseignants WHERE nom = p_nom and prenom =p_prenom
END#
DELIMITER ;

call ajouterEnseignant("Berners-Lee","Tim","1999-08-18")


DELIMITER #
CREATE Function nombreEns(nomMatiere varchar(45)) Returns int
BEGIN
return select count(p_id) from C301T_Enseignants e, C301T_Matieres m, C301T_EnsMatieres em WHERE e.id = idENS and m.id = idMat and m.nom = nomMatiere;
END#
DELIMITER ; 

/* Exercice 2 : Ecrire une fonction qui permet de retourner le
nombre d’enseignants qui enseignent la matière Maths */

DELIMITER //

CREATE FUNCTION ensMath() RETURNS int
BEGIN
    SET @idMath =NULL;
    SET @idMath = (
        SELECT  id
        FROM Matieres
        WHERE nom = 'Maths'
    );
    SET @nbEns =NULL;
    SET @nbEns =(
        SELECT COUNT(idEns)
        FROM EnsMatieres
        WHERE idMat = @idMath
    );
    return @nbEns
END//

DELIMITER ;

