import numpy as np
import time
import pyttsx3
from helper import significati

if __name__ == "__main__":
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume',1.0) 
    engine.setProperty('voice', 'italian+f4')
    
    estrazioni = np.random.choice(a=np.arange(1,91), size=90, replace=False)
    
    warmup = [
        'Fate attenzione!',
    ]
    
    try:
        rnd_seed = input("Inserisci un numero intero per selezionare il seme:")
        np.random.seed(rnd_seed)
    except:
        np.random.seed(42)
    
    log = [] 
    n_chiama = 0
    check = ''
    while check != 'quit':
        n_estratto = estrazioni[n_chiama]
        motto = significati[n_estratto]
        log.append(n_estratto)
        stringa = 'CHIAMA {}\nNUMERO ESTRATTO {}\nMOTTO {}'.format(n_chiama+1,n_estratto,motto)
        print(stringa)
        print(log)

        #warmup_index = warmup_rnd[n_chiama]
        warmup_index = n_chiama%len(warmup)
        voce_warmup = warmup[warmup_index]

        engine.say(voce_warmup)
        engine.runAndWait()
        time.sleep(0.5)

        engine.say('NUMERO ESTRATTO')
        engine.runAndWait()
        time.sleep(0.1)

        engine.say(n_estratto)
        engine.runAndWait()
        time.sleep(0.5)

        engine.say('NUMERO ESTRATTO')
        engine.runAndWait()
        time.sleep(0.1)

        engine.say(n_estratto)
        engine.runAndWait()
        time.sleep(0.2)

        engine.say(motto.split('(')[0])
        engine.runAndWait()

        n_chiama += 1
        
        check = input("Premi per la prossima estrazione o inserisci \'quit\' per uscire:")
        
    print('La tombola e\' finita.')
