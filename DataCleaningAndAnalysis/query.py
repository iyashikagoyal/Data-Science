import sys

class_file = open(sys.argv[1],"r").read()

def q1():
    count = 0
    courseslist = list()
    courses = list()
    count = dict()
    number_of_courses = 0
    l1 = class_file.strip().split("\n")

    for line in l1:
        courseslist.append(line.split("-")[1].strip())
    for c in courseslist:
        courses.append(c.split("|"))
    for course in courses:
        for c1 in course:
            count[c1] = count.get(c1, 0) + 1

    for k in count:
        number_of_courses = number_of_courses + 1
    return number_of_courses


def q2(prof):
    if "," in prof:
        prof = prof.split(",")[0].strip().lower()
    else:
        prof = prof.split()[len(prof.split())-1].strip().lower()
    l1 = class_file.strip().split("\n")

    for x1 in l1:
        prof_course = x1.split("-")

        if (prof_course[0].strip() == prof):
            c = prof_course[1].strip().split("|")
            return ("|".join(c))

def word_jaccard(a,b):
    union = set(a.split()).union(set(b.split()))
    intersection = set(a.split()).intersection(set(b.split()))
    return float(len(intersection)/len(union))


def q3():
    l1 = class_file.strip().split("\n")
    dct = dict()
    professorcourses = dict()
    a = 0.0
    for line in l1:
        course = list()
        prof_course = line.split("-")
        course = prof_course[1].split("|")
        dct[prof_course[0]] = len(course)

    for k in dct:
        if dct[k]>=5:
            for line in l1:
                x = line.split("-")
                if (k == x[0]):
                    professorcourses[k] = x[1]

    for key1 in professorcourses:
        s1 = professorcourses[key1]
        for key2 in professorcourses:
            s2 = professorcourses[key2]
            if not (s1 == s2):
                if (a < word_jaccard(s1,s2)):
                    a = word_jaccard(s1,s2)
                    prof1 = key1
                    prof2 = key2
    return (prof1 + "and " + prof2)


print("Number of courses : " + str(q1()))
print(q2(sys.argv[2]))
print(q3())
