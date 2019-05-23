import re

def main():
    l = ['python', 'jython', 'cython', '*ython-3.6']
    for w in l:
        if(re.match('.ython', w) or re.match("(p|c|j)ython", w, re.IGNORECASE) or re.match("[pcj]ython")):
            group = re.match('.ython', w).group()
            print(group)
            print('Matched!')

    mo = re.match("http://(.+)(.{3})", "http://amazon.com")
    print(mo.groups())
    # Create a RegexObject
    exp = re.compile("http://(.+)(.{3,})+")
    websites = ['http://www.google.com','http://www.codecademy.com.mx', 'http://www.motorola.com.mx','http://www.web.mx']
    for dir in websites:
        s = re.split("\.", dir)
        print('Split:',s)
        groups = exp.match(dir)
        print('Groups:',groups.groups())


if __name__ == '__main__': main()