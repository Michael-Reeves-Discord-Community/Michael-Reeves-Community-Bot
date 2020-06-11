import numpy, sys


def sort(phase):
    file = open("phase" + phase + "braindump.txt", "r")

    cont = file.read()
    file.close()
    print(cont)
    cont = cont.split(" ")

    unique = numpy.unique(cont).tolist()
    print(unique)
    file.close()

    out_str = ""

    for shitty_word in unique: 
        out_str += (shitty_word + " ") # i think you got some phase 3 stuff in there lmao the roasting otv it's good tho i am having a stronk from typing "mykull" so many times

    # aight 1290/2000 for phase 1
    file = open("sortedphase" + phase + ".txt", "w+")
    file.write(out_str[:-1])
    file.close()

if __name__ == "__main__":
    sort(sys.argv[1])
    # dab