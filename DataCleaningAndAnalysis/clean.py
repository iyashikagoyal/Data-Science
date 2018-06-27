import sys
class_file = open(sys.argv[1],"r").read()


lst = class_file.strip().split("\n")
newlst = list()
class_lst = list()
cleaned = dict()

#replaced "-" in courses with "space"
for e1 in lst:
    c = e1.split("-")
    l1 = list()
    c1 = str()
    if len(c)>2:
        for i in range(1,len(c)):
            c1 = str(c1) + " " +  str(c[i])
        l1.append(c[0])
        l1.append(c1)
        class_lst.append("-".join(l1))
    elif len(c)==2:
        class_lst.append("-".join(c))

#change the format of names of all professors to last_name, first_name
for element in class_lst:
    name = element.split("-")[0].rstrip()
    if ("." in name):
        name = " ".join(name.split("."))

    if "," in name:
        n = name

    else:
        n = name.split()

        i=len(n)-2
        temp=n[len(n)-1]
        while (i>=0):
            n[i+1] = n[i].rstrip()
            i=i-1
        n[0]=temp.rstrip()
        n.insert(1, ',')
        n = " ".join(n)
    split_lst = class_lst[class_lst.index(element)].split("-")
    split_lst[0] = n

    newlst.append("-".join(split_lst))


def character_jaccard(a,b):
    union = set(a).union(set(b))
    intersection = set(a).intersection(set(b))
    return float(len(intersection)/len(union))

def word_jaccard(a,b):
    union = set(a.split()).union(set(b.split()))
    intersection = set(a.split()).intersection(set(b.split()))
    return float(len(intersection)/len(union))


count = 0

#performed instance matching through jaccard and replaced the course with one of them.
for l1 in newlst:
    x1 = l1.split("-")[1].strip().lower().split("|")
    for e1 in x1:
        for l2 in newlst:
            x2 = l2.split("-")[1].strip().lower().split("|")
            for e2 in x2:
                if not (e1 == e2):
                    if word_jaccard(e1,e2) > 0.5:
                        if 0.82 <= character_jaccard(e1,e2) < 1.0:
                            count = count+1

                            for line in newlst:
                                a = newlst[newlst.index(line)].split("-")[1].strip().lower().split("|")

                                if e1 in a:

                                    newlst[newlst.index(line)] = newlst[newlst.index(line)].replace(e1,e2)


#searched for the similar professor through jaccard and grouped their courses, stored them into dict = cleaned
for i1 in newlst:
    n1 = i1.split("-")[0].lower()
    for i2 in newlst:
        if not (newlst.index(i1) == newlst.index(i2)):
            n2 = i2.split("-")[0].lower()
            if character_jaccard(n1,n2) >0.8:
                if word_jaccard(n1,n2)>0.0:

                    lastname1 = n1.split(",")[0].strip()

                    course1 = newlst[newlst.index(i1)].split("-")[1].strip().lower().split("|")
                    course2 = newlst[newlst.index(i2)].split("-")[1].strip().lower().split("|")

                    if not lastname1 in cleaned:
                        cleaned[lastname1] = []
                    for item1 in course1:
                        if not (item1 in cleaned[lastname1]):
                            cleaned[lastname1].append(item1)
                    for item2 in course2:
                        if not (item2 in cleaned[lastname1]):
                            cleaned[lastname1].append(item2)

#appended the rest of prof-course to cleaned
for line in newlst:
    lastname = line.split("-")[0].split(",")[0].strip().lower()
    course = line.split("-")[1].strip().lower().split("|")
    if not lastname in cleaned:
        cleaned[lastname] = []
    for item in course:
        if not (item in cleaned[lastname]):
            cleaned[lastname].append(item)


groupedlist = list()
cleanedlist = list()

#sorted the courses for every professor
for key in cleaned:
    cleaned[key] = sorted(cleaned[key])

#stored the prof-course into a list from dictionary
for k,v in cleaned.items():
    t = [k,v]
    groupedlist.append(t)

#sorted the list by lastname of prof.
groupedlist = sorted(groupedlist)

#converted the list to the same format as original
for line in groupedlist:
    x = list()
    x.append(line[0])
    x.append("|".join(line[1]))
    cleanedlist.append(" - ".join(x))

#created a cleaned.txt file and wrote the data to text file.
file =  open('cleaned.txt','w')
for line in cleanedlist:
    file.write("%s\n" % line)
file.close()
