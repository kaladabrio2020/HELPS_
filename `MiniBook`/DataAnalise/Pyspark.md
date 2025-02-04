# PySpark

|    | gender |   age |   hypertension |   heart_disease | smoking_history   |   bmi |   HbA1c_level |   blood_glucose_level |   diabetes |
|---:|:---------|------:|---------------:|----------------:|:------------------|------:|--------------:|----------------------:|-----------:|
|  0 | Female   |    17 |              0 |               1 | never             | 25.19 |           6.6 |                   140 |          0 |
|  1 | Female   |    54 |              0 |               0 | No Info           | 27.32 |           6.6 |                    80 |          0 |
|  2 | Male     |    28 |              0 |               0 | never             | 27.32 |           5.7 |                   158 |          0 |
|  3 | Female   |    36 |              0 |               0 | current           | 23.45 |           5   |                   155 |          0 |
|  4 | Male     |    76 |              1 |               1 | current           | 20.14 |           4.8 |                   155 |          0 |
|  5 | Female   |    20 |              0 |               0 | never             | 27.32 |           6.6 |                    85 |          0 |
|  6 | Female   |    44 |              0 |               0 | never             | 19.31 |           6.5 |                   200 |          1 |
|  7 | Female   |    79 |              0 |               0 | No Info           | 23.86 |           5.7 |                    85 |          0 |
|  8 | Male     |    42 |              0 |               0 | never             | 33.64 |           4.8 |                   145 |          0 |
|  9 | Female   |    32 |              0 |               0 | never             | 27.32 |           5   |                   100 |          0 |


&nbsp;

## Iniciando Sessão Spark

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MinhaSessaoSpark") \ 
    .getOrCreate()vo
```

* **.appName()** : Você pode definir um nome para sua aplicação Spark

* **.getOrCreate()** :

## Read File

```python
data = spark.read.option(
    "header", True
).format('csv').load('path/file.csv')
```

* **load** : usado para ler dados de uma fonte de dados específica, como um arquivo ou um banco de dados, e carregá-los em um DataFrame
* **format**: Tipo de arquivo
* **option**:
    1. *header* (booleano): Indica se a primeira linha do arquivo contém o cabeçalho com os nomes das colunas.
        * option("header", True) 
    2. *inferSchema* (booleano): De Indica se o Spark deve inferir automaticamente os tipos de dados das colunas.
        *  option("inferSchema", True) 
    3. *delimiter* (string): Define o caractere de delimitação usado para separar os campos no arquivo (padrão é a vírgula ",").
option("delimiter", "\t") para um arquivo com tabulação como delimitador.
    4. charset (string): Define o conjunto de caracteres (encoding) do arquivo, como "UTF-8" ou "ISO-8859-1".
        * option("charset", "UTF-8")


## Save File
```python
data.write.format('tipo').save('path/file.tipo')
```

## Select

```python
data.select('coluna').show()
```
outra forma:
```python
data.select(data['gender']).show()
```

### Seleção com condição
```python
data.select(data['gender']).filter(data['gender']=='Female').show()
```
Com mais de um condição `&`(and) e `|`(or)
```python
data.select(data['gender']).filter((data['gender']=='Female') & (data['age']<18)).show()
```