names   = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]
numbers = [  1,   1.5,  2,   2.5,  3,   4,   4.5,  5,   5.5,  6,   6.5,  7  ]

if __name__ == '__main__':
    target = input('1=')

    target_idx = names.index(target)

    result = []
    for n in range(1, 8):
        idx = (numbers.index(n) + target_idx) % len(names)
        result.append((n, names[idx]))
    
    for i in result:
        print(i[0], i[1])
