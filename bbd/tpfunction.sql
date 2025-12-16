/* Exercice 1
a.Retrouvez la fonction stockéeC301T_renvoyerNomUE() dans la liste des sous-programmes de votre base


                        *Tester-la avec l’interface Adminer
                        SHOW CREATE FUNCTION C301T_renvoyerNomUE

                            CREATE FUNCTION C301T_renvoyerNomUE () RETURNS varchar(255) 
                                BEGIN
                                    RETURN "Cours de Bases de Données Avancées (BDA)";
                                END
                        *Tester-la avec une requête SQL
                            SELECT C301T_renvoyerNomUE ()



b.Retrouvez la procédure stockéeC301T_afficherNom()dans la liste des sous-programmes de votre base

                            Tester-la avec l’interface Adminer
                            SHOW CREATE PROCEDURE C301T_afficherNom
                                CREATE PROCEDURE C301T_afficherNom (p_nom VARCHAR(255))
                                BEGIN
                                    SELECT concat("Le nom fourni en paramètre est : ", p_nom);
                                END
                            Tester-la avec une requête SQL
                                CALL C301T_afficherNom ('jey')
c.Appelez la procédure stockéeC301T_afficherNom()pour afficher le nom de l’UE (réfléchissez … un peu ;) )
                            Appelez-la avec l’interface Adminer
                            
                            Appelez-la avec une requête SQL
                            SET @nomUE =NULL;
                            SELECT C301T_renvoyerNomUE() INTO @nomUE;
                            CALL C301T_afficherNom(@nomUE)
 */




-- Exercice 2
-- a.Créez la procédure ajouterMatiere() permettant d’ajouter une matière sans son coef (qui pourra être mémorisé plus tard)
                            DELIMITER //
                            CREATE PROCEDURE ajouterMatiere(m_id INT(11), m_nom VARCHAR(45))
                            BEGIN
                                INSERT INTO C301T_Matieres (id, nom)
                                VALUES (m_id, m_nom);
                            END//
                            DELIMITER ;
-- b.Appelez cette procédure stockée pour ajouter la matière «Informatique»
                            CALL ajouterMatiere(4, 'Informatique')
-- c.Vérifiez que l’ajout c’est bien passé Bien réfléchir aux paramètres nécessaires à la procédure.





-- Exercice 3
-- a.Créez la procédure ajouterMatiereEnseignant() prenant en paramètre un enseignant (son nomet son prénom) et le nomde la matière à lui affecter. 
-- L’enseignant et la matière sont supposés déjà exister dans la base.Bien réfléchir aux opérations nécessaires avant d’ajouter le tuple.

                    DELIMITER //
                    CREATE PROCEDURE ajouterMatiereEnseignant(nom_Ens VARCHAR(40), prenom_Ens VARCHAR(40), nom_mat VARCHAR(45))
                    BEGIN
                        SET @id_Ens = NULL;
                        SET @id_Ens = (
                            SELECT id
                            FROM C301T_Enseignants
                            WHERE (prenom = prenom_Ens AND nom = nom_Ens) 
                        );
                        
                        SET @id_Mat = NULL;
                        SET @id_Mat = (
                            SELECT id
                            FROM C301T_Matieres
                            WHERE (nom = nom_mat)
                        );
                        
                        INSERT INTO C301T_EnsMatieres (idEns, idMat) 
                        VALUES (@id_Ens, @id_Mat); 
                    END//
                    DELIMITER ;

-- b.Appelez cette procédure stockée pour mémoriser qu’Alan Turing enseigne l’informatique.
                    CALL ajouterMatiereEnseignant('Turing','Alan','Informatique')
-- c. Vérifiez que l’ajout c’est bien passé (Alan Turing enseigne à présent 3 matières).
                    SELECT count(idMat)
                    FROM C301T_EnsMatieres en
                    INNER JOIN C301T_Enseignants e ON (en.idEns=e.id)
                    WHERE nom = 'Turing' AND prenom ='Alan' ;



-- Exercice 4
-- a.Créez une fonction stockée renvoyant l’identifiant du cours d’Histoire.
DELIMITER //
CREATE FUNCTION afficherIdCoursHist() RETURNS INT
BEGIN
    SELECT id INTO @idHist FROM C301T_Matieres WHERE nom ='Histoire'
 RETURN 
END;
DELIMITER ;
-- b.Ecrivez une requête qui affiche la liste des enseignants (leur id) d’Histoire(cette requête fait appel à la fonction précédente).