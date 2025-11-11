# TP_ALGO_MergeSort_And_QuickSort
> Objectif :

Protocole expérimental

|Paramétre | Valeurs à tester
|------|------|
|Taille de tableua|1K,5K,10K,50K,..|
|Type de tableua|A léatoire, Tré, inverscé|
|Algorithmes|Merge sort, Quick sort|
|Mesure|Comparaisons, échanges, Temps|
|Répétition| >= 5|

> Result :
```
Taille    Type      Algorithme  Comparaisons   Déplacements   Temps (s) 
1000      random    MergeSort   8700           9976           0.00294   
1000      random    QuickSort   11611          8114           0.00237   
1000      sorted    MergeSort   4932           9976           0.00189   
1000      sorted    QuickSort   11075          7083           0.00361   
1000      reversed  MergeSort   5044           9976           0.00340   
1000      reversed  QuickSort   10076          6375           0.00196   
5000      random    MergeSort   55243          61808          0.01991   
5000      random    QuickSort   80085          45409          0.01353   
5000      sorted    MergeSort   29804          61808          0.01070   
5000      sorted    QuickSort   67676          41126          0.01184   
5000      reversed  MergeSort   32004          61808          0.01880   
5000      reversed  QuickSort   72061          42170          0.02163   
10000     random    MergeSort   120387         133616         0.03787   
10000     random    QuickSort   159582         91709          0.02835   
10000     sorted    MergeSort   64608          133616         0.02328   
10000     sorted    QuickSort   152660         90361          0.02539   
10000     reversed  MergeSort   69008          133616         0.02330   
10000     reversed  QuickSort   154835         84472          0.02542   
50000     random    MergeSort   718146         784464         0.21961   
50000     random    QuickSort   995562         544329         0.16392   
50000     sorted    MergeSort   382512         784464         0.12652   
50000     sorted    QuickSort   954889         549460         0.15036   
50000     reversed  MergeSort   401952         784464         0.13687   
50000     reversed  QuickSort   928098         560758         0.16837   
100000    random    MergeSort   1536453        1668928        0.45864   
100000    random    QuickSort   1967300        1140852        0.34068   
100000    sorted    MergeSort   815024         1668928        0.28500   
100000    sorted    QuickSort   1938038        1092995        0.29714   
100000    reversed  MergeSort   853904         1668928        0.27201   
100000    reversed  QuickSort   1943702        1119548        0.32496   
1000000   random    MergeSort   18673994       19951424       7.14781   
1000000   random    QuickSort   24695732       13938075       5.14140   
1000000   sorted    MergeSort   9884992        19951424       3.86878   
1000000   sorted    QuickSort   24930351       14577778       4.49070   
1000000   reversed  MergeSort   10066432       19951424       3.22951   
1000000   reversed  QuickSort   24977888       13730579       3.84633   
10000000  random    MergeSort   220103453      233222784      84.58407  
10000000  random    QuickSort   291685019      168709714      83.99666  
10000000  sorted    MergeSort   114434624      233222784      40.71919  
10000000  sorted    QuickSort   305084995      164921001      47.97295  
10000000  reversed  MergeSort   118788160      233222784      40.81410  
10000000  reversed  QuickSort   285627447      152659022      46.99328 
```
