# kaasspel (leerpad-01 werken met condities)

import time

print('Ik ga raden wat jouw favoriete kaas is.')
time.sleep(1)
print('')

print("Beantwoord de vragen hieronder")

geel = {'y':True,'n':False}.get(input("Is de kaas geel? Y/N: ").lower())
gaten = {'y':True,'n':False}.get(input("Zitten er gaten in? Y/N: ").lower())
duur = {'y':True,'n':False}.get(input("Is de kaas belachelijk duur? Y/N: ").lower())

blauwe_schimmels = {'y':True,'n':False}.get(input("Heeft de kaas blauwe schimmels? Y/N: ").lower())
hard = {'y':True,'n':False}.get(input("Is de kaas hard als steen? Y/N: ").lower())
korst = {'y':True,'n':False}.get(input("Heeft de kaas een korst? Y/N: ").lower())

# Emmenthaler 
if all((geel, gaten, duur)):
         print('Hmm... Ik denk dat de kaas die je in gedachten hebt Emmenthaler is.')
# Leerdammer         
elif all((geel, gaten,not duur)):
         print('Hmm... Ik denk dat de kaas die je in gedachten hebt Emmenthaler is.')  
# Pamigiano Reggiano                
elif all((geel,not gaten,hard)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Pamigiano Reggiano is.')
# Goudse kaas
elif all((geel,not gaten,not hard)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Goudse kaas is.') 
# Bleu de Rochbaron
elif all((not geel,blauwe_schimmels,korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Bleu de Rochbaron is.')
# Camembert
elif all((not geel,not blauwe_schimmels,korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Camembert is.')
# Mozzerella
elif all((not geel,not blauwe_schimmels,not korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Mozzerella is.')
# Foume d'Ambert
elif all((not geel,blauwe_schimmels,not korst)):
    print('Hmm... Ik denk dat de kaas die je in gedachten hebt Foume d\'Ambert is.')
else:
    print('Helaas weet ik het antwoord niet :(')
