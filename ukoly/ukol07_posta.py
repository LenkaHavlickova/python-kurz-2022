import re
with open ("ukoly/posta.html", encoding = 'utf-8') as input:
  source_page = input.read()

source_page = source_page.replace("\n"," ")
reg_exp_spaces = re.compile("\s+")
source_page = re.sub(reg_exp_spaces, " ", source_page)
reg_exp_psc = re.compile("\d{3} \d{2} (?:[a-žA-Ž]+ *)+\d*")
psc_list = reg_exp_psc.findall(source_page)
for psc in psc_list:
  print(psc)