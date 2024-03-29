import sys, os
import json

from latextable import Texttable, draw_latex
import pyperclip

DATASETS = ("DaNE", "Plank", "WikiANN")
MODEL_NAMES = {
    "BERT":             "DaNLP da-BERT",
    "mBERT":            "NERDA m-BERT",
    "Ælæctra":          "NERDA Ælæctra",
    "DaCyMedium":       "DaCy medium",
    "DaCyLarge":        "DaCy large",
    "spaCy":            "DaNLP spaCy",
    "Flair":            "DaNLP Flair",
    "Polyglot":         "Polyglot",
    "daner":            "daner",
}

MODEL_TRAINDATA = {
    "BERT":         "DaNE",
    "mBERT":        "DaNE",
    "Ælæctra":      "DaNE",
    "DaCyMedium":   "DaNE",
    "DaCyLarge":    "DaNE",
    "spaCy":        "DaNE",
    "Flair":        "DaNE",
    "Polyglot":     "Wikipedia",
    "daner":        "ITU CDT",
}

def f1f(f: float) -> str:
    """ Format F1-score """
    if f  == "-": return f
    return "%.2f" % (f*100)

def build_main_table(dataset: str, experiment: dict) -> str:
    t = Texttable()
    t.set_deco(t.HEADER)
    cats = ["LOC", "PER", "ORG"]
    miscdata = dataset != "WikiANN"
    # Fix miscfuckeri
    row = ["Model name", "Trained on", "F1"]
    if miscdata:
        row.append(r"F1 {\tiny\textdiscount MISC}")
        cats.append("MISC")
    row += ["Prec.", "Rec."]
    row += cats

    t.set_cols_align(["l", "l"] + ["c"]*(3+len(cats)+int(miscdata)))
    t.set_cols_dtype(["t"]*len(row)) # Dont overwrite my formatting pls
    t.header(row)

    for m, mname in MODEL_NAMES.items():
        v = experiment[m]
        row = [mname, MODEL_TRAINDATA[m]]
        if miscdata:
            row.append(f1f(v["stats"]["micro avg"]["f1-score"]) if v["stats"]["MISC"]["f1-score"] else "-")
        row.append(f1f(v["stats_nomisc"]["micro avg"]["f1-score"]))
        row.append(f1f(v["stats"]["micro avg"]["precision"]))
        row.append(f1f(v["stats"]["micro avg"]["recall"]))
        row += [f1f(v["stats"][c]["f1-score"] or "-") for c in cats]
        t.add_row(row)
    #print(t.draw())
    out = draw_latex(t, caption=f"F1\pro-scores of Danish NER models of the {dataset} data-set consisting of {v['N']} sentences.", label=f"tab:{dataset}")
    print(out)
    return out

if __name__ == '__main__':
    indir = sys.argv[1]
    experiments = {d: dict() for d in DATASETS}
    for folder in next(os.walk(indir))[1]:
        if any(d in folder for d in DATASETS):
            model, dataset = folder.split("-")
            with open(os.path.join(indir, folder, "data.json"), "r") as f:
                experiment = json.load(f)
            experiments[dataset][model] = {
                    "stats": experiment["statistics"],
                    "stats_nomisc": experiment["statistics_nomisc"],
                    "N": len(experiment["predictions"])
                }
    pyperclip.copy("\n\n".join(
        build_main_table(data, exp) for data, exp in experiments.items()
        )
    )
