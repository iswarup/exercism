
d = {'AUG':'Methionine',
'UUU':'Phenylalanine',
'UUC':'Phenylalanine',
'UUA':'Leucine',
'UUG':'Leucine',
'UCU':'Serine',
'UCC':'Serine',
'UCA':'Serine',
'UCG':'Serine',
'UAU':'Tyrosine',
'UAC':'Tyrosine',
'UGU':'Cysteine',
'UGC':'Cysteine',
'UGG':'Tryptophan',
'UAA':'STOP',
'UAG':'STOP',
'UGA':'STOP'
}

stopCodons = ['UAA','UAG','UGA']

def proteins(strand):
    # for index in range(0,len(strand),3):
    # 	c.append(strand[index]:strand[index+3])
    proteins = []
    codons = [strand[i:i+3] for i in range(0,len(strand),3)]
    for i in codons:
    	if i in stopCodons:
    		break
    	proteins.append(d[i])
    return proteins

print(proteins('AUGUUUUCUUAAAUG'))