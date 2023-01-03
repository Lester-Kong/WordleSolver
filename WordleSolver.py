possible_words = ["cigar","rebut","sissy","humph","awake","blush","focal","evade","naval","serve","heath","dwarf","model","karma","stink","grade","quiet","bench","abate","feign","major","death","fresh","crust","stool","colon","abase","marry","react","batty","pride","floss","helix","croak","staff","paper","unfed","whelp","trawl","outdo","adobe","crazy","sower","repay","digit","crate","cluck","spike","mimic","pound","maxim","linen","unmet","flesh","booby","forth","first","stand","belly","ivory","seedy","print","yearn","drain","bribe","stout","panel","crass","flume","offal","agree","error","swirl","argue","bleed","delta","flick","totem","wooer","front","shrub","parry","biome","lapel","start","greet","goner","golem","lusty","loopy","round","audit","lying","gamma","labor","islet","civic","forge","corny","moult","basic","salad","agate","spicy","spray","essay","fjord","spend","kebab","guild","aback","motor","alone","hatch","hyper","thumb","dowry","ought","belch","dutch","pilot","tweed","comet","jaunt","enema","steed","abyss","growl","fling","dozen","boozy","erode","world","gouge","click","briar","great","altar","pulpy","blurt","coast","duchy","groin","fixer","group","rogue","badly","smart","pithy","gaudy","chill","heron","vodka","finer","surer","radio","rouge","perch","retch","wrote","clock","tilde","store","prove","bring","solve","cheat","grime","exult","usher","epoch","triad"]

def wrongLetters(result, guess):
    wrong_letters = []
    for i in range(5):
        if result[i] == "w":
            wrong_letters.append(guess[i])
    return wrong_letters

def removeWord(possible_words, result, guess):
    wordsToRemove = []
    wrong_letters = wrongLetters(result, guess)
    for wrongletter in wrong_letters:
        for word in possible_words:
            if wrongletter in word and word not in wordsToRemove:
                wordsToRemove.append(word)
            
    for word in wordsToRemove:
        possible_words.remove(word)
        
    return possible_words

def letterFreq(possible_words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letterFreqArr = {}
    freq = [0,0,0,0,0]
    for letter in alphabet:
        for word in possible_words:
            for i in range(5):
                if word[i] == letter:
                    freq[i] += 1
        letterFreqArr.update({letter: freq})
    return arr

"""def wordleSolver(possible_words):
    print(wrongLetters("wwwww", "abcde"))"""

print(removeWord(possible_words, "wwwww", "cigar"))
