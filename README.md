# elephant-carpaccio
Atelier Métode Agile avec SCRUM

## Sujet

Exercice Elephant Carpaccio

Cet atelier a pour objectif de montrer : 
- Comment découper des développements en fonctionnalités de 1 journée à 1 semaine, du point de vue métier ; 
- Comment découper des développements en tranches 15-30 minutes, d'un point de vue développeur. 
### Instructions 
- Se répartir en équipe de 2 à 3 personnes, UN SEUL développeur par équipe. 
- 10 minutes : Préparation - Chaque équipe écrit sur « papier » les 10 à 20 tranches de développement démontrables. Chacune de ces tranches doit être faisable en 3 à 8 minutes. Aucune tranche ne doit correspondre à une création de table de données ou une structure de données, etc.… toutes les démos doivent présenter de vraies séquences d'utilisation et montrer une progression de valeur métier au fur et à mesure. Chacun d’entre elle doit être implémentable (interface comprise) en 2 à 6 minutes
- 15 minutes : Discussion sur les tranches, qu’est-ce qui est ou n’est pas acceptable, recherche de moyen de découper plus finement, etc. 
- 40 minutes : Développement en 5 itérations de développement de 8 minutes, l’horloge ne s’arrête pas. A la fin de chaque itération, chaque équipe démontre son produit aux autres équipes. 
- Debrief 
### Spécification 
Calculer un prix de vente en fonction de trois données d'entrée :
- Un nombre d’articles, 
- Un prix pour l’article, 
- Un code état à 2 lettres (US). 

Sortie : Calculer le prix de la commande, en tenant compte d'une remise calculée sur la valeur de la commande (pas du nombre d’articles) et en ajoutant la taxe liée à l'état. 

Valeur commande	Réduction		
- 1,000 $	3 %		
- 5,000 $	5 %		
- 7,000 $	7 %		
- 10,000 $	10 %		
- 50,000 $	15 %		

Etat	Taxe
- UT	6.85 %
- NV	8.00 %
- TX	6.25 %
- AL	4.00 %
-C A	8.25 %