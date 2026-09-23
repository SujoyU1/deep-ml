def dice_statistics(n: int) -> tuple[float, float]:
    mean=0

    for i in range(1,n+1):
        mean=mean+i
    mean=mean/n
    var=0
    for i in range(1,n+1):
        var+=(i-mean)**2
    var=var/n
    return (mean,var)