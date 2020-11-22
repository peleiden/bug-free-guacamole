Noter til Yamada et al.: LUKE

-- LUKE er en transformer trænet på et stort entitetsannoteret korpus

-- Modellen opdeler sprog ikke kun i ord, men også "entiteter", hvilket virker til bl.a. at være navne på Wikipediaartikler

-- Modellen bestemmer repræsentationer for alle disse entiteter og modellerer herigennem, forholdet mellem entiteter

-- Modellen er trænet på en maskeringsopgave baseret på BERT, hvor der skal gættes den manglende entitet. I løbet af træningen optimeres både på maskeringsopgaven og på en ny opgave, der her fremsættes.

-- Transformeren bruger entiteter i sin opmærksomhedsmekanisme
