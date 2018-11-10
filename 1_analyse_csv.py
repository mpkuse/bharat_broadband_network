fname = '0_337.csv'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content if len(x.strip()) != 0 ] # remove blank lines
content = [x.split(',') for x in content if x[0] != '#']

# now the content :
# [
#    ['1', 'Haryana', ' KAITHAL', ' KAITHAL', ' Baba Ladana'],
#   ['2', 'Haryana', ' KAITHAL', ' KAITHAL', ' Budda Khera'],
#   ['3', 'Haryana', ' KAITHAL', ' KAITHAL', ' Chak Padla'],
#    ...
# ]



## How many states in this list?
list_of_uniq_states = set( [ x[1] for x in content] )
print '### How Many States in the list'
for state in list_of_uniq_states:
    print '- ', state



## Number of Districts in each state
haryana_dist =  set([ x[2] for x in content if x[1] == 'Haryana'])


## Make JSON heirarchy
import json
JSON_OBJ = {}
for x in content :
    assert( len(x) == 5 )
    if x[1] not in JSON_OBJ.keys():
        JSON_OBJ[ x[1] ] = {}

    if x[2] not in JSON_OBJ[ x[1] ].keys():
        JSON_OBJ[ x[1] ][ x[2] ] = []

    JSON_OBJ[ x[1] ][ x[2] ].append( x )

with open('state_dist_hierarchy.json', 'w') as fp:
    json.dump(JSON_OBJ, fp,  indent=4)
