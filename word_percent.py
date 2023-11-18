class Project:

    def enter_word(self):
        word=input('enter the word: ')
        return word.lower()
    
    def char_counter(self,word):
        
        char=input('enter the wanted character: ')
        char=char.lower()
        if char in word:
            count=word.count(char)
        else:
            print('the character not found!') #pip install multipledispatch
        return count   

try:



 p=Project()


 word=p.enter_word()

 char_percent=(p.char_counter(word)/len(word))*100


 print(char_percent)
except UnboundLocalError:
    print('enter the character that exists in the given word!')
           


