import sys,re


class PyPP:
    class Parser:
        @staticmethod
        def load(file_path):
            lines = []
            with open(file_path, "r") as f:
                lines = f.readlines()
            return lines
        
        @staticmethod
        def save(file_path,lines):
            with open(file_path,"w") as f:
                f.writelines(lines)


if __name__ == "__main__":
    file_path = sys.argv[1]

    lines = PyPP.Parser.load(file_path)

    for i,line in enumerate(lines):
        if "->" in line:
            # lines[i]=line.replace("->","&&&")
            m = re.search("\w*->\w*", line)
            print(m.start(), m.end())
            print(type(m.start()))
            a=line[:m.start()]
            b=line[m.start():m.end()]
            c=line[m.end():]
            
            x=b.split("->")
            b=f"{x[0]}['{x[1]}']"
            lines[i]=a+b+c

    print(lines)

    PyPP.Parser.save("test.py",lines)
