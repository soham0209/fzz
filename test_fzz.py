import pyfzz

if __name__ == '__main__':
    fzz = pyfzz.pyfzz()
    bars = fzz.compute_zigzag([('i', [0]), ('i', [1]), ('i', [0, 1]), ('d', [0, 1]), ('d', [1])])
    # bars = fzz.compute_zigzag([('i', [0]), ('i', [1]), ('i', [0, 1])])

    print(bars)