# Step 1: Pre-process text to create a dictionary


punctuation = ['!', '"', '#', '$', '%', '&', '(', ')',\
               '*', '+', ',', '.', '/', ':', ';', '<', \
               '=', '>', '?', '@', '[', '\\', ']', '^', '_', \
               '`', '{', '|', '}', '~']
               
#further improvement - read text from file

fr = ''' 
OU EST JEAN? Jean et Marie sont dans le jardin. Il fait beau aujourd'hui, 
il fait très chaud. Mais hier, il faisait très froid ! Ils n'ont pas pu jouer dehors.
Jean et Marie adorent jouer, ils jouent toujours ensemble dans le jardin devant la grande
maison. Jean est un petit garçon et il a six ans. La petite fille est sa sœur, elle a cinq
ans. Jean a un petit chien, le chien est aussi dans le jardin en ce moment. Le chien aime
jouer avec les deux enfants. Le chien est très content à présent. Est-ce que Marie a aussi
un chien ? Non, Marie n'a pas de chien, elle a un chat. Mais le chat est dans la maison, 
le chat dort. Leur mère est dans la maison avec le chat, elle regarde par la fenêtre et
voit Jean et Marie qui jouent. Jean court vite vers le gros arbre vert, il se cache de
Marie. Savez-vous pourquoi ? Marie est assise et a les mains devant ses yeux. Elle ne peut
rien voir et elle compte. Pourquoi fait-elle cela ? Et que fait Jean près de l'arbre ? 
C'est un jeu. Lorsque Marie a fini de compter, elle regarde autour d'elle. Elle cherche
Jean : où est-il allé ? Le voyez-vous ? Marie ne sait pas où est Jean. Elle demande au
chien :"As-tu vu Jean ?" Mais le chien ne peut pas parler, bien sûr ! Alors Marie
n'obtient aucune réponse à sa question. Les gens n'obtiennent jamais de réponse
lorsqu'ils parlent aux chiens ! Marie regarde sa mère derrière la fenêtre, sa mère rit.
Marie pense qu'elle a vu où Jean est allé : "Dis-moi où il est !", dit-elle à sa mère.
"Non, Marie, je ne peux pas te le dire", répond-elle. Bien qu'elle sache probablement où
il est, elle ne veut pas le dire. Marie marche lentement à travers le jardin. Elle cherche
toujours à trouver Jean. Elle regarde sous la table et sous les chaises, mais Jean
n'y est pas. Elle regarde partout mais elle ne peut pas trouver Jean. Elle entend alors un
bruit, il vient de derrière le gros arbre vert. Est-ce que c'est Jean ? Encore ce bruit !
Elle écoute attentivement. Ce n'est pas un oiseau ou un autre animal. Elle l'entend bien
maintenant. Ce doit être Jean !Elle voit alors une petite main et lorsqu'elle s'approche,
elle voit aussi sa tête ! Elle rit et dit : "Je t'ai trouvé !" Ils sont contents,
tous les deux, et ils rentrent à la maison, il est l'heure de manger quelque chose et de
boire de l'eau !
''' 

fr=fr.lower() # make lowercase
fr = fr.split() 
fr = [''.join(x for x in par if x not in punctuation) for par in fr]
fr = set(fr) #choose unique element
fr = list(fr) #make it a list again
fr.sort() #alph order


# Step 2: Create a fra-cos word-to-word dictionary out of source text

fra_cos = { 
       'a':'hà', 'adorent':'amanu','aime':'amu', 
       'allé':'andatu', 'alors':'tandu', 'animal':'animale', 'ans':'anni',
       'arbre':'albero', 'as-tu':'hai', 'assise':'basatu', # check 'as-tu'
       'attentivement':'attentamenti', 
       'au':'a', 'aucune':'micca', "aujourd'hui":'oghje', 'aussi':'dinù',
       'autour':'attornu', 'autre':'altru', 'aux':'ad', 'avec':'cù', # fix 'aux', "avec"
       'beau':'bellu', 'bien sûr':'certu',  #'bien sur' should be considered as unseparable bigram
       'bien':'bè', 'boire':'beie', 'bruit':'sonu', 
       "c'est":'hè', 'se cache':'si piatta', 'ce':'stu', 'cela':'questu',
       'chaises':'sedie', 'chat':'gattu', 'chaud':'caud', 'cherche':'cerca', 
       'chien':'ghjacaru', 'chiens':'ghjacari', 'chose':'cosa', 'cinq':'cinqui',
       'compte':'conta', 'compter':'cuntà', 'content':'felice', 'contents':'felici',
       'court':'corre', "d'elle":'à ella', 'dans':'in', 'de':'à', # de = ['a','di']; 'court'
       'dehors':'','demande':'dumanda', 'derrière':'dietro a', 'deux':'duie',
       'devant':'davanti', 'dire':'dì', 'dis-moi':'', 'dit':'dici',
       'dit-elle':'dici', 'doit':'deve', 'dort':'dormi', 'elle':'ella',
       'en':'in', 'encore':'ancu', 'enfants':'zitelli', 'ensemble':'nsemmula',
       'entend':'senti', 'est':'hè', 'est-ce':'', 'est-il':'hà',
       'et':'e', 'il faisait':'facia', 'fait':'faci', 'fait-elle':'faci',
       'fenêtre':'finestra', 'fille':'figghjola', 'fini':'finitu', 'froid':'freddo',
       'garçon':'zitellu', 'les gens':'u pòpulu', 'grande':'grande', 'gros':'grande',
       'hier':'eri', 'il':'ellu', 'ils':'', 'jamais':'eternu',
       'jardin':"'ortu", 'je ne peux pas':"Ùn pò micca", 'Jean':'Jean', 'jeu':'ghjocu',
       'ils jouent':'ghjocani', 'jouer':'ghjucà', "l'arbre":"l'arvulu", "l'eau":'acqua',
       "l'entend":'senti à ellu', "l'heure":'tempu', 'la':'a', 'le':'u',
       'lentement':'lentamente', 'les':'i', 'leur':'li', "lorsqu'elle":'quandu',
       "lorsqu'ils":'quandu', 'lorsque':"quandu", 'main':'manu', 'mains':'mani',
       'maintenant':'avà', 'mais':'ma', 'maison':'casa', 'manger':'manghjà',
       'marche':'viaghja', 'Marie':'Marie', 'moment':'momentu', 'mère':'mamma',
       "n'a pas":'ùn hà micca', "n'est pas":'ùn hè micca', "n'obtiennent":'un capiscini micca',
       "n'obtient":'un capisci micca',"n'ont pas pu":'un pudutu micca', "n'y est pas":'ùn hè micca',
       'non':'ùn', 'oiseau':'acellu','ou':'o', 'où':'induva',
       'par':'attraversu', 'ils parlent':'parlani', 'parler':'parlà',
       'partout':'ignilocu', 'pas':'micca', 'pense':'pensa', 'petit':'picculu',
       'petite':'piccola','ne peut':'ùn pò', 'peux':'possu', 'pourquoi':'perchè',
       'probablement':'prubbabbirmenti', 'près de':'vicinu', 'présent':'prisente',
       "qu'elle":'chì ella', 'que':'chì', 'quelque':'qualchi', 'question':'domanda',
       'qui':'quale', 'regarde':'guarda', 'ils rentrent':'tornani', 'rien':'macca', 'rit':'rida',
       'répond-elle':'rispondi', 'réponse':'risposta', "s'approche":'si avvicina',
       'sa':'so', 'à sa':'a so', 'sache':'cunnosce', 'sait':'sà', 'savez-vous':'sapeti',
       'ses':'i so', 'six':'sei', 'sont':'sò', 'sous':'sottu ',
       'sœur':'surella', "t'ai":'', 'table':'tavula', 'te':'ti', 'toujours':'sempre',
       'tous':'tuttu', 'à travers':'attraverso', 'trouver':'truvà', 'trouvé':'trovu',
       'très':'assai', 'tête':'testa', 'un':'un', 'une':'una', 'vers':'à', #vers = ??
       'vert':'verde', 'veut':'voli', 'vient':'veni', 'vite':'subitu',
       'voir':'veda', 'voit':'vedi', 'le voyez-vous':'lu viditi?', 'vu':'vistu',
       'yeux':'occhi', 'écoute':'ascolta', 'être':'esse'
       } 
 
 
cos_fra = {y:x for x,y in fra_cos.items()} # a cos-fra dictionary (reversed)

result = [] #make a new empty list to store the result later

### further ideas - rewrite using HFST as dict structure is not efficient enough

# Step 3: create a translation function

def translate(direction):
    said = input('insert here a phrase from text "OU EST JEAN?": ') # here is the input
    said = said.split() # naive tokenisation
    for s in said:
        if s in direction: # check if the words are in dict
            values = direction[s] # get values from keys, they are the target-lang words
            res = result.append(values)
            res = str(res)
    return (result)
    print(res)
    
# Step 4: Run

translate(fra_cos) 
