
def AlturaAD(d,an):
    return an*tan(an)

def AlturaADN(d,an):
    al=AlturaAD(d,an)
    if(al<0):
        return al*(-1)
    else:
        return al
