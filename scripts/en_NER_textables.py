import sys, os
import json

import numpy as np
from latextable import Texttable, draw_latex
import pyperclip


SIZES = ("large", "base")
REPS  = range(1, 6)
#FIXME: Handle micro average
cats = ("Micro avg.", "LOC", "PER", "ORG", "MISC")
def arr_f1f(a: np.ndarray) -> str:
    """ Format F1-score """
    return "%.2f \pm  %.1g" % (a.mean()*100, a.std()*100)

def read(path: str) -> list:
    reps = list()
    with open(os.path.join(path), "r") as f:
        L = list(f)
    for i in range(len(L)):
        if "The number of labels: 46435" in L[i]: #Then we have test-set
            rep = {f: dict() for f in F1s}

            for j in range(i+3, i+9):
                if stats := L[j].split():
                    # Handle microp average being two words
                    rep[stats[0].strip()]["f1-score"] = float(stats[3])
                    rep[stats[0].strip()]["support"] =  int(stats[4])
            reps.append(rep)
    return reps


def build_main_table(exp: dict) -> str:
    t = Texttable()
    t.set_deco(t.HEADER)
    header = ("Model", *F1s)
    t.set_cols_align(["l"] + ["r"]*5)
    t.set_cols_dtype(["t"]*len(header))
    t.header(header)


if __name__ == '__main__':
    indir = sys.argv[1]
    experiments = {s: read(os.path.join(indir, f"english_luke_{s}_ner.txt")) for s in SIZES}
    print(experiments)

    # pyperclip.copy(
    #     build_main_table(experiments)
    # )


