import nltk
import os
import sys
import traceback
from sol_frames import SolidityEngine as SE
import sol_frames as sf

LINKING_VERBS = ('be','was','is','are')


class NLParse(object):
    """
    This object tokenizes and returns document tokens and trees.
    """


    def __init__(self,file_name = None, text = None):
        if file_name == None:
            print "Please include a file name"

        self.solidity = SE()

        try:
            try:
                self.file_text = open(os.path.join(os.curdir,file_name), "r").read()
                self.doc_tokens = nltk.word_tokenize(self.file_text)
                self.tagged = nltk.pos_tag(self.doc_tokens)          
 
            except:
                self.file_text = text
                self.doc_tokens = nltk.word_tokenize(self.file_text)
                self.tagged = nltk.pos_tag(self.doc_tokens)


        except:
            print "There has been an Error: \n\n"
            traceback.print_exc()
            pass 

    def __str__(self):
        return self + self.self.tagged

    def buildTree(self):
       return nltk.chunk.ne_chunk(self.tagged)

    def drawTree(self):
        tree = self.buildTree()
        tree.draw()

    def getTags(self):
        return self.tagged

    def test(self):
        print self.buildTree()


    def identifyActionVerbs(self):
        """
        Returns a tuple with all non-linking verbs
        """

        verbs = []
        word_tree = self.buildTree()
        for word in word_tree:
           print "viewing %s" % str(word)

           if len(word) < 2:
               continue
           
           else:
               if word[1] == "VB":
                   verbs.append(word[0])


        verbs = tuple(verb for verb in set(verbs) if verb not in LINKING_VERBS)
        return verbs 

    
    def identifyNouns(self):
        nouns = []
        word_tree = self.buildTree()
        for word in word_tree:
           print "viewing %s" % str(word)

           if len(word) < 2:
               continue
           
           else:
               if word[1] == "NN" or "NNP":
                   nouns.append(word[0])


        nouns = tuple(noun for noun in set(nouns))   #For filtering
        return nouns 

    def returnSolidity(self,contract_name = "Test"):

        self.solidity.buildFunctions(self.identifyActionVerbs()) 
        self.solidity.buildStructs(self.identifyNouns())
        return self.solidity.returnFull(name = contract_name,
                                        struct_string = self.solidity.structs,
                                        func_string = self.solidity.functions)


