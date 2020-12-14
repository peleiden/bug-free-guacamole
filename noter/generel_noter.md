# Named Entity Recognition (NER)
- Følgende er baseret på [Wikipedia]( https://en.wikipedia.org/wiki/Named-entity_recognition)
- En form for informationsudtræk, hvor en streng modtages og en række annoteringer af "tokens" returneres;
- F.eks.: "Asger mistede 10000 kr. på SAS-aktier i 2021" kunne omdannes til token "Asger" af typen person, "SAS" af typen organistation" og "2021" af typen tid.
- Systemer får meget høj performance på engelsk.
- Named Entities er som regel: Pronominer, ord for levende væsener, navne for typer af objekter, kan indeholde tidsudtryk.
- Kan ses som to dele: 1. Detektion af navne (segmentering/chunking) 2. Klassifikation af navne til entitestype (kræver ontologi)
- Der findes forsøg på hierakier med typer og subtyper (forbundet med vidensbaser som Freebase)
- Evaluering af modellen er svær og der kan laves mange indviklede regler og der er forskellige "grader" af fejl hos modellen
- CoNLL bruger en streng F1-score med særlige definitioner af precision og recall. Wiki kalder den pessimistisk.
- Problem inden for NER: Generaliserbarhed. De er for domænsespecifikke.
- Også spændende arbejde med gener og kemi
- Det er nyere at bruge Wikipedia, hvilket virker ret genialt. Her er en entitet=Wikipedia-side

