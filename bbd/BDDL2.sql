Create table C301T_departements (
    id int,
    nom VARCHAR(30),
    Primary key (id)
);
Create table C301T_villes(
    id int,
    nom VARCHAR(30),
    idDep int,
    Primary key (id),
    Foreign key (idDep)
        references C301T_departements (id)
);

Alter table C301T_Enseignants
    ADD constraint fk_ensvil_vil
        Foreign key (idVille)
        references C301T_villes (id);


/* exo view */
Create View V_Notes_Etudiants_Matieres as
    select e.id as id , e.nom as nom , e.prenom as prenom, m.nom as matière, note
    from C301T_Etudiants e , C301T_Notes n , C301T_Matieres m
    where e.id = idEtu and m.id = idMat and note > 10;

Create view V_Moyennes_Etudiants_Matieres as
    select id , nom , prenom , matière , round(avg(note),2) as moyenne
    from V_Notes_Etudiants_Matieres
    group by id , matière
        ;

