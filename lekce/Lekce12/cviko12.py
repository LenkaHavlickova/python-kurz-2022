import requests
import pandas as pd
import matplotlib.pyplot as plt

r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.csv")
open("lekce/Lekce12/kostky.csv", "wb").write(r.content)


cubes = pd.read_csv("lekce/Lekce12/kostky.csv")
# cubes.hist(bins=11)
# plt.show()

# Jaká je nejčastější hodnota, která na dvou kostkách padne?
# 7

# Je větší šance, že padne hodnota 12 než že padne hodnota 2?
# ano


r = requests.get("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.csv")
open("lekce/Lekce12/callcentrum.csv", "wb").write(r.content)

callcentrum = pd.read_csv("lekce/Lekce12/callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)
callcentrum.columns = ['minutes', 'seconds']
callcentrum['total_seconds'] = callcentrum['minutes'] * 60 + callcentrum['seconds']
callcentrum = callcentrum.drop(columns=['minutes', 'seconds'])
# callcentrum.hist(bins=25)
# callcentrum.plot(kind='box')
# plt.show()

snih = [
  [1968, 480, 351],
  [1969, 462, 663],
  [1970, 443, 490],
  [1971, 518, 444],
  [1972, 537, 420],
  [1973, 446, 941],
  [1974, 446, 691],
  [1975, 450, 477],
  [1976, 356, 395],
  [1977, 381, 652],
  [1978, 345, 525],
  [1979, 430, 762],
  [1980, 266, 316],
  [1981, 533, 781],
  [1982, 471, 769],
  [1983, 407, 801],
  [1984, 526, 633],
  [1985, 391, 488],
  [1986, 361, 624],
  [1987, 470, 471],
  [1988, 506, 514],
  [1989, 333, 208],
  [1990, 462, 909],
  [1991, 438, 443],
  [1992, 364, 488],
  [1993, 452, 579],
  [1994, 484, 519],
  [1995, 460, 809],
  [1996, 465, 682],
  [1997, 431, 814],
  [1998, 463, 595],
  [1999, 460, 512],
  [2000, 503, 750],
  [2001, 462, 951],
  [2002, 429, 413],
  [2003, 405, 738],
  [2004, 477, 777],
  [2005, 385, 316],
  [2006, 368, 417],
  [2007, 513, 635],
  [2008, 448, 689],
  [2009, 525, 443],
  [2010, 427, 225],
  [2011, 460, 618],
  [2012, 417, 742],
  [2013, 517, 247],
  [2014, 466, 552],
  [2015, 523, 441],
  [2016, 422, 690],
  [2017, 420, 699]
]
snihdf = pd.DataFrame(snih, columns=['rok', 'hora', 'udoli'])
snihdf = snihdf.set_index('rok')
snihdf.plot(kind='box')
plt.show()
