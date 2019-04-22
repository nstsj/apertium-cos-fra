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

fra_cos = { '':'','a':'hà', 'adorent':'amanu','aime':'amu', #'aime': amu/ama
       'allé':'andatu', 'alors':'tandu', 'animal':'animale', 'ans':'anni',
       'arbre':'albero', 'as-tu':'hai', 'assise':'basatu', # check 'as-tu'
       'attentivement':'attentamenti', 
       'au':'a', 'aucune':'micca', "aujourd'hui":'oghje', 'aussi':'dinù',
       'autour':'attornu', 'autre':'altru', 'aux':'ad', 'avec':'cù', # fix 'aux', "avec"
       'beau':'bellu', 'bien sûr':'certu',  #'bien sur' should be considered as unseparable bigram
       'bien':'bè', 'boire':'beie', 'bruit':'sonu', 
       "c'est":'hè', 'cache':'', 'ce':'stu', 'cela':'questu', #cache (well, the whole line)
       'chaises':'sedie', 'chat':'gattu', 'chaud':'caud', 'cherche':'cerca', 
       'chien':'ghjacaru', 'chiens':'ghjacari', 'chose':'cosa', 'cinq':'cinqui',
       'compte':'conta', 'compter':'cuntà', 'content':'felice', 'contents':'felici',
       'court':'corre', "d'elle":'à ella', 'dans':'in', 'de':'à', # de = ['a','di']; 'court'
       'dehors':'', 'demande', 'derrière', 'deux',
       'devant', 'dire', 'dis-moi', 'dit',
       'dit-elle', 'doit', 'dort', 'elle',
       'en', 'encore', 'enfants', 'ensemble',
       'entend', 'est', 'est-ce', 'est-il',
       'et', 'faisait', 'fait', 'fait-elle',
       'fenêtre', 'fille', 'fini', 'froid',
       'garçon', 'gens', 'grande', 'gros',
       'hier', 'il', 'ils', 'jamais',
       'jardin', 'je', 'jean', 'jeu',
       'jouent', 'jouer', "l'arbre", "l'eau",
       "l'entend", "l'heure", 'la', 'le',
       'lentement', 'les', 'leur', "lorsqu'elle",
       "lorsqu'ils", 'lorsque', 'main', 'mains',
       'maintenant', 'mais', 'maison', 'manger',
       'marche', 'marie', 'moment', 'mère',
       "n'a", "n'est", "n'obtiennent", "n'obtient",
       "n'ont", "n'y", 'ne', 'non', 'oiseau',
       'ou', 'où', 'par', 'parlent', 'parler',
       'partout', 'pas', 'pense', 'petit',
       'petite','peut', 'peux', 'pourquoi',
       'probablement', 'près', 'présent', 'pu',
       "qu'elle", 'que', 'quelque', 'question',
       'qui', 'regarde', 'rentrent', 'rien', 'rit',
       'répond-elle', 'réponse', "s'approche",
       'sa', 'sache', 'sait', 'savez-vous', 'se',
       'ses', 'six', 'sont', 'sous', 'sûr',
       'sœur', "t'ai", 'table', 'te', 'toujours',
       'tous', 'travers', 'trouver', 'trouvé',
       'très', 'tête', 'un', 'une', 'vers',
       'vert', 'veut', 'vient', 'vite',
       'voir', 'voit', 'voyez-vous', 'vu',
       'yeux', 'à', 'écoute', 'être'
       }  
 # dictionary is to be finished 
 
 
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
    res = result.append(values) # !! smth went wrong here 
    return (result)
    print(res)
    
# Step 4: Run

translate(fra_cos) 
