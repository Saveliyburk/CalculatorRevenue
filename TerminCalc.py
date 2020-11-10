import func as f
try:
    print('Write working time 0-17')
    zero=f.format(input())
    print('Write working time 17-0')
    seven=f.format(input())
    print('Write working time in holiday')
    holy=f.format(input())
    print("Write working time for double chat's")
    double=f.format(input())
    alltime=f.alltime(zero, seven, holy, double)
    print('Please write your stability')
    plaf=f.format(input())
    print('Please write your quality')
    kqual=f.qual(f.format(input()))
    print('Please write your self-supporting')
    ss = f.selfsup(f.format(input()))
    print('Please write your efficiency')
    eff = f.effect(f.format(input()))

    result=f.result(plaf=plaf, time=alltime, quality=kqual, selfsupport=ss, efficienty=eff)
    print('Your total revenue: {}'.format(result))

except KeyboardInterrupt:
    print('Bye-bye!!!')