# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_tarble1984nuevos.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_tarble1984nuevos.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_tarble1984nuevos.py
cldfbench zenodo --communities glottography cldfbench_tarble1984nuevos.py
cldfbench readme cldfbench_tarble1984nuevos.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| enap1235 | 0.46 | False | 1 |
| gali1262 | 0.00 | False | 3 |
| guam1236 | 0.00 | True | 2 |
| mapo1246 | 0.26 | False | 1 |
| otom1301 | 0.00 | True | 1 |
| puin1248 | 0.28 | False | 1 |
| pume1238 | 0.00 | True | 3 |
| sali1298 | 0.82 | False | 2 |
| tama1338 | 4.17 | False | 1 |
| yaba1248 | 0.12 | False | 1 |
