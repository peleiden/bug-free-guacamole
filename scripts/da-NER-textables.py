import sys, os
import json
from latextable import Texttable

DATASETS = ("DaNE", "Plank", "WikiANN")

def build_main_table(dataset: str, experiment: dict) -> str:
    print(dataset)
    t = Texttable()
    cats = ["LOC", "PER", "ORG"]
    miscdata = dataset != "WikiANN"
    if miscdata:
        cats.append("MISC")

    t.set_cols_align(["l", "l"] + ["r"]*(2+len(cats)))
    # Fix miscfuckeri
    t.add_row( ["Model", "Train data", "Micro avg.", "Micro avg. (no MISC)", *cats] )
    for mname in sorted(experiment, key=str.lower):
        v = experiment[mname]
        miscmodel = miscdata and v["stats"]["MISC"]["f1-score"] != 0
        t.add_row(
            [mname, "", v["stats"]["micro avg"]["f1-score"] if miscmodel else "-", v["stats_nomisc"]["micro avg"]["f1-score"]]
                + [v["stats"][c]["f1-score"] for c in cats]
        )

    print(t.draw())


if __name__ == '__main__':
    indir = sys.argv[1]
    experiments = {d: dict() for d in DATASETS}
    for folder in next(os.walk(indir))[1]:
        if any(d in folder for d in DATASETS):
            model, dataset = folder.split("-")
            with open(os.path.join(indir, folder, "data.json"), "r") as f:
                experiment = json.load(f)
            experiments[dataset][model] = {"stats": experiment["statistics"], "stats_nomisc": experiment["statistics_nomisc"]}
    for data, exp in experiments.items():
        build_main_table(data, exp)
