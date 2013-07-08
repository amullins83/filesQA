def summarize(fileName="answers.txt"):
    with open(fileName, "r") as f:
        for line in f.readlines():
            print line,

if __name__ == "__main__":
    summarize()
