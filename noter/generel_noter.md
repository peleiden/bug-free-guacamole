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

# Bachelorformalia
- [DTU's bachelorprojekt-side](https://www.inside.dtu.dk/Undervisning/Regler/Afsluttende-projekter/Bachelorprojekt)
- [KID-studieordningens afsnit om bachelorprojekt](https://sdb.dtu.dk/myline#Bachelorprojekt)


# Noter til reproduktion af dansk NER

### Spørgsmål:
- Hvilken rolle har "Finn's name list" og "Wikidata+Dannet" i projektplansforslaget? - De ser ikke ud til at være NER-modeller som resten (og jeg kan ikke finde dem)
- Skal vi træne BERT, spaCy, flair osv. selv? Det antager jeg ikke - vi kan vel godt bruge færdigtrænede, offentliggjorte modeller og så selv udføre testen.
- Hvilken rolle har "Finn's name list" og "Wikidata+Dannet" i projektplansforslaget?

# Noter til engelsk LUKE

## Spørgsmål og undren

- Hvor meget træning skal vi faktisk lave? Er det bare at hente deres ned og så køre inferens? I hvor høj grad kan vi bruges Johannes og Victors arbejde?
- Vidensgrafen/-basen: Hvordan ser den faktisk ud, og hvor kommer den fra?
- Sammenhæng mellem RoBERTa og LUKE? Starten på 3.4 er konfus
- Hvad dækker prætræning helt præcist over? De bruger prætrænet RoBERTa, men det virker mere TL-agtigt
- Forskel på prætræning og træning? Betyder træning tilpasning til hvert datasæt som antydet i bilag B?
- Hvor har de deres ordforråd fra? Det lyder til at være det samme, som RoBERTa-papiret vagt hentyder til
- Er det rigtigt forstået, at datasættet er hele wikipedia, hvor  hyperlinks <=> entiteter? Antydes i starten af 3.3. Altså at entitetsforekomster som ikke-hyperlinks tælles med, hvis >1% af forekomster er hyperlinks?
- Hvor meget træning skal vi faktisk lave på den engelske? RoBERTa er jo implementeret i torch, men den videretrænes jo også

