import jellyfish
from pyphonetics import Soundex, Metaphone
FILIPINO_ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','NG','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase = []
for i in FILIPINO_ALPHABETS:
    lowercase.append(i.lower())

#28x2
TOTAL_ALPHABETS = FILIPINO_ALPHABETS+lowercase

CONSONANTS = ['B','C','D','F','G','H','J','K','L','M','N','Ñ','NG','P','Q','R','S','T','V','W','X','Y','Z']
VOWELS = ['A','E','I','O','U']

CONSONANTS_1 = ['B','C','D','F','G','H','J','K','L','M','N']
CONSONANTS_2 = ['Ñ','NG','P','Q','R','S','T','V','W','X','Y','Z']

CONSONANTS_EZ = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']



def word_to_letter(answer, result):
    if answer.lower() == result.lower():
        return True
    elif answer.lower() == "b" and result.lower() == "bee":
        return True
    elif answer.lower() == "c" and result.lower() == "see":
        return True
    elif answer.lower() == "c" and result.lower() == "sea":
        return True
    elif answer.lower() == "d" and result.lower() == "dee":
        return True
    elif answer.lower() == "d" and result.lower() == "day":
        return True
    elif answer.lower() == "f" and result.lower() == "if":
        return True
    elif answer.lower() == "f" and result.lower() == "ef":
        return True
    elif answer.lower() == "g" and result.lower() == "jee":
        return True
    elif answer.lower() == "h" and result.lower() == "each":
        return True
    elif answer.lower() == "h" and result.lower() == "itch":
        return True
    elif answer.lower() == "i" and result.lower() == "eye":
        return True
    elif answer.lower() == "j" and result.lower() == "jay":
        return True
    elif answer.lower() == "k" and result.lower() == "kay":
        return True
    elif answer.lower() == "k" and result.lower() == "gay":
        return True
    elif answer.lower() == "l" and result.lower() == "el":
        return True
    elif answer.lower() == "m" and result.lower() == "im":
        return True
    elif answer.lower() == "n" and result.lower() == "in":
        return True
    elif answer.lower() == "ñ" and result.lower() == "enye":
        return True
    elif answer.lower() == "ng" and result.lower() == "angie":
        return True
    elif answer.lower() == "ng" and result.lower() == "engine":
        return True
    elif answer.lower() == "ng" and result.lower() == "n g":
        return True
    elif answer.lower() == "o" and result.lower() == "ow":
        return True
    elif answer.lower() == "p" and result.lower() == "fee":
        return True
    elif answer.lower() == "q" and result.lower() == "cue":
        return True
    elif answer.lower() == "r" and result.lower() == "are":
        return True
    elif answer.lower() == "s" and result.lower() == "is":
        return True
    elif answer.lower() == "s" and result.lower() == "ss":
        return True
    elif answer.lower() == "t" and result.lower() == "tea":
        return True
    elif answer.lower() == "u" and result.lower() == "you":
        return True
    elif answer.lower() == "v" and result.lower() == "vee":
        return True
    elif answer.lower() == "v" and result.lower() == "bee":
        return True
    elif answer.lower() == "w" and result.lower() == "double you":
        return True
    elif answer.lower() == "w" and result.lower() == "double u":
        return True
    elif answer.lower() == "x" and result.lower() == "ex":
        return True
    elif answer.lower() == "y" and result.lower() == "why":
        return True
    elif answer.lower() == "z" and result.lower() == "zee":
        return True

def word_to_phonetics(answer, result):
    if answer.lower() == result.lower():
        if answer.upper() in VOWELS:
            return True
    elif answer.lower() == "a" and result.lower() == "ah":
        return True
    elif answer.lower() == "a" and result.lower() == "aa":
        return True
    elif answer.lower() == "b" and result.lower() == "ba":
        return True
    elif answer.lower() == "c" and result.lower() == "ca":
        return True
    elif answer.lower() == "c" and result.lower() == "ka":
        return True
    elif answer.lower() == "d" and result.lower() == "da":
        return True
    elif answer.lower() == "d" and result.lower() == "the":
        return True
    elif answer.lower() == "e" and result.lower() == "eh":
        return True
    elif answer.lower() == "f" and result.lower() == "fa":
        return True
    elif answer.lower() == "g" and result.lower() == "ga":
        return True
    elif answer.lower() == "g" and result.lower() == "go":
        return True
    elif answer.lower() == "h" and result.lower() == "ho":
        return True
    elif answer.lower() == "h" and result.lower() == "ha":
        return True
    elif answer.lower() == "i" and result.lower() == "ee":
        return True
    elif answer.lower() == "i" and result.lower() == "e":
        return True
    elif answer.lower() == "j" and result.lower() == "ja":
        return True
    elif answer.lower() == "k" and result.lower() == "ka":
        return True
    elif answer.lower() == "k" and result.lower() == "ca":
        return True
    elif answer.lower() == "k" and result.lower() == "co":
        return True
    elif answer.lower() == "k" and result.lower() == "ko":
        return True
    elif answer.lower() == "l" and result.lower() == "la":
        return True
    elif answer.lower() == "m" and result.lower() == "mm":
        return True
    elif answer.lower() == "m" and result.lower() == "ma":
        return True
    elif answer.lower() == "n" and result.lower() == "na":
        return True
    elif answer.lower() == "n" and result.lower() == "nah":
        return True
    elif answer.lower() == "n" and result.lower() == "nn":
        return True
    elif answer.lower() == "p" and result.lower() == "po":
        return True
    elif answer.lower() == "p" and result.lower() == "pa":
        return True
    elif answer.lower() == "q" and result.lower() == "kwa":
        return True
    elif answer.lower() == "q" and result.lower() == "kya":
        return True
    elif answer.lower() == "r" and result.lower() == "ra":
        return True
    elif answer.lower() == "r" and result.lower() == "rah":
        return True
    elif answer.lower() == "s" and result.lower() == "sa":
        return True
    elif answer.lower() == "s" and result.lower() == "sah":
        return True
    elif answer.lower() == "t" and result.lower() == "ta":
        return True
    elif answer.lower() == "t" and result.lower() == "tah":
        return True
    elif answer.lower() == "u" and result.lower() == "oo":
        return True
    elif answer.lower() == "u" and result.lower() == "ooh":
        return True
    elif answer.lower() == "v" and result.lower() == "va":
        return True
    elif answer.lower() == "w" and result.lower() == "wa":
        return True
    elif answer.lower() == "x" and result.lower() == "xa":
        return True
    elif answer.lower() == "y" and result.lower() == "ya":
        return True
    elif answer.lower() == "z" and result.lower() == "za":
        return True

def understand_tlw(answer, result):
    try1 = Metaphone().sounds_like(answer, result)
    try2 = Soundex().sounds_like(answer, result)
    try3 = jellyfish.jaro_similarity(answer, result)
    
    if try1:
        return [try1, 'try1']
    elif try2:
        return [try2, 'try2']
    elif try3:
        return [try3, 'try3']

     


CVCA = [
    'cab', 'dab', 'gab', 'jab', 'lab', 'nab', 'tab', 'blab', 'crab', 'grab', 'scab', 'stab', 'slab','bat', 'cat', 'fat', 'hat', 'mat', 'pat', 'rat', 'sat', 'vat', 'brat', 'chat', 'flat', 'gnat', 'spat',
    'bad', 'dad', 'had', 'lad', 'mad', 'pad', 'sad', 'tad', 'glad', 'ban', 'can', 'fan', 'man', 'pan', 'ran', 'tan', 'van', 'clan', 'plan', 'scan', 'than', 'bag', 'gag', 'hag', 'lag', 'nag', 'rag', 'sag', 'tag', 'wag', 'brag', 'drag', 'flag', 'snag', 'stag',
    'cap', 'gap', 'lap', 'map', 'nap', 'rap', 'sap', 'tap', 'yap', 'zap', 'chap', 'clap', 'flap', 'slap', 'snap', 'trap','bam', 'dam', 'ham', 'jam', 'ram', 'yam', 'clam', 'cram', 'scam', 'slam', 'spam', 'swam', 'tram', 'wham',
    'back', 'hack', 'jack', 'lack', 'pack', 'rack', 'sack', 'tack', 'black', 'crack', 'shack', 'snack', 'stack', 'quack', 'track',
    'bash', 'cash', 'dash', 'gash', 'hash', 'lash', 'mash', 'rash', 'sash', 'clash', 'crash', 'flash', 'slash', 'smash', 'gal', 'pal', 'gas', 'yak', 'wax', 'tax', 'bath', 'math'
]

CVCE = [
    'bed', 'fed', 'led', 'red', 'wed', 'bled', 'bred', 'fled', 'pled', 'sled', 'shed','beg', 'keg', 'leg', 'peg','bet', 'get', 'jet', 'let', 'met', 'net', 'pet', 'set', 'vet', 'wet', 'yet', 'fret',
    'den', 'hen', 'men', 'pen', 'ten', 'then', 'when', 'beck', 'deck', 'neck', 'peck', 'check', 'fleck', 'speck', 'wreck','bell', 'cell', 'dell', 'jell', 'sell', 'tell', 'well', 'yell', 'dwell', 'shell', 'smell', 'spell', 'swell',
    'yes', 'web', 'gem', 'hem', 'pep', 'step'
]

CVCI = [
    'bit', 'fit', 'hit', 'kit', 'lit', 'pit', 'sit', 'wit', 'knit', 'quit', 'slit', 'spit', 'bid', 'did', 'hid', 'kid', 'lid', 'rid', 'skid', 'slid',
    'big', 'dig', 'fig', 'gig', 'jig', 'pig', 'rig', 'wig', 'zig', 'twig','dim', 'him', 'rim', 'brim', 'grim', 'skim', 'slim', 'swim', 'trim', 'whim',
    'dip', 'hip', 'lip', 'nip', 'rip', 'sip', 'tip', 'zip', 'chip', 'clip', 'drip', 'flip', 'grip', 'ship', 'skip', 'slip', 'snip', 'trip', 'whip',
    'kick', 'lick', 'nick', 'pick', 'sick', 'tick', 'wick', 'brick', 'chick', 'click', 'flick', 'quick', 'slick', 'stick', 'thick', 'trick',
    'fish', 'dish', 'wish', 'swish', 'bin', 'din', 'fin', 'pin', 'sin', 'tin', 'win', 'chin', 'grin', 'shin', 'skin', 'spin', 'thin', 'twin',
    'him', 'this', 'mix', 'six', 'fix', 'crib'
]

CVCO = [
    'cot', 'dot', 'got', 'hot', 'jot', 'lot', 'not', 'pot', 'rot', 'tot', 'blot', 'knot', 'plot', 'shot', 'slot', 'spot',
    'cob', 'gob', 'job', 'lob', 'mob', 'rob', 'sob', 'blob', 'glob', 'knob', 'slob', 'snob','bog', 'cog', 'dog', 'fog', 
    'hog', 'jog', 'log', 'blog', 'clog', 'frog', 'cop', 'hop', 'mop', 'pop', 'top', 'chop', 'crop', 'drop', 'flop', 'glop',
    'plop', 'shop', 'slop', 'stop','dock', 'lock', 'rock', 'sock', 'tock', 'block','clock', 'flock', 'rock', 'shock',
    'smock', 'stock','box', 'fox', 'pox', 'rod', 'sod', 'mom'
]

CVCU = [
    'but', 'cut', 'gut', 'hut', 'jut', 'nut', 'rut', 'shut','cub', 'hub', 'nub', 'rub', 'sub', 'tub', 'grub', 'snub', 'stub',
    'bug', 'dug', 'hug', 'jug', 'lug', 'mug', 'pug', 'rug', 'tug', 'drug', 'plug', 'slug', 'snug','bum', 'gum', 'hum', 'mum',
    'sum', 'chum', 'drum', 'glum', 'plum', 'scum', 'slum','bun', 'fun', 'gun', 'nun', 'pun', 'run', 'sun', 'spun', 'stun','bud',
    'cud', 'dud', 'mud', 'spud', 'stud', 'thud','buck', 'duck', 'luck', 'muck', 'puck', 'suck', 'tuck', 'yuck', 'chuck',
    'cluck', 'pluck', 'stuck', 'truck','gush', 'hush', 'lush', 'mush', 'rush', 'blush', 'brush', 'crush', 'flush', 'slush','pup', 'cup', 'bus'
]

CVC_QUIZ = [
    'cab', 'dab', 'gab', 'jab', 'lab', 'nab', 'tab','can', 'fan', 'man',
    'bed', 'fed', 'led', 'red', 'wed', 'yes', 'web', 'gem', 'hem', 'pep',
    'bit', 'fit', 'hit', 'kit', 'lit', 'pit', 'sit', 'wit', 'pin', 'sin',
    'dot', 'got', 'hot', 'dog', 'lot', 'not', 'mop', 'pop', 'top', 'box',
    'but', 'cut', 'gut', 'hut', 'mud', 'bum', 'gum', 'hum', 'fun', 'gun',
]

AKES = [
    'm', 'l', 's', 'b'
]

CVC2_QUIZ = [
    'rake', 'tame', 'gale', 'fade', 'hate', 'maze', 'came', 'vale', 'yale', 'gate'
]

DIPTHONGS = ['aw', 'au', 'oy', 'ui', 'ow', 'ou']
DIPTHONGS_EX = ['raw', 'law', 'saw', 'cause', 'haul', 'toy', 'boy', 'coy', 'coin', 'noise', 'oil', 'cow', 'now', 'mower', 'loud', 'house']

DIGRAPHS = ['ch', 'ck', 'ph', 'sh', 'th', 'wh', 'kn', 'wr']
DIGRAPHS_EX = ['child', 'rich', 'luck', 'knife', 'phone', 'ship', 'flash', 'mesh', 'three', 'bath', 'whale', 'why', 'wreck']

CONSONANTBLENDS = ['bl', 'cr', 'dr', 'fl', 'fr', 'gr', 'pl', 'pr', 'qu', 'sk', 'sl', 'sn', 'sp', 'st', 'sw']
CONSONANTBLENDS_EX = ['blend', 'desk', 'drive', 'blow', 'blue', 'gray', 'grow', 'cry', 'from', 'small', 'flow']

DIP_DIG_CON_QUIZ = [
    'coil', 'soil', 'out', 'own', 'bound', 'author', 'lair', 'pier', 'cloud', 'flaw', 
    'wrench', 'thread', 'braid', 'show', 'check', 'knot', 'fetch', 'what', 'ghost', 'whack',
    'block', 'crest', 'casket', 'slow', 'flask', 'down', 'frown', 'creek', 'free', 'film'
    ]