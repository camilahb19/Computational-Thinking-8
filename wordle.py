import random

# Pick a word at random
word_list = ["heart","loopy","audio","laugh","trial","chain","train","drain","crane","plane","ABACK","ABASE","ABATE","ABBEY","ABBOT","ABHOR","ABIDE","ABODE","ABORT","ABOUT","ABOVE","ABUSE","ABYSS","ACORN","ACRID","ACTOR","ACUTE","ADAGE","ADAPT","ADEPT","ADMIN","ADMIT","ADOBE","ADOPT","ADORE","ADORN","ADULT","AFFIX","AFIRE","AFOOT","AFOUL","AFTER","AGAIN","AGAPE","AGATE","AGENT","AGILE","AGING","AGLOW","AGONY","AGORA","AGREE","AHEAD","AIDER","AISLE","ALARM","ALBUM","ALERT","ALGAE","ALIBI","ALIEN","ALIGN","ALIKE","ALIVE","ALLAY","ALLEY","ALLOT","ALLOW","ALLOY","ALOFT","ALOHA","ALONE","ALONG","ALOOF","ALOUD","ALPHA","ALTAR","ALTER","AMASS","AMAZE","AMBER","AMBLE","AMEND","AMISS","AMITY","AMONG","AMPLE","AMPLY","AMUSE","ANGEL","ANGER","ANGLE","ANGRY","ANGST","ANIME","ANKLE","ANNEX","ANNOY","ANNUL","ANODE","ANTIC","ANVIL","AORTA","APART","APHID","APING","APNEA","APPLE","APPLY","APRON","APTLY","ARBOR","ARDOR","ARENA","ARGUE","ARISE","ARMOR","AROMA","AROSE","ARRAY","ARROW","ARSON","ARTSY","ASCOT","ASHEN","ASIDE","ASKEW","ASPIC","ASSAY","ASSET","ASTER","ATOLL","ATONE","ATTIC","AUDIO","AUDIT","AUGUR","AUNTY","AVAIL","AVERT","AVIAN","AVOID","AWAIT","AWAKE","AWARD","AWARE","AWASH","AWFUL","AWOKE","AXIAL","AXIOM","AZURE","BACON","BADGE","BADLY","BAGEL","BAGGY","BAKER","BALER","BALMY","BALSA","BANAL","BANJO","BARGE","BARON","BASAL","BASIC","BASIL","BASIN","BASIS","BASTE","BATCH","BATHE","BATON","BATTY","BAWDY","BAYOU","BEACH","BEADY","BEARD","BEAST","BEAUT","BEECH","BEEFY","BEFIT","BEGAN","BEGAT","BEGET","BEGIN","BEGUN","BEIGE","BEING","BELCH","BELIE","BELLE","BELLY","BELOW","BENCH","BERET","BERRY","BERTH","BESET","BETEL","BEVEL","BEZEL","BIBLE","BICEP","BIDDY","BIGOT","BILGE","BILLY","BINGE","BINGO","BIOME","BIRCH","BIRTH","BISON","BITTY","BLACK","BLADE","BLAME","BLAND","BLANK","BLARE","BLAST","BLAZE","BLEAK","BLEAT","BLEED","BLEEP","BLEND","BLESS","BLIMP","BLIND","BLINK","BLISS","BLITZ","BLOAT","BLOCK","BLOKE","BLOND","BLOOD","BLOOM","BLOWN","BLUER","BLUFF","BLUNT","BLURB","BLURT","BLUSH","BOARD","BOAST","BOBBY","BONEY","BONGO","BONUS","BOOBY","BOOST","BOOTH","BOOTY","BOOZE","BOOZY","BORAX","BORNE","BOSOM","BOSSY","BOTCH","BOUGH","BOULE","BOUND","BOWEL","BOXER","BRACE","BRAID","BRAIN","BRAKE","BRAND","BRASH","BRASS","BRAVE","BRAVO","BRAWL","BRAWN","BREAD","BREAK","BREED","BRIAR","BRIBE","BRICK","BRIDE","BRIEF","BRINE","BRING","BRINK","BRINY","BRISK","BROAD","BROIL","BROKE","BROOD","BROOK","BROOM","BROTH","BROWN","BRUNT","BRUSH","BRUTE","BUDDY","BUDGE","BUGGY","BUGLE","BUILD","BUILT","BULGE","BULKY","BULLY","BUMPY","BUNCH","BUNNY","BURLY","BURNT","BURST","BUSED","BUSHY","BUTCH","BUTTE","BUXOM","BUYER","BYLAW","CABAL","CABBY","CABIN","CABLE","CACAO","CACHE","CACTI","CADDY","CADET","CAGEY","CAIRN","CAMEL","CAMEO","CANAL","CANDY","CANNY","CANOE","CANON","CAPER","CAPON","CAPUT","CARAT","CARGO","CAROL","CAROM","CARRY","CARVE","CASTE","CATCH","CATER","CATTY","CAULK","CAUSE","CAVIL","CEASE","CEDAR","CELLO","CHAFE","CHAFF","CHAIN","CHAIR","CHALK","CHAMP","CHANT","CHAOS","CHARD","CHARM","CHART","CHASE","CHASM","CHEAP","CHEAT","CHECK","CHEEK","CHEER","CHESS","CHEST","CHICK","CHIDE","CHIEF","CHILD","CHILI","CHILL","CHIME","CHINA","CHIRP","CHOCK","CHOIR","CHOKE","CHORD","CHORE","CHOSE","CHUCK","CHUMP","CHUNK","CHURN","CHUTE","CIDER","CIGAR","CINCH","CIRCA","CIVIC","CIVIL","CLACK","CLAIM","CLAMP","CLANG","CLANK","CLASH","CLASP","CLASS","CLEAN","CLEAR","CLEAT","CLEFT","CLERK","CLICK","CLIFF","CLIMB","CLING","CLINK","CLOAK","CLOCK","CLONE","CLOSE","CLOTH","CLOUD","CLOUT","CLOVE","CLOWN","CLUCK","CLUED","CLUMP","CLUNG","CLUNK","COACH","COAST","COBRA","COCOA","COLON","COLOR","COMET","COMFY","COMIC","COMMA","CONCH","CONDO","CONIC","COPSE","CORAL","CORER","CORNY","COUCH","COUGH","COULD","COUNT","COUPE","COURT","COVEN","COVER","COVET","COVEY","COWER","COYLY","CRACK","CRAFT","CRAMP","CRANE","CRANK","CRASH","CRASS","CRATE","CRAVE","CRAWL","CRAZE","CRAZY","CREAK","CREAM","CREDO","CREED","CREEK","CREEP","CREME","CREPE","CREPT","CRESS","CREST","CRICK","CRIED","CRIER","CRIME","CRIMP","CRISP","CROAK","CROCK","CRONE","CRONY","CROOK","CROSS",]

hidden_word = random.choice(word_list)

# Guess a word
guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")

guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")
guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")
guess_word = input("ENTER A WORD: ")
output = ""
if len(guess_word) != 5:
    print("Enter a word that is 5 letters")
    guess_word = input("ENTER A WORD: ")
    output = ""
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# Result
print(f"Result: {output}")
if output == "🟩🟩🟩🟩🟩":
    print("You win")
else: 
    print("You lose")