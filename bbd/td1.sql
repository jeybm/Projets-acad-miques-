/*I- LID SQL */
-- 1.Quels biens sont en péril ?
Select refBien, Titre, GPS,DateInsc, Superficie,TypeBien, idPhotoPrincipale
from P301T_Biens
where EnPeril = 1;

-- 2.Combien de biens sont répertoriés par pays ?
Select p.idPays, p.nom as Nom ,count(refBien) as NbBiens
from P301T_LocalisationsBiens as lc , P301T_Pays as p
where lc.idPays = p.idPays
group by p.idPays
order by NbBiens, Nom ;

-- Quelle est la description en français des différents biens (Titre) ?
Select Titre, TexteDesc
from P301T_Langues as lg, P301T_DescriptionsBiens as d, P301T_Biens as b
where d.refBien = b.refBien and d.idLangue = lg.idLangue and Libelle = "français";
 
-- 4. A combien de critères répondent chacun des biens ? Afficher la référence et le titre des biens
-- triés par ordre décroissant du nombre de critères
select b.refBien,Titre,count(ev.numCritere) as NbCritere
from P301T_Criteres as cr,P301T_Biens as b,P301T_EvaluationsBiens as ev 
where cr.numCritere = ev.numCritere and b.refBien = ev.refBien
group by b.refBien
order by NbCritere desc ;

-- 5.Pour chaque photographe, son nom, son prénom, le nombre de photos qu'il a prises sur les
-- biens de l'Unesco (potentiellement aucune!). Résultat trié sur le nombre croissant de photos.
select idPhotographe,Nom, Prenom, count(idPhoto) as nbPhotos
from  P301T_Photographes 
left join P301T_Photos using (idPhotographe)
group by idPhotographe
order by nbPhotos asc;

-- 6.Quels biens ont été photographiés par Barbara BLANCHARD ? (répondez avec des sous-
-- requêtes - pas de jointure !) 

select *
from P301T_Biens
where idPhotoPrincipale in(
    select idPhoto
    from P301T_Photos as ph
    where ph.idPhotographe in(
        select p.idPhotographe
        from P301T_Photographes as p
        where Prenom ="Barbara " and Nom ="BLANCHARD"
    )
);

-- 7.Quels biens ne sont associés à aucune carte? (2 possibilités : a) avec une sous-requête, b) 
-- avec une demi-jointure)
Select *
from P301T_Biens as b
where b.refBien not in (
    select c.refBien
    from P301T_Cartes asc
);

Select *
from P301T_Biens b
left join P301T_Cartes as c using(refBien)
where c.refBien is null;

-- 8.Préambule :   Ecrivez   une   requête   SQL  qui   affiche   le   nombre   de   biens   par   type   de   biens.   Vous
-- devriez obtenir ceci 
Select TypeBien, count(refBien) as NbBiens
from P301T_Biens 
group by TypeBien;

-- 1. Définissez et ordonnez les opérations (l’algo) à réaliser, sur papier,
-- 2. Ecrivez   et   mettez   au   point   les   requêtes   correspondant   à   ces   opérations,   dans   l’ordre défini
Create table P301T_TypesBiens as
    Select distinct (TypeBien) as Libelle
    From P301T_Biens ;
    
ALTER TABLE P301T_TypesBiens
    ADD idTypeBien INT NOT NULL AUTO_INCREMENT PRIMARY KEY;


alter table P301T_Biens
    add idTypeBien int;


Alter table  P301T_Biens
    ADD constraint con_b_t  Foreign key (idTypeBien)
    references P301T_TypesBiens (idTypeBien);


update table P301T_Biens
set idTypeBien = (
    select tb.idTypeBien
    From P301T_TypesBiens as tb
    where Libelle = tb.TypeBien
);
Alter table P301T_Biens
    Drop typeBien;

select b.idTypeBien,Libelle,count(refBien) as NbBiens
from P301T_Biens as b , P301T_TypesBiens as tb
where b.idTypeBien = tb.idTypeBien
group by Libelle
-- 3. Vérifiez que vous n’avez pas perdu d’information