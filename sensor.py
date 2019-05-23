def main():
    print("Sensor: Hides a word in a sentence using a character.")
    op = 1
    while(op==1):
        sentence = input("Enter the sentence: ")
        word = input("Enter the word to be hidden: ")
        ch = input("Enter the character to hide the word: ")
        if(ch == ''):
            sensor(sentence, word)
        else:
            sensor(sentence,word,ch)

        op = int(input("Choose an option:\n1)Run again\n2)Exit\n"))

    exit()

def sensor(st,word,ch='*'):
    saved = st.split(word)
    hide =[]
    for s in range(len(saved)):
        if(s == len(saved)-1):
            hide.append(saved[s])
        else:
            hide.append(saved[s]+(ch * len(word)))

    hidden = ''.join(hide)
    print('\n'+hidden+'\n')
    input("Press enter to continue")

if __name__ == '__main__':
    main()