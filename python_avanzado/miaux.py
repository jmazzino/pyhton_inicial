import json
from collections import OrderedDict

dic = {
        'bomber': [1, 2, 3, 4, 5],
        'irritation': [1, 3, 5, 7, 8]
      }

json_dict = OrderedDict([
              ('filename', 'abc.pdf'),
              ('data', [ OrderedDict([
                                        ('keyword', k),
                                        ('term_freq', len(v)),
                                        ('lists', [{'occurrance': i} for i in v])
                                     ]) for k, v in dic.items()])
            ])

with open('abc.json', 'w') as outfile:
    json.dump(json_dict, outfile)


# Now to read the orderer json file

with open('abc.json', 'r') as handle:
    new_json_dict = json.load(handle, object_pairs_hook=OrderedDict)
    #print json.dumps(json_dict, indent=4)