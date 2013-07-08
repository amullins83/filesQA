def askme(fileName="answers.txt"):
    with open(fileName, "w") as f:
        for item in ["name", "quest", "favorite color"]:
            value = raw_input("What is your " + item + "?: ")
            f.write(item + ": " + value + "\n")

if __name__ == "__main__":
    askme()
