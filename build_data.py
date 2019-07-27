# -*- coding: utf-8 -*-
# buld_data by pythonbrad 28/04/2018
import json
import glob

_dict_word = {}
ext = '.lang'

for filename in glob.glob('*' + ext):
    lang = filename.split('.')[0]
    f = open(lang + ext, encoding='utf-8')
    data = f.read()
    f.close()
    data = data.splitlines()
    word_no_translate = []
    word_translate = []

    for i in data:
        if i != '':
            d = i.split('.')
            word_no_translate.append(d[0])
            word_translate.append(d[1])

    data = {'lang': {}, 'mlang': {}}

    for i in range(len(word_no_translate)):
        data['lang'][i] = word_no_translate[i].capitalize()
        data['mlang'][i] = word_translate[i].capitalize()

    _dict_word[lang] = data

# -*- coding: utf-8 -*-

a = """*****L’ÉCOLE – LA CLASSE – L’INSTRUCTION
l’école
la classe
le devoir
un élève
l’instituteur
la leçon
dire
savoir
parler
apprendre
le cahier
le mot
un écolier
un instituteur
la parole
la récréation
un congé
la rentrée
le crayon
les vacances
un exemple
le cours
la voix
punir
écrire
étudier
gronder
instruire
raconter
une étude
la faute
le papier
le problème
la grammaire
l’encre
la page
la punition
le professeur
le bulletin
l’institutrice
scolaire
primaire
obéissant
paresseux
bavarder
enseigner
résoudre
corriger
réciter
attentivement
la rédaction
la conduite
le directeur
le carnet
le sujet
la note
la question
la récompense
le dictionnaire
l’absence
le français
un examen
la désobéissance
le collège
le discours
attentif
silencieux
sûr
répéter
mériter
prononcer
silencieusement
la remarque
un étudiant
une explication
le poème
l’instruction
l’éducation
un accent
une application
la correction
le langage
le texte
une analyse
distrait
sérieux
absent
se taire
diviser
interroger
compléter
fréquenter
citer
une écriture
la dictée
la division
la préparation
la distribution
la règle
la distinction
un enseignement
le lecteur
le progrès
le pensionnaire
redire
signifier
compliquer
ignorer
effacer
dicter
sérieusement
exprès
la copie
la retenue
la réputation
la révision
la répétition
le résumé
la possibilité
une interrogation
le surveillant
la composition
la fable
la signification
le réfectoire
le préau
le propos
l’obéissance
un copain
le règlement
la surveillance
l’ignorance
un brouillon
l’alphabet
classique
correct
bavard
l’exception
questionner
analyser
*****PAYSAGES – CLIMAT – FORMES
la neige
la pluie
le vent
l’air
le côté
froid
doux
chaud
voici
voilà
le coin
la forme
le rocher
la plaine
la colline
large
sombre
magnifique
rond
vilain
abriter
pleuvoir
situer
admirer
souffler
la droite
la foudre
la gauche
la montagne
une averse
le carré
le paysage
un angle
la température
la flaque
le creux
le climat
le sommet
le brouillard
plat
pointu
couvert
épais
neiger
dominer
geler
glacer
le lac
un orage
la pointe
la grandeur
la gelée
la surface
la tempête
la côte
un éclair
la descente
une inondation
énorme
admirable
affreux
boueux
briser
réchauffer
grelotter
la brume
le ravin
le cercle
la géographie
un tas
le fossé
un degré
la masse
l’humidité
la fraîcheur
l’atmosphère
le tonnerre
minuscule
éclatant
aigu
varier
refléter
tremper
largement
le guide
le mont
les ravages
une observation
le tourbillon
la grêle
idéal
épouvantable
gigantesque
fâcheux
bizarre
fondre
prévoir
éclaircir
la bise
la brise
la pente
le couchant
la vallée
la montée
le pic
la perspective
le vallon
un abîme
l’aire
le défilé
le tremblement
le flanc
la végétation
la cime
rude
lisse
massif
monotone
rigoureux
incroyable
divers
propice
horizontal
oblique
vertical
maussade
pittoresque
gravir
tournoyer
dissiper
*****QUALITÉS ET DÉFAUTS
le défaut
bien
poli
plaire
la curiosité
charitable
sot
franc
modeste
savant
brutal
remercier
la colère
tendre
le pardon
le respect
la paresse
généreux
curieux
charmant
pardonner
mal
mieux
sage
méchant
gentil
honnête
mentir
respecter
la conduite
inviter
excuser
la charité
la bonté
un merci
la douceur
le mensonge
le remerciement
une amitié
menteur
simple
fier
sincère
tromper
le compliment
la politesse
une invitation
le dévouement
le bienfaiteur
un vice
la violence
la confiance
la patience
la générosité
la reconnaissance
l’impatience
timide
respectueux
moqueur
sévère
reconnaissant
raisonnable
favoriser
agréer
flatter
accueillir
le reproche
la faveur
la sagesse
l’estime
la franchise
la haine
la sincérité
l’orgueil
le flatteur
un accueil
convenable
indigne
digne
étourdi
mécontent
ignorant
grossier
loyal
pire
vulgaire
moral
jaloux
indifférent
orgueilleux
hypocrite
détester
estimer
se moquer
franchement
sincèrement
le charme
la rage
une brute
mépriser
la gratitude
la vertu
la modestie
la méchanceté
l’ingratitude
un bienfait
la timidité
un caprice
la simplicité
un empressement
la jalousie
l’honnêteté
la bienveillance
la sympathie
avare
docile
trompeur
humble
ingrat
cordial
contrarier
aborder
barrer
acheminer
supprimer
précéder
librement
dès lors
néanmoins
successivement
constamment
ci-joint
fréquemment
une obligation
la résolution
le refus
le symbole
une combinaison
obligatoire
définitif
*****CALCUL ET MESURES
une fois
deux
autre
quatre
quelques
plus
aussi
beaucoup
trois
dix
demi
cinq
huit
droit
moyen
six
nombreux
contenir
rien
trop
tant
peu
le calcul
la poignée
l’abondance
la moitié
un millier
entier
onze
sept
deuxième
troisième
plein
plusieurs
mesurer
combien
également
environ
autant
moins
assez
le nombre
la mesure
une dizaine
la plupart
la quantité
douze
mille
aucun
cent
trois cents
trente
cinquante
vingt
second
quinze
abondant
partager
complètement
certainement
une unité
le contenu
le volume
un chiffre
une erreur
un million
une expérience
la science
nul
quarante
soixante
quatrième
quatorze
total
égal
pareil
redoubler
diminuer
démontrer
ressembler
tellement
le double
la découverte
une douzaine
une centaine
la moyenne
la base
la comparaison
le système
unique
normal
treize
seize
précis
suffisant
comparer
vérifier
doubler
prolonger
multiplier
nullement
entièrement
précisément
évidemment
abondamment
davantage
suffisamment
le partage
la multitude
le comble
la négation
la solution
la mathématique
la multiplication
le cube
la balance
un tiers
le triple
un inventeur
un ingénieur
DJ13 DJ14
la somme
la différence
la soustraction
la division
l’addition
le produit
le quotient
le dividende
le diviseur
le multiplicateur
le multiplicande
l’angle
le degré
isométrique
l’amplitude
parallèle
perpendiculaire
sécant
le segment
la droite
*****LES ALIMENTS – LES BOISSONS- LES REPAS
l’eau
le pain
bon
boire
manger
préparer
la soupe
le café
un œuf
une tartine
le lait
le boulanger
la viande
le morceau
le souper
le beurre
la nourriture
le déjeuner
la faim
le dîner
mauvais
frais
fumer
remplir
préférer
le sucre
la salade
le fromage
le sel
le miel
la farine
la pâte
le chocolat
le repas
la boisson
un aliment
le bonbon
la cuisinière
le besoin
la ménagère
la cerise
la serviette
les provisions
la bière
une assiette
le goûter
gras
délicieux
meilleur
mûr
cuire
mordre
ajouter
vider
verser
nourrir
une orange
le vin
la corbeille
le four
le pot
une part
la soif
la bouteille
le flacon
le dessert
le gâteau
une habitude
l’alcool
l’appétit
le quartier
vide
mélanger
conserver
découper
gâter
la confiture
le plateau
l’huile
la graisse
la crème
la croûte
fameux
habituel
excellent
avaler
déboucher
trancher
rafraîchir
apprécier
habituer
volontiers
le liquide
le mélange
la réserve
le tonneau
la cigarette
le boucher
la pension
la grappe
le thé
la préférence
ivre
tiède
priver
la bonne
une tranche
le cabaret
le buveur
la pastille
une friandise
le festin
l’ivresse
la recette
le cuisinier
la privation
un délice
la conservation
un noyau
le champignon
un penchant
la crêpe
le pâté
la pâtisserie
le restaurant
une frite
la liqueur
l’excellence
sucré
tranchant
préférable
savoureux
gourmand
amer
salé
affamé
exquis
pourvoir
savourer
digérer
*****LE CORPS HUMAIN
la tête
un homme
le cœur
la main
le pied
un bras
les yeux
gros
grand
petit
la femme
la bouche
la figure
la joue
une dent
une oreille
le nez
la peau
la jambe
la taille
le visage
le coude
la fatigue
la langue
la gorge
le doigt
le bonhomme
le corps
un œil
le poing
fort
dormir
lever
former
endormir
respirer
la moustache
le sang
le ventre
le foie
le dos
le cou
le genou
un cheveu
coucher
éveiller
la force
l’épaule
un être
le front
blond
nu
réveiller
pâle
fatiguer
reposer
la poitrine
la lèvre
l’humeur
l’estomac
le sommeil
géant
courber
relever
fortement
le personnage
la mâchoire
humain
abaisser
le poumon
faible
grandir
pencher
écarter
la barbe
le menton
souple
mince
la respiration
la faiblesse
roux
grossir
incliner
baisser
la chevelure
le souffle
vigoureux
développer
le muscle
la veine
le nerf
la paupière
délicat
redresser
le crâne
le songe
un organe
un membre
le nain
un orteil
un individu
une haleine
bossu
le dormeur
le poignet
la hanche
la cuisse
la vigueur
la cervelle
la physionomie
le cerveau
maigre
physique
la créature
la cheville
le rein
le rêveur
le sourcil
le squelette
robuste
infirme
mignon
sain
chétif
recoucher
constituer
maigrir
chatouiller
faiblement
la robustesse
chauve
raide
barbu
culbuter
ronfler
faiblir
pincer
bâiller
calmement
la délicatesse
*****LES SENS – LA VOLONTE – L’INTELLIGENCE
la couleur
rouge
bleu
noir
blanc
vert
devenir
voir
entendre
trouver
vouloir
le bruit
un son
jaune
gris
brun
toucher
revoir
écouter
sentir
la pensée
se souvenir
remarquer
oublier
penser
connaître
la vue
le regard
une odeur
visible
rougir
luire
fixer
le caractère
possible
comprendre
rechercher
falloir
rappeler
un aveugle
la teinte
le goût
foncé
retentir
observer
distinguer
examiner
apercevoir
en effet
l’idée
un esprit
la raison
la volonté
la recherche
l’intelligence
la connaissance
contraire
intelligent
vrai
faux
obliger
réfléchir
deviner
refuser
surmonter
reconnaître
projeter
empêcher
vraiment
les lunettes
un écho
sourd
muet
bruyant
la conscience
la conséquence
la réflexion
véritable
impossible
confondre
décider
renoncer
imaginer
admettre
imposer
s’efforcer
parfaitement
simplement
la blancheur
le tapage
invisible
noircir
la mémoire
une intention
malin
incapable
capable
intellectuel
réel
l’imagination
figurer
persuader
approuver
exiger
supposer
réellement
absolument
suave
violet
multicolore
mauve
pourpre
reconnaissable
entrevoir
exhaler
clairement
une obligation
la résolution
le refus
le symbole
la précision
la soustraction
une fraction
une addition
un oubli
menu
multiple
comparable
moindre
considérable
incertain
inégal
extrême
insuffisant
intense
quelconque
maint
uniquement
relativement
totalement
*****L’INTÉRIEUR ET LE MOBILIER
la table
le livre
le feu
le lit
le tableau
la chose
l’eau
la chambre
la chaleur
la tasse
le charbon
la lampe
le banc
la cuisine
le panier
un objet
la lumière
la pièce
le ménage
une horloge
un intérieur
garnir
recouvrir
placer
allumer
casser
renfermer
la pipe
le moulin
un ordre
l’armoire
le cadre
la couverture
le bureau
le tapis
la chaise
la gravure
la bougie
le rideau
le vase
le berceau
l’incendie
le portrait
la ficelle
le poêle
électrique
luisant
ancien
laid
lumineux
brûlant
central
chauffer
éteindre
arranger
le meuble
la nappe
le désordre
le verre
le gaz
la flamme
le carreau
le fauteuil
doré
pendre
suspendre
appartenir
installer
brûler / bruler
balayer
ranger
la couche
le siège
la pendule
la transformation
le piano
l’étincelle
la serrure
l’électricité
l’allumette
le miroir
le dossier
la vaisselle
la cuillère
la bibliothèque
moderne
redevenir
enfermer
déranger
tapisser
essuyer
abîmer
enflammer
s’asseoir
débarrasser
le coussin
le coffre
la lanterne
le réveil
la cendre
le tiroir
le mobilier
un entretien
net
le briquet
le vestibule
une rampe
le tabouret
la mèche
le libraire
la cire
le fourneau
la sonnerie
le palier
le matelas
le cabinet
le buffet
l’oreiller
la librairie
l’ivoire
le foyer
le chauffage
le cigare
la laideur
la chandelle
le balai
la paroi
la cloison
la tapisserie
un éclairage
la baignoire
le bien-être
l’ampoule
élastique
obscur
la commode
étincelant
replacer
rallumer
le luxe
*****L’INDUSTRIE ET LE TRAVAIL
prendre
faire
le mineur
le forgeron
un ouvrier
le métier
la peine
terminer
procurer
aider
occuper
l’ordinateur
pourquoi
comment
le clavier
une usine
la vapeur
la sueur
la machine
la mine
le marteau
une aide
le conseil
un atelier
un outil
une occupation
un employé
actif
facile
marquer
fabriquer
remplacer
transformer
refaire
frotter
cesser
recommencer
employer
exercer
le patron
une industrie
un ouvrage
difficile
produire
fournir
expliquer
serrer
arrondir
coller
percer
la fabrique
le moteur
un clou
le métal
le couteau
la barre
une activité
une invention
le matériel
la sirène
l’acier
la profession
un emploi
un hangar
mécanique
manuel
industriel
intéressant
graver
défaire
conseiller
scier
tracer
assembler
interrompre
intéresser
péniblement
autrement
particulièrement
spécialement
la production
la pompe
la perfection
la fabrication
un barreau
le ressort
une organisation
la méthode
énergique
ennuyeux
joindre
utiliser
clouer
effectuer
taper
l’ardeur
l’usage
la forge
l’énergie
le fardeau
une utilisation
la satisfaction
le salaire
la tâche
la colle
un appareil
l’entrain
la grève
la négligence
le mécanicien
automatique
joint
métallique
satisfaisant
fatigant
munir
démonter
consacrer
extraire
étirer
accomplir
exécuter
lasser
s’empresser
peiner
persévérer
tâcher
la manufacture
le textile
la métallurgie
*****LES ARTS
la fête
une histoire
joli
chanter
la lecture
la suite
le journal
la statue
le chant
l’œuvre
lire
composer
une image
le chanteur
un artiste
la musique
la chanson
le dessin
le titre
le cirque
le modèle
la beauté
une annonce
distraire
dessiner
fêter
émerveiller
encadrer
illustrer
créer
majestueux
grandiose
la fée
le spectateur
la merveille
le musée
le spectacle
un conte
un auteur
le refrain
le cinéma
le rôle
bravo
un appel
le musicien
la cérémonie
le concert
superbe
exposer
célébrer
un article
un instrument
la représentation
le peintre
la danse
le tambour
le programme
la collection
une affiche
la trompette
la phrase
le récit
le poète
la scène
le théâtre
parfait
remarquable
exprimer
informer
imprimer
applaudir
la revue
le bal
un acteur
la poésie
la brochure
une introduction
le chapitre
la peinture
une exposition
un écrit
un orgue
le talent
la création
un écrivain
un exemplaire
la photographie
le rapport
le pinceau
le chef-d’œuvre
la flûte
le mystère
magique
prodigieux
extraordinaire
relire
colorer
copier
conter
sensationnel
le proverbe
une estrade
le journaliste
la mélodie
le ton
l’imprimerie
une émission
un danseur
un illustré
un écran
un imprimé
l’art
le violon
la photo
un orchestre
la télévision
la décoration
la gazette
le photographe
un trait
un album
le style
le décor
une imitation
sonore
mélodieux
original
harmonieux
contempler
certes
*****L’AGRICULTURE
le jardin
le cheval
la campagne
la cour
la prairie
le travail
travailler
la vache
le lapin
la plante
le fermier
la cage
le sol
le blé
la ferme
une sorte
une poule
le jardinier
une herbe
la paille
la gerbe
le domestique
le grain
le poussin
le champ
le pré
semer
garder
planter
arracher
une étable
le mouton
le légume
la récolte
le canard
le tabac
le cultivateur
le travailleur
la haie
la pelouse
le veau
la chèvre
le paysan
la betterave
le pois
la chaîne
entretenir
mener
cultiver
arroser
une écurie
un âne
le laboureur
le foin
la besogne
un bœuf
le berger
le rosier
le gazon
le terrain
la graine
la barrière
la charrue
le chou / les choux
le parterre
brouter
aboyer
la niche
le cochon
le raisin
le poulet
le porc
le valet
la meule
entasser
le labeur
la fourche
le poireau
le piquet
le pâtre
la mare
la grange
le seau
le fouet
lier
labourer
récolter
germer
la vigne
la culture
la brebis
le lin
la moisson
le lien
l’agriculture
le bétail
le sillon
le campagnard
le géranium
un épi
le chrysanthème
la jacinthe
le poulailler
pénible
rustique
agricole
las
paisible
laborieux
suer
faucher
épanouir
ferrer
enfouir
fouetter
croître
céder
atteler
faner
répandre
*****VERGER – BOIS – CHASSE - PÊCHE
la fleur
la feuille
un arbre
le coup / tout à coup
regarder
chercher
la poire
la branche
la chasse
le chasseur
la pomme
le verger
une ombre
le pommier
le feuillage
le poirier
le sentier
le buisson
la renoncule
une allée
le fruit
la forêt
le chêne
fruitier
tuer
couper
traverser
parcourir
tirer
le bois
chasser
entourer
une échelle
le sapin
un arbuste
la hache
un pêcheur
le hêtre
le tronc
la noix
le bûcheron
vierge
humide
pêcher
jaunir
se noyer
permettre
se presser
grimper
abattre
fleurir
mûrir
laisser
à travers
la ligne
le lièvre
le fusil
le cerisier
une aventure
le filet
un hameçon
la rangée
la trace
la flèche
sec
poursuivre
surprendre
craquer
cueillir
longtemps
la piste
la poursuite
la prise
la portée
une écorce
la cueillette
fendre
viser
effrayer
tourbillonner
inquiéter
longuement
la touffe
la pêche
une inquiétude
la frayeur
le domaine
forestier
flamber
épouvanter
lâcher
le fagot
la rosée
le gibier
la bûche
le pâturage
le piège
le tir
le bosquet
le craquement
le calice
la traversée
la sève
la lisière
le bourgeon
le rameau
la clairière
les ronces
la corolle
la jonquille
le coquelicot
le gland
un œillet
l’anxiété
reverdir
longer
parsemer
dépouiller
joncher
anxieux
*****GESTES ET MOUVEMENTS
la promenade
le pas
finir
tomber
rentrer
ouvrir
aller
rester
donner
pousser
promener
entrer
vite
le mouvement
la grâce
tourner
suivre
marcher
reprendre
tenir
monter
battre
ramener
jeter
poser
descendre
déposer
emporter
frapper
glisser
apporter
accompagner
ramasser
arrêter
lentement
un acte
une action
la rapidité
le geste
immobile
remonter
soulever
attirer
enlever
imiter
remuer
danser
bouger
avancer
précipiter
retirer
bousculer
agiter
accourir
lancer
rapporter
accrocher
doucement
légèrement
le signe
la chute
le signal
la façon
retenir
disposer
transporter
renverser
se dépêcher
vivement
rapidement
facilement
debout
la position
le choc
fixe
lent
tordre
reculer
secouer
maintenir
claquer
plier
retomber
agir
franchir
reporter
repousser
appuyer
brusquement
subitement
une agitation
brusque
nerveux
habile
introduire
rejeter
redescendre
la secousse
la pression
le zèle
la hâte
la grimace
une allure
un clin d’œil
vif
mobile
inerte
saisissant
gracieux
continuel
maladroit
prompt
hésitant
irrégulier
mouvoir
redonner
manier
ramper
saisir
remporter
hâter
énerver
aplatir
hausser
fixement
aisément
promptement
continuellement
élégamment
maladroitement
*****ÉPOQUE – TEMPS - SAISONS
le matin
le soir
une année
midi
la semaine
la journée
le jour
le mois
la nuit
une heure
demain
hier
avant
enfin
jamais
parfois
après
souvent
quand
alors
toujours
vendredi
jeudi
lundi
mardi
la matinée
mercredi
samedi
dimanche
la date
la montre
la minute
le moment
la glace
la soirée
le début
le lendemain
le temps
un an
agréable
favorable
soudain
maintenant
dès que
tôt
tard
déjà
minuit
l’été
l’hiver
la saison
le printemps
le commencement
l’après-midi
l’automne
aujourd’hui
aussitôt
immédiatement
mars
octobre
juillet
janvier
avril
juin
décembre
mai
septembre
la veille
novembre
un instant
février
un quart
une seconde
août
désagréable
suivant
terrible
régulier
subir
durer
l’avenir
le futur
le trimestre
une époque
le présent
la période
le siècle
violent
rarement
autrefois
actuellement
dernièrement
durant
tantôt
sans cesse
la durée
Noël
Pâques
la quinzaine
éternel
journalier
actuel
quotidien
dater
déchaîner
le passé
le grondement
le calendrier
la demi-heure
la bourrasque
matinal
orageux
pluvieux
antérieur
mensuel
printanier
final
perpétuel
annuel
immédiat
étouffant
refroidir
succéder
retarder
terriblement
avant-hier
sitôt
jadis
violemment
désormais
*****VÊTEMENTS – TOILETTE - PARURES
nouveau
mettre
la robe
le bouton
la poche
le chapeau
la toile
une écharpe
la laine
la tache
le soulier
le parapluie
le manteau
un habit
le fil
propre
neuf
laver
couvrir
remettre
changer
étendre
allonger
déchirer
vêtir
la chemise
le sac
le linge
le sabot
le tablier
le mouchoir
le ruban
la chaussure
le bonnet
la casquette
la culotte
le cuir
la canne
le chiffon
une aiguille
le vêtement
un anneau
sale
précieux
coudre
coiffer
tricoter
repasser
sécher
tailler
le costume
la botte
le trou
le pantalon
le veston
le drap
la qualité
le pardessus
revêtir
chausser
dérouler
nettoyer
user
habiller
soigneusement
la perle
la tenue
la paire
la blouse
la soie
la manche
le gant
le tissu
la ceinture
les ciseaux
le velours
boucler
envelopper
essayer
déshabiller
ordinairement
la mode
la boucle
le coton
le tailleur
la dentelle
le bijou / les bijoux
le pli
le nœud
élégant
ravissant
déplaire
replier
élargir
trouer
broder
voiler
ôter
raccommoder
le gilet
le jupon
le corsage
le satin
un ornement
l’étoffe
la bague
le bracelet
la chaussette
une coiffure
le collier
une parure
la couture
le foulard
le lambeau
le bijoutier
le capuchon
l’imperméable
un pan
la couturière
la pantoufle
le paletot
les haillons
coquet
soyeux
artificiel
ample
nouer
onduler
embellir
négliger
renouveler
déployer
parer
retrousser
endosser
tacher
fourrer
nettement
fièrement
le parfum
*****SPORTS ET JEUX
la poupée
la joie
le plaisir
l’amusement
le jeu / les jeux
premier
dernier
joyeux
heureux
jouer
la balle
la partie
le jouet
la boule
la course
le camarade
amusant
crier
perdre
cacher
la coupe
la corde
le joueur
le groupe
le numéro
l’exercice
balancer
gonfler
réussir
attraper
la marche
la ronde
la bande
le bassin
la vitesse
l’arbitre
le ballon
le but
l’équipe
la chance
courir
amuser
gagner
la difficulté
plonger
s’écrier
aligner
la lutte
l’adversaire
la balançoire
sauter
rouler
ensemble
le match
nager
lutter
gaiement
la distraction
le succès
bondir
annoncer
joyeusement
le bond
un essai
rejoindre
élancer
la reprise
la farce
le hasard
désigner
la file
l’effort
le résultat
le concours
disputer
récompenser
le sport
les loisirs
le favori
épuiser
proclamer
risquer
se débattre
le risque
l’union
la facilité
le football
glissant
entraîner
le masque
décourager
participer
exciter
l’épreuve
l’équilibre
l’élan
adroit
pratiquer
la cachette
le cortège
inspirer
forcer
agacer
la pratique
le saut
l’échec
drôle
triompher
le lot
l’insigne
la dispute
la passe
la piscine
la glissoire
le champion
la revanche
l’entraînement
triomphant
passif
détendre
le parti
le flambeau
la défaite
le fantôme
l’acclamation
la kermesse
le carrousel
indien
périlleux
attribuer
l’agrément
l’arc
la réussite
la gymnastique
la colonie
la magie
agile
fantastique
exigeant
masquer
*****LA MAISON – LE BATIMENT
la maison
la porte
la fenêtre
bas
la cheminée
le grenier
la tour
le mur
le toit
la salle
le château
la façade
vaste
haut
construire
commencer
habiter
la brique
la cave
la vitre
la fumée
l’escalier
le salon
l’étage
la construction
le monument
le volet
la clé / la clef
la demeure
l’appartement
la tuile
le bâtiment
le seuil
le plan
le corridor
l’habitant
profond
immense
blanchir
réparer
fermer
loger
bâtir
creuser
pénétrer
dresser
la sortie
la planche
l’entrée
l’habitation
le palais
la propriété
le propriétaire
le plafond
solide
étroit
soutenir
peindre
achever
enfoncer
la caverne
l’ouverture
la villa
la tente
le local
le parquet
la ruine
le domicile
la situation
la galerie
le couloir
la grille
la description
la sonnette
un établissement
un hôtel
la colonne
les débris
l’abri
le souterrain
louer
établir
entreprendre
refermer
décharger
demeurer
la muraille
le balcon
la poutre
la cabane
le refuge
l’auberge
l’architecte
le plancher
la terrasse
le tuyau
l’entreprise
l’appui
écrouler
le chalet
l’ardoise
la pile
l’entrepreneur
la chaumière
la dalle
le chaume
la baraque
le logement
l’occupant
l’extrémité
la destruction
l’emplacement
le pavillon
l’exécution
la mansarde
le logis
la réparation
l’immeuble
les matériaux
le rez-de-chaussée
*****LES VOYAGES
le chemin
le vélo
revenir
pouvoir
venir
sortir
partir
monter
retourner
attendre
arriver
la route
la voiture
le voyageur
le tram
le voyage
l’automobile
le passage
l’accident
conduire
continuer
retrouver
approcher
diriger
éviter
charger
quitter
la roue
le camion
le promeneur
l’adieu
la circulation
la chaussée
le pavé
l’arrêt
le chariot
la charrette
l’excursion
le trottoir
romain
prudent
découvrir
amener
croiser
l’avion
la direction
le pont
le chauffeur
l’imprudence
le départ
la poussière
le trajet
le carrefour
complet / complète
tranquille
prêt
impatient
parvenir
voyager
indiquer
réserver
circuler
écraser
apprêter
traîner
seulement
tranquillement
l’aviateur
la borne
la valise
la prudence
le détour
la lenteur
le tournant
le projet
le contact
inconnu
imprudent
anglais
enchanté
allemand
aboutir
regagner
reconduire
ralentir
déplacer
filer
dépasser
rattraper
emmener
la charge
la station
l’indication
le transport
l’obstacle
la sécurité
la malle
l’essence
l’impossibilité
américain
surgir
détourner
égarer
manœuvrer
merveilleusement
difficilement
le terme
la fusée
le panache
le panorama
l’animation
l’approche
le séjour
le véhicule
l’imprévu
la tranquillité
le réservoir
le sens
la bicyclette
l’aéroport
le taxi
une halte
le garage
la mallette
l’inconvénient
incomplet / incomplète
pressé
colonial
repartir
camper
border
atterrir
attarder
différer
quoique
toutefois
prudemment
les vacances
le plaisir
la traversée
*****LES ANIMAUX
le chat
l’animal
le chien
le nid
l’oiseau
l’hirondelle
la plume
la patte
l’abeille
la tigresse
l’insecte
l’aile
le coq
la mouche
le poisson
la bête
la souris
le papillon
le cri
le panda
le poil
la fourmi
utile
détruire
envoler
protéger
voler
élever
blesser
le zèbre
l’os
le bec
le merle
le plumage
le renard
la grenouille
le moineau
le corbeau
l’ours
le crapaud
le pinson
la griffe
le pigeon
la chair
le rossignol
la queue
la caresse
piquer
couver
siffler
attacher
le lion
le loup
le troupeau
la femelle
le vol
la fourrure
l’araignée
la perdrix
l’écureuil
sauvage
fidèle
lécher
dévorer
détacher
caresser
le singe
le rat
la tortue
le protecteur
la corne
l’éléphant
le cygne
nuisible
furieux
féroce
cruel
ronger
hurler
planer
bourdonner
gratter
guetter
le coucou
le tigre
le chameau
la protection
la coquille
la race
crever
trotter
le fauve
la colombe
le monstre
la clochette
l’aigle
l’arête
l’écaille
l’agneau
le cavalier
le museau
la proie
le gazouillement
la girafe
le serpent
l’alouette
le phoque
le cerf
le moustique
le chevreuil
la guêpe
le perroquet
l’espèce
le ver
le hérisson
redoutable
farouche
craintif
poilu
rusé
effrayant
hérissé
familier
voltiger
redouter
galoper
taquiner
grogner
rattacher
gazouiller
rôder
le cheval
la jument
le porc
la truie
le brochet
le sanglier
le marcassin
la laie
le poulain
*****VILLE – VILLAGE – UNIVERS - DIMENSIONS
la rue
la terre
le soleil
le monde
la ville
la place
le ciel
long
loin
devant
le nuage
le village
la lune
le lieu
la fin
le point
l’avenue
le rayon
le parc
l’endroit
le bout
le milieu
le fond
clair
court
éclairer
disparaître
autour
en face de
parmi
la commune
l’espace
la longueur
le centimètre
aux abords
le boulevard
le désert
prochain
supérieur
paraître
ici
dessous
dessus
dehors
auprès
là-bas
derrière
le nord
l’étoile
la région
la hauteur
le mètre
le centre
l’extérieur
l’apparition
le lointain
la distance
l’horizon
merveilleux / merveilleuse
apparaître
arrière
hors
au-dessus
le sud
le kilomètre
la cité
le niveau
splendide
ensoleillé
éblouir
illuminer
obscurcir
le professeur
la limite
la ruelle
l’étendue
l’océan
l’obscurité
l’île
la frontière
la disparition
l’univers
la dimension
inférieur
infini
terrestre
limiter
rapprocher
rayonner
environner
resplendir
reparaître
ailleurs
l’astre
le piéton
le crépuscule
la capitale
la contrée
l’aurore
la clarté
la population
le hameau
la splendeur
l’épicier
l’arrondissement
le villageois
les ténèbres
une lieue
le firmament
l’azur
la zone
l’épaisseur
morne
proche
étoilé
ardent
radieux
grandiose
céleste
populaire
officiel
communal
bienfaisant
universel / universelle
serein
voter
infiniment
là-haut
les alentours
le suffrage
*****EAUX – MINÉRAUX - VÉGÉTAUX
la nature
la rose
le bouquet
le fer
l’or
la rivière
la tulipe
la violette
la pierre
la mer
le lilas
le parfum
la source
le bleuet
le ruisseau
le marron
léger
différent
sembler
le sable
la matière
le fleuve
le cuivre
le murmure
la plage
la racine
la mousse
le bloc
le bâton
la grotte
l’étang
le reflet
la baguette
la marguerite
la pâquerette
le muguet
la goutte
rare
pur
lourd
dur
brillant
couler
parfumer
briller
dedans
la tige
la boue
la vague
le brin
le caillou / les cailloux
semblable
écouler
mouiller
le marbre
l’épine
la plaque
le roseau
le plomb
le torrent
la différence
le marronnier
le puits
mou
naturel / naturelle
flotter
inonder
la fontaine
l’écluse
l’apparence
le diamant
transparent
purifier
déborder
engloutir
fouiller
pourrir
naturellement
profondément
la verdure
le lis / le lys
l’onde
l’éclat
le peuplier
le jet
le gravier
le flot
le courant
l’aspect
la roche
le caoutchouc
le pétrole
la chaux
le suc
le tilleul
la primevère
le barrage
le buis
le lierre
la houille
végétal
limpide
murmurer
provenir
débiter
ruisseler
jaillir
embaumer
durcir
durement
au sein de
le chêne
le gland
l’érable
la ferraille
le schiste
le calcaire
l’émeraude
le cristal
le hêtre
*****LE COMMERCE
rendre
la vitrine
la foire
le marchand
le client
l’argent
le magasin
vendre
acheter
valoir
posséder
l’achat
l’étalage
le bazar
le franc
la marchandise
la caisse
le paquet
le sou
l’affaire
calculer
distribuer
représenter
proposer
obtenir
payer
coûter
compter
le reste
le billet
le trésor
le produit
la somme
le prix
l’économie
le commerce
le compte
le kilogramme
l’occasion
le poids
la commission
livrer
choisir
profiter
étaler
prêter
le carton
la vente
la valeur
l’offre
l’amateur
le vendeur
la demande
la bourse
le capital
le manque
l’acheteur
l’avantage
le profit
le choix
le commerçant
l’intérêt
réduire
inscrire
enrichir
peser
réaliser
discuter
épargner
vanter
la fortune
la marque
la remise
la liste
la boutique
la perte
la banque
la série
la richesse
un centime
la dette
le détail
le bénéfice
le banquier
la commande
l’échantillon
le notaire
le représentant
le portefeuille
la monnaie
commercial
avantageux
dépenser
ruiner
échanger
régler
faciliter
réclamer
augmenter
associer
principalement
un avoir
le livret
la démarche
la tentation
la prospérité
la dépense
l’échange
le montant
la réclame
l’inscription
la boucherie
le secrétaire
l’engagement
la garantie
le comptoir
le paiement
le négociant
l’aisance
la ressource
DJ13
la possession
le fonds
gratuit
coûteux
aisé
répartir
protester
importer
traiter
acquérir
*****LA COMMUNICATION
le train
la gare
passer
porter
encore
ensuite
bientôt
la carte
le bord
la lettre
le port
répondre
recevoir
manquer
envoyer
depuis
jusque
partout
lorsque
le facteur
la locomotive
le marin
le téléphone
le retard
l’attention
le bateau
la boîte / la boite
rapide
renvoyer
encombrer
cependant
peut-être
la poste
la barque
le navire
le wagon
la réponse
la voile
la tournée
l’adresse
l’avance
l’arrivée
la voie
le quai
la correspondance
dégager
adresser
éloigner
atteindre
recommander
tandis que
la cabine
le porteur
la destination
le changement
le courrier
l’attente
le sifflet
le canot
fragile
précédent
tarder
déclarer
signaler
provoquer
embarquer
directement
généralement
finalement
sûrement
le timbre
le canal
la signature
l’équipage
les bagages
l’expédition
la portière
le renseignement
l’enveloppe
le télégramme
le passager
le sifflement
le naufrage
la catastrophe
l’interruption
le dépôt
l’envoi
la communication
urgent
personnel / personnelle
fréquent
exact
rompre
débarquer
expédier
téléphoner
transmettre
renseigner
communiquer
continuellement
probablement
régulièrement
exactement
quelquefois
l’aviation
le pirate
la marine
le matelot
le poteau
le conducteur
le message
la messagère
le colis
le phare
l’assurance
l’autorisation
le mât
direct
constant
éblouissant
contrarier
aborder
barrer
acheminer
supprimer
précéder
librement
dès lors
néanmoins
successivement
*****JOIES ET PEINES
cher / chère
aimer
pleurer
le bonheur
le sourire
triste
calme
content
malheureux
gai
rire
se réjouir
se fier
espérer
malheureusement
la peur
la larme
le soupir
le rêve
le regret
craindre
trembler
se fâcher
heureusement
dommage
la douleur
la surprise
le doute
la pitié
l’envie
l’espoir
le chagrin
la tristesse
inquiet / inquiète
affectueux
horrible
songer
consoler
troubler
étonner
éprouver
se contenter
désirer
rêver
regretter
tristement
gentiment
la honte
l’admiration
le désir
les pleurs
l’émotion
l’espérance
le souci
l’impression
l’expression
l’ennui
la gaieté
chéri
honteux / honteuse
convenir
confier
envier
rassurer
ressentir
oser
attrister
hésiter
embarrasser
tendrement
affectueusement
l’amour
la terreur
la fureur
la tendresse
la désolation
la crainte
le contentement
la passion
l’attachement
l’étonnement
le désespoir
l’illusion
l’horreur
l’angoisse
l’embarras
le remords
douloureux
désireux
sensible
soupirer
douter
calmer
pâlir
frissonner
tourmenter
bouleverser
agréablement
le trouble
le découragement
le sentiment
l’exclamation
l’affection
la mélancolie
la déception
l’hésitation
l’attrait
la compassion
l’enthousiasme
ravi
sinistre
lugubre
rieur
riant
consolant
étonnant
mélancolique
regrettable
confus
jouir
émouvoir
chérir
frémir
enchanter
affectionner
impressionner
tressaillir
égayer
le frisson
le ressentiment
*****GOUVERNEMENT ET JUSTICE
le roi
le voleur
la reine
le pays
l’agent
le gendarme
la couronne
le gardien
la princesse
avouer
accuser
le prince
le chef
la victime
l’inspecteur
le témoin
le seigneur
la paix
la vérité
la séance
le comte
libre
juste
belge
puissant
royal
juger
régner
commettre
le chevalier
la politique
le juge
la loi
la promesse
la police
le repentir
la puissance
l’amende
le tort
le bourgmestre
coupable
flamand
innocent
contribuer
témoigner
prouver
menacer
pécher
condamner
sévèrement
le crime
le duc
la nation
le ministre
le tribunal
le motif
la réunion
la proposition
la fonction
le jugement
le défenseur
la justice
le royaume
l’empereur
le président
le bandit
l’autorité
le marquis
le gouvernement
la conférence
l’administration
le règne
l’assemblée
la majesté
l’empire
la république
le témoignage
le maire
l’enquête
la décision
la condition
le brigand
l’opinion
la discussion
illustre
imposant
jurer
prétendre
dérober
abuser
conclure
gouverner
autoriser
adoucir
interdire
garantir
convaincre
couronner
soupçonner
offenser
acquitter
le policier
le souverain
l’injustice
la conviction
le congrès
le trône
l’avocat
l’incident
monseigneur
le condamné
l’innocence
le communiqué
l’indépendance
injuste
absolu
solennel / solennelle
honorable
majestueux
national
responsable
indépendant
implorer
présider
nier
révéler
maudire
procéder
accabler
attester
*****L’ARMÉE
le soldat
le courage
la poudre
le drapeau
le service
le danger
la guerre
le rang
la permission
le salut
brave
dangereux
courageux
général
réunir
se dévouer
éclater
obéir
encourager
ordonner
abandonner
s’emparer
l’arme
la prison
la garde
la victoire
la patrie
la bataille
la liberté
le capitaine
la troupe
l’armée
le militaire
le prisonnier
la défense
l’officier
l’alerte
l’honneur
le camp
l’ennemi
le combattant
engager
avertir
échapper
délivrer
fuir
constater
défendre
surveiller
libérer
s’enfuir
organiser
armer
vaincre
attaquer
résister
rassembler
commander
justement
le canon
la gloire
le sabre
la fuite
le clairon
le régiment
le combat
l’épée
le képi
le désastre
le héros
formidable
vaillant
vainqueur
effroyable
prévenir
réfugier
soumettre
défiler
combattre
tenter
grouper
guider
féliciter
envahir
supplier
la preuve
le sacrifice
la médaille
un allié
l’attaque
le sergent
le colonel
l’accord
la manœuvre
la résistance
le mérite
le commandement
le commandant
intervenir
recourir
sacrifier
décorer
venger
conquérir
opposer
disperser
la caserne
les préparatifs
le bataillon
la torture
le blessé
le pistolet
la retraite
l’abandon
le lieutenant
le casque
le patriote
la lance
le conquérant
le bombardement
le poignard
le revolver
l’alliance
l’obus
l’explosion
l’assaut
l’offensive
sublime
lamentable
héroïque
neutre
torturer
ébranler
fusiller
solliciter
aux dépens de
le contact
la dague
la hache
l’escadron
*****VIE HUMAINE – MALADIES - HYGIÈNE
le malade
vieux
la mort
la vie
le docteur
la cause
le silence
les soins
jeune
seul
vivre
soigner
mourir
souffrir
assister
le bébé
la tombe
la crise
l’âge
le médecin
le cimetière
le malheur
le vieillard
l’hôpital
mortel
revivre
sauver
salir
guérir
promettre
naître étouffer
proprement
hélas
la maladie
le bain
le tombeau
la jeunesse
le repos
la propreté
la santé
l’état
la toilette
la souffrance
le cas
la présence
le deuil
l’orphelin
la naissance
l’opération
le secours
fou
âgé
préserver
plaindre
veiller
exister
baigner
désespérer
le cadavre
l’utilité
la plaie
la consolation
la blessure
le remède
le sanglot
l’enterrement
l’existence
la précaution
l’ambulance
vivant
solitaire
vieil / vieille
rétablir
s’évanouir
raser
aspirer
se désoler
opérer
gémir
saigner
accepter
délaisser
gravement
le régime
la folie
le soulagement
la solitude
le traitement
la fièvre
la plainte
la guérison
la vieillesse
périr
affaiblir
secourir
soulager
expirer
ranimer
isoler
consulter
enterrer
se résigner
supporter
le confrère
l’idiot
la peste
l’assistant
la coupure
la saleté
le frisson
la destinée
la médecine
l’éternité
le mourant
le fléau
la grippe
le pou / les poux
le rhume
le gémissement
le chevet
le défunt
le pharmacien
le poison
la brûlure
fiévreux
soigneux
fatal
plaintif
insupportable
superficiel
stupide
tousser
cracher
empoisonner
affliger
prodiguer
renaître
vieillir
sangloter
*****LES MOTS GRAMMATICAUX ESSENTIELS
avec
pour
sur
lui
même
si
pendant
mais
puis
car
dans
tout
comme
chaque
sous
sans
celui
ceux
par
leur
très
vers
entre
contre
tous
donc
presque
chacun
surtout
pourtant
malgré
cela
eux
lequel
laquelle
lesquels
lesquelles
là
chez
parce que
près de
puisque
dont
afin de
afin que
ni
quel
quelle
quels
quelles
ainsi
envers
quoi
plutôt
ça
le sien
selon
auquel
sauf
le nôtre
le vôtre
mien
ceci
duquel
desquels
desquelles
sinon
pourvu que
à laquelle
vous
nous
il
elle
ils
elles
tu
c’est
bien que
sauf que
mais
*****LES USTENSILES DE CUISINE
Le plat
L’assiette
L’assiette de sauce
Le verre
La hache
La casserole
La marmite
La poêle
La fourchette
La cuillère
La cuillère à sauce
Le pilon
Le mortier
Le mortier à taro
Le couteau
La cuillère à trou
*****LES PARTIES DU CORPS
Ma tête
Mes cheveux
Ma nuque
Ma face
Le front
Mon front
Mon œil
Mes yeux
Mon nez
Ton nez
Ma joue
Mes joues
Ma bouche
Mes lèvres
L’intérieur de ma bouche
Ma dent
Mes dents
Leurs dents
Ma langue
Ma gorge
Mon cou
Mon menton
La main
Les mains
Ma main
Mes mains
Ma paume de main
Mon doigt
Mes doigts
Mon ongle
Mes ongles
Mon sein
Mes seins
Mon nombril
Mon ventre
Mon dos
Mes reins
Mes cuisses
Mon pied
Mes pieds
Mon orteil
Mes orteils
Ma plante des pieds
La queue
La queue de chien
La queue de cheval
La queue de singe
La queue de poisson
*****LES REPAS
La nourriture
Le plantain
Le plantain mûr
La banane
La banane mûre
Le couscous de manioc
Le couscous de manioc
Le taro
Le couscous
Le maïs
L’igname blanc
L’igname jaune
Le macabo
Le riz
Le haricot
Le haricot pilé
Le macabo rappé
Le plantain pilé
Les pommes
Les pommes de France
Les pommes pilées
Le Nkui
Le couscous nkui
Le ndolè
Le plantain malaxé
La banane malaxée
Le légume
Le melon
Les feuilles de melon
La patate
Les feuilles de patate
L’huile
L’huile d’arachide
L’arachide
L’arachide grillée
L’eau
L’eau des habits
L’eau des assiettes
Le lait
L’eau du haricot
L’oignon
Le sel gemme
La tomate
L’orange
Le sucre
Le tapioca
Le piment
Le pain
La viande
Le vin
La sauce
La boullie
Les beignets
Le pistache
L’eau à boire
Le sel
L’arachide salée
La prune
Le prunier
L’avocat
L’avocatier
La mangue
Le manguier
Le bananier
Le doigt de banane
Le doigt de plantain
Le grain d’arachide
*****LES OBJETS
La pierre
L’argent
La porte
Le ciment
Le sable
Le seau
La cuvette
La clé
Le savon
Le pétrole
La fumée
La cigarette
L’ardoise
Le bic
Le crayon
La télévision
La radio
Le bandit
Le fer à repasser
Le sac
La voiture
Les chaussures
La maison
La poubelle
La terre
Le bac à ordure
La fleur
Le pot de fleur
Les jouets
L’avion
La lame
La table
La chaise
L’arbre
La porte
L’aiguille
La seringue
La fenêtre
L’information
L’homme
La femme
La fille
L’enfant
La route
La pluie
L’oreiller
La houe
La machette
La rivière
Le plafond
Le calendrier
La fête
L’armoire
L’épine
Le ballon
Le tailleur
La prison
Le prisonnier
L’essence
La bouteille
Mon ami
Mon petit frère
Mon père
Le feu
La lumière
Le bois
Le lit
Le drap
La photo
Le cahier
Le livre
La lettre
La montre
La machine
La calculatrice
La torche
Le froid
Le ventilateur
La saison sèche
La saison pluvieuse
Le ciel
En l’air
La vérité
Ceci (ci)
Pour moi
Le côté
Gauche
Droite
Le foyer
La langue
Les marchandises
Un blanc
Une boîte
Une boîte
La couverture
Chose
Le sol
Le mur
L’infirme
Le chanceux
*****LES ANIMAUX
Le chien
Le cabri
Le chiot
Le bœuf
Le veau
Le cheval
Le petit du cheval
Le poussin
Le coq
Le canard
La panthère
Le lion (roi de la forêt)
L’éléphant
L’écureuil
Le porc épic
Le porc
Le porcelet
Le cafard
La mouche
L’abeille
Le moustique
L’oiseau
L’épervier
Le lézard
Le serpent
La chenille
Les fourmis magnantes
Les fourmis
Les termites
L’araignée
Le moineau
Le rat
Le hibou
Le pou
Le poisson
Le poisson fumé
Le poisson fumé
Les crevettes
Le corbeau
La chique
Le boa
La grenouille
Le mille pattes
Le singe
Le chimpanzé
Le mouton
La sauterelle
*****LES TEMPS
Le matin
Le soir
Demain
Après demain
Tard dans la nuit
Le jour
La nuit
Dehors
Dedans
Hier
Maintenant
Aurevoir
Aurevoir
Aujourd’hui
L’autre jour
La semaine
*****LES LIEUX
L’église
Le marché
L’école
Le village
Le village
Le champ
L’état
Sur
En bas
En haut
A gauche
A droite
A côté
Derrière
Devant
Là
Ici
Là bas
En Haut
En Haut
En Bas
En Bas
Notre pays
Le ciel
La terre
*****LES VERBES
Voir
Partir
Manger
Porter (habit, chaussures)
Porter (une charge)
Boire
Verser (Liquide/solide)
Verser (Liquide/solide)
Accrocher
Sécher
Ouvrir
Enlever
Prendre
Dormir
Ramasser
Pousser
Rentrer
Sauter
Courir
Faire
Avoir
Monter
Pleuvoir
Aimer
Aider
Regarder
Savoir
Compter
Acheter
Appeler
Casser (ce qui est cassable)
Casser (ce qui est cassable)
Perdre
Ecouter
Bavarder
Gâter
Mettre
Couper
Lire
Gagner
Voler (dans l’air)
Voler (quelque chose)
Chasser
Tremper
Charger
Vomir
Jouer
Oublier
Déchirer
Rêver
Entrer
Se rappeler
Parler
Nourrir
Ecrire
Arranger
Se lever
Glisser
Demander
Frotter
Repasser
Pleurer
Rire
Donner
Etre
Paraitre
Promener
Remplir
Apprendre
Tourner
Préparer
Piquer (injection)
Confondre
Réveiller
S’habiller
Montrer
Ecraser
Comprendre
Mentir
Sortir
Cultiver
Voyager
Aider
Dire
Sucré
Fermer
Emballer
Lécher
Ouvrir
Chercher
Pousser
Marcher
Mordre (piquer)
Imiter
Essayer
Brûler
Gifler quelqu’un
Attacher
Construire
Descendre
Descendre
Braiser
Brûler
Griller
Revenir
Tomber
Danser
Bouffer
Blesser
Casser
Grandir
Mordre
Allumer
Allumer
Eteindre
Vouloir
Chercher
Connaitre
Echanger
Calculer
Chanter
Ecouter
Diriger
Amener
Arroser
Balayer
*****LES PRONOMS
Je
Tu
Il
Nous
Vous
Ils
Mon
Ton
Son
Notre
Votre
Leur
Mes
Tes
Ses
Ses
Nos
Vos
Leurs
*****LES CONJONCTIONS
Mais
N’est ce pas ?
Trop
beaucoup
Qui
Sans
Quoi
Lui et moi
Quand ?
A quel moment ?
Comment ?
IL ne faut plus jamais…
Chez nous
Chez nous
A moi
Quelque chose
Lui seul
On
Où ?
Et
Donc
Personne
Car
Je ne vais plus jamais…
Avec
Dans
A lui
Comme
Encore
Rentre
*****LES CHIFFRES
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
1000
5 francs
2000
10 francs
3000
20 francs
4000
25 francs
5
30 francs
6
50
50 francs
7000
100 francs
8000
200 francs
9000
300 francs
10000
400 francs
1000000
500 francs
*****LES METIERS
Le cultivateur
Le docteur
L’élève
Le commerçant
Le Chef de l’état
Le danseur
Le tailleur
Le prêtre
Le maître
Policier
gendarme
militaire
Le Chef
Le notable
Le sous-chef
*****LES ADJECTIFS QUALIFICATIFS
Bon
Sale
Propre
Mauvais
faible
Fort
Grand
Petit
Mince
Gros
Vite
Vite
Sec
Mouillé
Méchant
Chiche
*****LES PARTIES DE LA MAISON
Le salon
La chambre
La cuisine
La douche
Le WC
Le magasin
*****LES VILLES
YAOUNDE
DOUALA
BAFOUSSAM
AKONOLINGA
BATIE
BAMENDJOUN
BADENKOP
BAHAM
BAFANG
MBOUDA
BATCHAM
BAPI
BALENG
BANDJOUN
BAMOUGOUM
NGAOUNDERE
NKONGSAMBA
BANDJA
BANGANGTE
FOUTOUNI
""".split('\n')

data = {}
title = 'delete_me'

for i in a:
    if '*****' in i:
        title = i.replace('*****', '').title()
        data[title] = []
    else:
        data[title].append(i.capitalize())


def exist(word):
    result = {}
    for lang in _dict_word:
        for word_id in _dict_word[lang]['lang']:
            if word.lower() == _dict_word[lang]['lang'][word_id].lower():
                if lang not in result:
                    result[lang] = []
                result[lang].append(word_id)
    return result


dict_word = {}
id_word_used = {}

for theme in data:
    for word in data[theme]:
        _ = exist(word)
        if _:
            for lang in _:
                if lang not in dict_word:
                    dict_word[lang] = {}
                if theme not in dict_word[lang]:
                    dict_word[lang][theme] = {}
                if 'lang' not in dict_word[lang][theme]:
                    dict_word[lang][theme]['lang'] = {}
                    dict_word[lang][theme]['mlang'] = {}
                for i in _[lang]:
                    if lang not in id_word_used:
                        id_word_used[lang] = []
                    id_word_used[lang].append(i)
                    dict_word[lang][theme]['lang'][i] = _dict_word[lang][
                        'lang'][i]
                    dict_word[lang][theme]['mlang'][i] = _dict_word[lang][
                        'mlang'][i]

for lang in _dict_word:
    for id_word in _dict_word[lang]['lang']:
        if lang in id_word_used:
            if id_word not in id_word_used[lang]:
                if 'Other theme' not in dict_word[lang]:
                    dict_word[lang]['Other theme'] = {'lang': {}, 'mlang': {}}
                dict_word[lang]['Other theme']['lang'][id_word] = _dict_word[
                    lang]['lang'][id_word]
                dict_word[lang]['Other theme']['mlang'][id_word] = _dict_word[
                    lang]['mlang'][id_word]

f = open('word.json', 'w')
json.dump(dict_word, f)
f.close()

f = open('word.py', 'w', encoding='utf-8')
f.write("""# -*- coding: utf-8 -*-
dict_word = %s
""" % str(dict_word))
f.close()
