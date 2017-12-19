def lowest(list):
    return min(list)


def highest(list):
    return max(list)


def average(list):
        avg=(sum(g)/len(list))
        return avg


def FindStudent(dic,digit):
    for s in dic:
        if dic[s] == digit:
            std=s

    return std


GRADES={
    "Ana" : 9 ,
    "Carl" : 9 ,
    "David" : 7 ,
    "Drake" : 8 ,
    "Diana" : 7 ,
    "Frank" : 9 ,
    "Gyan" : 7 ,
    "Hall" : 10 ,
    "Spencer" : 6
}

g=[]

for e in GRADES:
    g.append(GRADES[e])

print(g)

l=lowest(g)
h=highest(g)

print("%d %d" %(h,l))

b_std=FindStudent(GRADES,h)
w_std=FindStudent(GRADES,l)

print("Student with the best grade: "+str(b_std))
print("Student with the worst grade: "+str(w_std))
print("Average: "+str(average(g)))
print(w_std+" were deleted!")
del GRADES[w_std]
g.remove(l)