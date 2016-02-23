#
# finalproject.py - Final Project
#
# Name: Sarah Larbi
# Email: slarbi@bu.edu
#
# Partner's Name: Sheryn Chung
# Partner's Email: sherync@bu.edu 
#
import math
def clean_text(txt):
    """takes a string of text txt as a parameter and returns a list containing the words in txt after it has been “cleaned”."""
    txt = str.lower(txt)
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('!', '')
    txt = txt.replace('?', '')
    txt = txt.replace('"', '')
    txt = txt.replace("'", '')  
    return txt.split()

def prefix(word):
    ''' helper funtion for stem'''
    
    if word[:5] == 'inter':
        word = word[5:]
    elif word[:5] == 'intra':
        word = word[5:]
    elif word[:5] == 'intro':
        word = word[5:]
    elif word[:2] == 'in':
        word = word[2:]
    elif word[:4] == 'hypo':
        word = word[4:]
    elif word[:5] == 'hyper':
        word = word[5:]
    elif word[:5] == 'extra':
        word = word[5:]
    elif word[:5] == 'extro':
        word = word[5:]
    elif word[:2] == 'ex':
        word = word[2:]
    elif word[:3] == 'dys':
        word = word[3:]
    elif word[:3] == 'dis':
        word = word[3:]
    elif word[:3] == 'dia':
        word = word[3:]
    elif word[:4] == 'demi':
        word = word[4:]
    elif word[:2] == 'de':
        word = word[2:]
    elif word[:6] == 'contra':
        word = word[6:]
    elif word[:6] == 'circum':
        word = word[6:]
    elif word[:2] == 'bi':
        word = word[2:]
    elif word[:4] == 'anti':
        word = word[4:]
    elif word[:3] == 'abs':
        word = word[3:]
    elif word[:3] == 'pre':
        word = word[3:]
    elif word[:2] == 'un':
        word = word[2:]
    elif word[:2] == 're':
        word = word[2:]
    elif word[:3] == 'non':
        word = word[3:]
    elif word[:3] == 'mis':
        word = word[3:]
    elif word[:3] == 'sub':
        word = word[3:]
    elif word[:5] == 'trans':
        word = word[5:]
    elif word[:4] == 'semi':
        word = word[4:]

    return word 

    
def suffix(word):
    ''' helper for stem'''
    
    if word[-3:] == 'ing':
        if len(word) > 4:
            if word[-4] == word[-5]:
                word = word[:-4]
            else:
                word = word[:-3]
    elif word[-3:] == 'ers':
        word = word[:-3]
    elif word[-2:] == 'er':
        word = word[:-3]
    elif word[-2:] == 'ed':
        word = word[:-3]
    elif word[-2:] == 'ly':
        word = word[:-3]
    elif word[-4:] == 'able':
        word = word[:-4]
    elif word[-3:] == 'ish':
        word = word[:-3]
    elif word[-3:] == 'ity':
        word = word[:-3]
    elif word[-4:] == 'less':
        word = word[:-4]
    elif word[-4:] == 'ness':
        word = word[:-4]
    elif word[-3:] == 'ous':
        word = word[:-3]
    elif word[-2:] == 'ty':
        word = word[:-2]
    elif word[-4:] == 'tion':
        word = word[:-4]
    elif word[-4:] == 'some':
        word = word[:-4]
    elif word[-7:] == 'ization':
        word = word[:-7]
    elif word[-4:] == 'tion':
        word = word[:-4]
    elif word[-5:] == 'ation':
        word = word[:-5]
    elif word[-4:] == 'ular':
        word = word[:-4]
    elif word[-3:] == 'ure':
        word = word[:-3]
    elif word[-4:] == 'sect':
        word = word[:-4]
    elif word[-4:] == 'sion':
        word = word[:-4]
    elif word[-4:] == 'ship':
        word = word[:-4]
    elif word[-6:] == 'scribe':
        word = word[:-6]
    elif word[-3:] == 'ory':
        word = word[:-3]
    elif word[-3:] == 'oid':
        word = word[:-3]
    elif word[-4:] == 'ment':
        word = word[:-4]
    elif word[-3:] == 'ive':
        word = word[:-3]
    elif word[-3:] == 'ite':
        word = word[:-3]
    elif word[-4:] == 'itis':
        word = word[:-4]
    elif word[-3:] == 'ism':
        word = word[:-3]
    elif word[-3:] == 'ist':
        word = word[:-3]
    elif word[-3:] == 'ful':
        word = word[:-3]
    elif word[-3:] == 'est':
        word = word[:-3]
    elif word[-5:] == 'esque':
        word = word[:-5]
    elif word[-4:] == 'ency':
        word = word[:-4]
    elif word[-2:] == 'ee':
        word = word[:-2]
    elif word[-2:] == 'dom':
        word = word[:-2]
    elif word[-4:] == 'cule':
        word = word[:-4]
    elif word[-3:] == 'ate':
        word = word[:-3]
    elif word[-5:] == 'ative':
        word = word[:-5]
    elif word[-4:] == 'ance':
        word = word[:-4]
    elif word[-3:] == 'ant':
        word = word[:-3]
    

    return word

def stem(word):
#suffix twice for cases such as 'cautiously'
   word = prefix(suffix(suffix(word)))
   return word


def compare_dictionaries(d1, d2):
        
    
    score = 0
    total = 0
    for key in source1.words:
        total += source1.words[key]
    

    print(total)

    if total == 0:
        return total
    for n in d2:
        if n in d1:
            score += math.log((d1[n])/total)
        else:
            score += math.log((.5/total))
    return score

class TextModel:
    """this is a textmodel class"""

        

    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name as a parameter """

        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stem = {}
        self.sentence_lengths = {}
        self.starter_count = {}


    def __str__(self):
        """returns a string that includes the name of the model as well as the sizes of the dictionaries for each feature of the text."""

        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of sentence_lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stem)) + '\n'
        s += '  number of sentence starters: ' + str(len(self.starter_count)) + '\n'
        return s

       
    def add_string(self, s):
        """adds a string of text s to the model by augmenting the feature dictionaries defined in the constructor. """
 
        words = s.split()
        
        current_num = 0
        for w in words:
            if w[-1] in '.!?':
                current_num += 1
                if current_num not in self.sentence_lengths:
                    self.sentence_lengths[current_num] = 1
                    current_num = 0
                elif current_num in self.sentence_lengths:
                    self.sentence_lengths[current_num] += 1
                    current_num = 0
                
            if w[-1] not in '.?!':
                current_num += 1
                
        for w in range(len(words) - 1):
            if words[w][-1] in '.?!':
                if words[w+1] not in self.starter_count:
                    if words[w+1][-1] in '!?,.":;)(][\/-_^%#<>$&*' or words[w+1][-1] == "'":
                        self.starter_count[(words[w+1][:-1])] = 1
                    else:
                        self.starter_count[(words[w+1])] = 1
                else:
                    if words[w+1][-1] in '!?,.":;)(][\/-_^%#<>$&*' or words[w+1][-1] == "'":
                        self.starter_count[(words[w+1][:-1])] += 1
                    else:
                        self.starter_count[(words[w+1])] += 1

            
        words = clean_text(s)

        for w in words:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

        for w in words:
            if len(w) not in self.word_lengths:
                self.word_lengths[(len(w))] = 1

            elif len(w) in self.word_lengths:
                self.word_lengths[(len(w))] += 1

        for w in words:
            if stem(w) not in self.stem:
                self.stem[stem(w)] = 1
            elif stem(w) in self.stem:
                self.stem[stem(w)] += 1
                

            
                    
                
# maybe wrong?
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model."""

        f = open(filename, 'r', encoding='utf8')

        self.add_string(str(filename))
        f.close()

    def save_model(self):
        """saves the TextModel object self by writing its various feature dictionaries to files."""
        filename = self.model_name + '_' + 'word_lengths'
        d = self.word_lengths
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

        filename = self.model_name + '_' + 'words'
        d = self.words
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

        filename = self.model_name + '_' + 'stem'
        d = self.stem
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

        filename = self.model_name + '_' + 'sentence_lengths'
        d = self.sentence_lengths
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

        filename = self.model_name + '_' + 'starter_count'
        d = self.starter_count
        f = open(filename, 'w')
        f.write(str(d))
        f.close()

    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from their files and assigns them to the attributes of the called TextModel. """
        
        filename = self.model_name + '_' + 'word_lengths'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.word_lengths = d
        
        
        filename = self.model_name + '_' + 'words'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.words = d

        filename = self.model_name + '_' + 'stem'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.stem = d

        filename = self.model_name + '_' + 'sentence_lengths'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.sentence_lengths = d

        filename = self.model_name + '_' + 'starter_count'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()
        d = dict(eval(d_str))
        self.starter_count = d
        

    def similarity_scores(self, other):

         word_score = compare_dictionaries(other.words, self.words)
         word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
         stem_score = compare_dictionaries(other.stem, self.stem)
         sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
         starter_count_score = compare_dictionaries(other.starter_count, self.starter_count)

         lst = [word_score, word_lengths_score, stem_score, sentence_lengths_score, starter_count_score]
         return lst
         print(lst)

    def classify(self, source1, source2):

        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))

        higher_scores_source1 = 0
        higher_scores_source2 = 0

        for x in scores1:
            for y in scores2:
                if x > y:
                    higher_scores_source1 += 1
                if x < y:
                    higher_scores_source2 += 1
                if x == y:
                    higher_scores_source2 += 1
                    higher_scores_source1 += 1

        if higher_scores_source1 > higher_scores_source2:
            print(self.model_name + ' is more likely to have come from ' + source1.model_name)
        else:
            print(self.model_name + ' is more likely to have come from ' + source2.model_name)



def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ your docstring goes here """
    source1 = TextModel("Grey's Anatomy")
    source1.add_file("Greys.txt")
    source1.add_file("Didn't We Almost Have It All.txt")
    source1.add_file('Losing My Religion.txt')
    source1.add_file("Who's Zoomin Who.txt")

   

    source2 = TextModel('Kimmy Schmidt')
    source2.add_file('The Unbreakable Kimmy Schmidt.txt')
    source2.add_file('Kimmy Has A Birthday.txt')
    source2.add_file('Kimmy Goes Outside.txt')



    new1 = TextModel('Kimmy Makes Waffles')
    new1.add_file('Kimmy Makes Waffles.txt')
    new1.classify(source1, source2)

    new2 = TextModel('Scandal')
    new2.add_file('Scandal.txt')
    new2.classify(source1, source2)

    new3 = TextModel("Grey's Two Text")
    new3.add_file('Greys2.txt')
    new3.classify(source1, source2)

    new4 = TextModel('30 Rock')
    new4.add_file('30rock.txt')
    new4.classify(source1, source2)

    

    # Add code for three other new models below.
