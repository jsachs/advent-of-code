from aocd import data

class crazydict(dict):
    def __missing__(self, key):
        if key == 'wtf':
            return locals
        if key == 'max':
            return max
        self[key] = 0
        return 0

def run(data):
    data += '\n'
    data = data.replace('\n', ' else 0\nΣ = max(Σ, *wtf().values())\n')
    data = data.replace('inc', '+=').replace('dec', '-=')
    d = crazydict()
    exec(data, {}, d)
    b = d.pop('Σ')
    return max(d.values()), b

test_data = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

assert run(test_data) == (1, 10)
a, b = run(data)
print(a)  # part a: 4448
print(b)  # part b: 6582
