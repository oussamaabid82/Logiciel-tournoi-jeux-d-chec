# Programme de gestion des tournois, système Suisse, de jeux d'échec 

* ##### Ce programme hors ligne, aide à gérer des tournois, système Suisse, de jeux d'échec, on peut avec créer un tournois, créer des joueurs, générer des rounds et des matchs puis sauvegarder le tournoi à l'aide de TinyDB


* ### Prérequis
	- il faut installer un Shell sur votre ordinateur, sinon vous pouvez utiliser le terminal préinstallé avec votre système d'exploitation:

	- WINDOWS:
		-  touche Windows + R puis tapez 'cmd' puis ENTRER 

	- MAC:
		- Cliquez sur l’icône Launchpad dans le Dock, saisissez Terminal dans le champ de recherche, puis cliquez sur Terminal.
		- Dans le Finder, ouvrez le dossier /Applications/Utilitaires, puis cliquez deux fois sur Terminal.
	 
	- LINUX: 
		- ctrl + alt + t

* ### Démarrage
	- Sauvegardez le dossier chess_tournament_manager telle qu'il est sans rien modifier.
	- Démarrer votre terminal et diriger vous dans le dossier chess_tournament_manager.
	- Installez les modules nécessaires pour le bon fonctionnement du programme
		```bash
		pip install -r requirements.txt
		``` 
	- Maintenant pour démarrer le programme il faut taper dans votre terminal:

		```shell
		python ctm.py
		```
* ### Flake8
	- Pour valider le code au regard de la PEP8 et avoir un rapport flake8-html, il faut effectuer le peluchage du code en tapant dans votre terminal:
		```shell
		python -m flake8 --format=html --htmldir=flake-report
		```
	- Pour éviter que flake8 fait le peluchage du dossier de l'environnement virtuel, veuillez ouvrir le fichier ```.flake8``` dans votre éditeur de texte et veuillez modifier la 3éme ligne comme ce qui suit:
		* exclude = (Nom du dossier de l'environnement virtuel)/*

* ### Fabriqué avec
	- [VSCode](https://code.visualstudio.com/) 
	- [Cygwin](https://www.cygwin.com/install.html)

* ### Versions
	- Bêta

* ### Auteurs
	- Abid Oussama:
 
	 [oussamaabidd@gmail.com](oussamaabidd@gmail.com)

	- Mr Williams De Souza
