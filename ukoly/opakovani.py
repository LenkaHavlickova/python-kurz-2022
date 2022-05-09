from audioop import add
from posixpath import split


opery = [
    "Figarova svatba", 
    "Don Giovanni", 
    "La Traviata",
    "Kouzelná flétna"
]

# num_char = [len(opera) for opera in opery]
# print(num_char)

# opera_words = [len(opera.split()) for opera in opery]
# print(opera_words)

autori = [
    "Mozart", 
    "Mozart", 
    "Verdi",
    "Mozart"
]

# opera_autor_list = [[opera, autori[opery.index(opera)]] for opera in opery]
# print(opera_autor_list)

# opera_autor_dict = {opera : autori[opery.index(opera)] for opera in opery}
# print(opera_autor_dict)

# autor_opera_dict = {}
# i = 0
# for autor in autori:
#   if autor not in autor_opera_dict:
#     autor_opera_dict[autor]=[opery[i]]
#     i += 1
#   else:
#     autor_opera_dict[autor].append(opery[i])
#     i += 1
# print(autor_opera_dict)

from collections import defaultdict
d = defaultdict(list)
for i in range(len(opery)):
  d[autori[i]].append(opery[i])

print(d)
