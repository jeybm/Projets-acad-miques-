-- 1. Créez la vue (requête SQL) P301T_V_Biens_EnPeril en exploitant la requête du 1er exercice 
-- sur le LID SQL du TP Unesco
CREATE VIEW P301T_V_Biens_EnPeril as
    Select refBien, Titre,EnPeril,idLangue,TexteDesc
    from P301T_Biens as b, P301T_DescriptionsBiens as d
    where b.refBien = d.refBien and EnPeril = 1;

-- 2. a) Créez la vue P301T_V_Biens_ParPays qui fournit le nombre de biens répertoriés par pays
create view P301T_V_Biens_ParPays as
    select idPays, Nom, NbBiens, NbBiensPeril
    from P301T_Pays as p,P301T_Biens as b ,