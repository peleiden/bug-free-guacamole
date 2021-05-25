# Noter til udarbejdelse af afsnittet "Deep Knowledge-enhanced NLP"

## ERNIE
- Fundet via LUKE
- https://arxiv.org/abs/1905.07129
- 17. maj 2019
- Static, separate knowledge graph
- Tilføjer vidensencoder til BERT
- "recognize named entity mentions in text and then align these mentions to their corresponding entities in KGs"
- "randomly masking some of the named entity alignments in the input text and asking the model to select appropriate entities from KGs to complete the alignments"
- "we encode the graph  structure  of  KGs  with  knowledge  embedding algorithms like TransE,and then take the informative entity embeddings as input for ERNIE"

## KGLM
- Fundet via Victor
- https://arxiv.org/abs/1906.07241
- 17. jun 2019
- "maintains a dynamically growing local knowledge graph, a subset of the knowledge graph that contains entities that have already been mentioned in the text, and their related entities"
- "when generating entity tokens, the model either decides to render a new entity that is absent from the local graph, thereby growing the local knowledge graph, or to render a fact from the local graph"

## Know-BERT
- Fundet via LUKE
- https://arxiv.org/abs/1909.04164
- 9. sep 2019

## KEPLER
- Fundet via LUKE
- https://arxiv.org/abs/1911.06136
- 13. nov 2019

## WKLM
- Fundet via LUKE
- https://arxiv.org/abs/1912.09637
- 20. dec 2019

## K-adapter
- Fundet via LUKE
- https://arxiv.org/abs/2002.01808
- 5. feb 2020

# KALM
- Fundet via egen søgning
- https://arxiv.org/abs/2007.00655v2
- 29. jun 2020

# KgPLM
- Fundet via egen søgning
- https://arxiv.org/abs/2012.03551
- 7. dec 2020
