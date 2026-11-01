# Namazen

Site de Namazen, le cabinet de soins énergétiques de Virginie Gorczinski-Petit à Carnières (59217).

Site statique en une seule page (`index.html`), sans outil de build. Chaque soin a sa propre vue, accessible par son ancre (`#reflexologie`, `#access-bars`, `#lahochi`, `#chakras`, `#communication-animale`, `#passeuse-de-lieux`).

## Voir le site en local

Ouvrir `index.html` dans un navigateur.

## Mettre en ligne

Le site peut être publié gratuitement avec GitHub Pages (Settings > Pages > branche `main`, dossier `/`), relié au domaine namazen59.fr (DNS chez IONOS, fichier `CNAME`).

Site en ligne : https://namazen59.fr

## À compléter

- Tarifs : volontairement « sur demande » partout.
- Photos : ajouter une photo de Virginie (le cabinet est déjà en photo).

## Pages des soins

Chaque soin a sa propre adresse (namazen59.fr/lahochi, ...). Les fichiers `lahochi.html`, `access-bars.html`, etc. sont générés à partir de `index.html` : après chaque modification de `index.html`, lancer `python3 build.py` avant de publier.
