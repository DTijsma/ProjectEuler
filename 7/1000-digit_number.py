
a1='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843'
a2='8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557'
a3='6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749'
a4='3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776'
a5='6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397'
a6='5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474'
a7='8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586'
a8='17866458359124566529476545682848912883142607690042242190226710556263211111093705442175069416589604080'
a9='7198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060'
a10='588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

number=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10



lijst=[]
for i in range(1000-13):
    p=1
    for j in range(i,i+13):
        p=p*int(number[j])
    lijst.append(p)

print(max(lijst))