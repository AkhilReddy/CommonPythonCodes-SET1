#static_num.x = 0

def static_num():
    static_num.x += 1
    return static_num.x


static_num.x = 0
if __name__ == '__main__':
    for i in range(10):
        print static_num()
