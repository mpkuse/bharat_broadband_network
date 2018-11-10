# Converts the raw txt file to csv or json

fname = 'List_GPs_Fbr_Blck6253a7e4-366d-41ac-89fc-9fd94d047763.txt'
fname = '0_337.csv'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content if len(x.strip()) != 0 ] # remove blank lines
content = [x for x in content if x[0] != '#']

splited_content = [ x.split(',') for x in content]

for i in range( len(splited_content) ):
    if len( splited_content[i] )!= 5 :
        print i, len( splited_content[i] ), splited_content[i]
