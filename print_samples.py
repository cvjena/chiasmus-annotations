import sys
import json


def main():
    annotations = [a.lower() for a in sys.argv[1:]]
    if len(annotations) == 0:
        print("""
Usage:
# python print_samples.py type1 type2 type3 ...

e.g.
# python print_samples.py a c
for all chiasmi and antimetaboles
                """)
        exit()

    with open('data/data.json', 'r') as f:
        data = json.load(f)

    count = 0
    for d in data:
        if not d["annotation"].lower() in annotations:
            continue
        count += 1
        print('###', count)
        print(to_string(d))
        print("###")
        print("\n\n\n")


def to_string(sample):
    #print(type(sample['tokens'][0]))
    #tokens = [t.encode('ascii', 'ignore') for t in sample['tokens']]
    tokens = sample['tokens']
    ids = [s -sample['cont_ids'][0] for s in sample['ids']]

    print(type(tokens[0]))

    t_return = []
    for i, t in enumerate(tokens):
        if i in ids: 
            t = "["+t+"]"
        t_return.append(t)
    return " ".join(t_return)

if __name__ == "__main__":
    main()
