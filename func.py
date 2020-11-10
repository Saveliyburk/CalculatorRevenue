import default_data as dd

def alltime(zero, seven, holy, double):
    time=(zero*dd.TIME['ZERO']+(seven+holy)*dd.TIME['SEVEN']+double)*60
    return(time)

def qual(qualy):
    if qualy <dd.QUALITY['VALQ1']:
        kqualy=dd.QUALITY['KQ1']
    elif qualy < dd.QUALITY['VALQ2']:
        kqualy = dd.QUALITY['KQ2']
    elif qualy < dd.QUALITY['VALQ3']:
        kqualy = dd.QUALITY['KQ3']
    elif qualy < dd.QUALITY['VALQ4']:
        kqualy = dd.QUALITY['KQ4']
    elif qualy < dd.QUALITY['VALQ5']:
        kqualy = dd.QUALITY['KQ5']
    elif qualy < dd.QUALITY['VALQ6']:
        kqualy = dd.QUALITY['KQ6']
    elif qualy < dd.QUALITY['VALQ7']:
        kqualy = dd.QUALITY['KQ17']
    elif qualy < dd.QUALITY['VALQ8']:
        kqualy = dd.QUALITY['KQ8']
    else: kqualy = 2
    return (kqualy)

def selfsup(selfs):
    if selfs<dd.SS['VALSS1']:
        kselfs = dd.SS['KSS1']
    elif selfs <dd.SS['VALSS2']:
        kselfs = dd.SS['KSS12']
    elif selfs < dd.SS['VALSS3']:
        kselfs = dd.SS['KSS3']
    elif selfs < dd.SS['VALSS4']:
        kselfs = dd.SS['KSS4']
    elif selfs < dd.SS['VALSS5']:
        kselfs = dd.SS['KSS5']
    else: kselfs = 2
    return(kselfs)

def effect(eff):
    if eff< dd.EFF['VALEFF1']:
        keff = dd.EFF['KEFF1']
    elif eff<dd.EFF['VALEFF2']:
        keff = dd.EFF['KEFF2']
    elif eff<dd.EFF['VALEFF3']:
        keff = dd.EFF['KEFF3']
    elif eff<dd.EFF['VALEFF4']:
        keff = dd.EFF['KEFF4']
    elif eff<dd.EFF['VALEFF5']:
        keff = dd.EFF['KEFF5']
    elif eff<dd.EFF['VALEFF6']:
        keff = dd.EFF['KEFF6']
    else: keff = 1.7
    return (keff)

def format(text):
    try:
        num = float(text)
        return (num)
    except ValueError:
        print('This is not number')
        quit('Bye!')

def result(plaf, time, quality, selfsupport, efficienty):
    base = time*quality
    if plaf<dd.STABIL['MIN']:
        return base
    elif plaf<dd.STABIL['MEAN']:
        second = base*selfsupport
        return second
    else: maximaly = base*selfsupport*efficienty
    return maximaly
