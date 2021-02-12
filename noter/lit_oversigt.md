# Teori og modeller
- Yamada et al: ["LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention"](https://www.aclweb.org/anthology/2020.emnlp-main.523/).
    Indfører nye, lærte representationer af ord og entiteter, som er lært ved en maskeret gætteopgave af en self-attention-mekanisme.
- Hvingelby et al: ["DaNE: A Named Entity Resource for Danish"](https://www.aclweb.org/anthology/2020.lrec-1.565/).
    Præsenterer selve annoteringerne og træner en række modeller herunder BERT på det nye data. Fokuserer både på flersproget og rent dansk.
    Deres metode til annotering bygger på CoNLL-2003 (se Sang et al.) og har krævet en masse manuelt arbejde.
- Derczynski et al: ["DKIE: Open Source Information Extraction for Danish"](https://www.aclweb.org/anthology/E14-2016/).
    Præsenterer værktøjet DKIE, der ser ud til at være en altmulig-pipeline for NLP, men indeholder også NER-annoteringer og NER-modeller.
    De NER-annoterer Copenhagen Dependency Treebank for person/lokation/organisation "i overenstemmelse med ACE-guidelines" (uklart).
    De kalder annoteringen "ongoing" i 2014 og at de har 100 000 på dette tidspunkt tokens.
- Derczynski: ["Simple Natural Language Processing Tools for Danish"](https://arxiv.org/abs/1906.11608).
    Forklarer kort NLP-værktøjer; herunder NER-værktøjet `daner`, som bygger på DKIE-data og -pipeline.
- Liu et al: [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)
- Plank: [Neural Cross-Lingual Transfer and Limited Annotated Data for Named Entity Recognition in Danish](https://www.aclweb.org/anthology/W19-6143/)
    NER-datasæt
- Johannsen et al: [Universal Dependencies for Danish](http://tlt14.ipipan.waw.pl/files/4914/4974/3227/TLT14_proceedings.pdf#page=164).
    Generation af datasæt, som bruges af DaNE

# Reviews/challenges
- Pradhan et al: ["CoNLL-2012 Shared Task:ModelingMultilingual Unrestricted Coreference in OntoNotes"](http://disi.unitn.eu/moschitti/articles/2012/CONLL2012.pdf)
    Handler om mange forskellige NLP-ting, men der er også en smule om NER, hvor de er gået op til 18 kategorier så vidt jeg kan se

- Sang et al: ["Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition"](https://arxiv.org/abs/cs/0306050)
    Beskriver en NER-challenge med data på engelsk og tysk. Ser ud til, at de bruger 4 kategorier: LOC, MISC, ORG, PER.
    Præsenterer også resultaterne på opgaven.

# Mere uformelle forklaringer
- Hofer: ["Deep Learning for Named Entity Recognition"](https://towardsdatascience.com/deep-learning-for-ner-1-public-datasets-and-annotation-methods-8b1ad5e98caf)
    En artikel på towardsdatascience om NER
- Pascal Poupart: [CS480/680 Lecture 19: Attention and Transformer Networks](https://www.youtube.com/watch?v=OyFJWRnt_AY)
- Årup Nielsen: ["Awesome Danish NLP"](https://github.com/fnielsen/awesome-danish)
    Kæmpe samling af kilder til dansk NLP
- Jagtap: ["RoBERTa: Robustly Optimized BERT Pretraining Approach"](https://medium.com/dataseries/roberta-robustly-optimized-bert-pretraining-approach-d033464bd946)
    En Medium-artikel om RoBERTa
