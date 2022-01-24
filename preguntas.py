"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return len(tbl0)


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    return len(tbl0.columns)


def pregunta_03():
    respueta = tbl0.groupby('_c1')['_c0'].count()
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    return respueta


def pregunta_04():
    respueta = tbl0.groupby('_c1')['_c2'].mean()
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return respueta


def pregunta_05():
    respueta = tbl0.groupby('_c1')['_c2'].max()
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return respueta


def pregunta_06():
    respuesta = tbl1['_c4'].unique()
    respuesta = sorted([x.upper() for x in respuesta])
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    return respuesta


def pregunta_07():
    respuesta = tbl0.groupby('_c1')['_c2'].sum()
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return respuesta


def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    tbl0.to_csv('tbl0.tsv',sep='\t', index=False)
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    return tbl0


def pregunta_09():
    tbl0['year'] = pd.DatetimeIndex(tbl0['_c3']).year
    tbl0['year'] = tbl0['year'].apply(lambda x: str(x))
    tbl0.to_csv('tbl0.tsv',sep='\t', index=False)
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    return tbl0


def pregunta_10():
    respuesta = tbl0.groupby('_c1')['_c2'].apply(list).reset_index(name='_c2')
    respuesta['_c2'] = respuesta['_c2'].apply(lambda x: sorted(x))
    respuesta['_c2'] = respuesta['_c2'].apply(lambda x: ':'.join(map(str,x)))
    index_2 = respuesta['_c1']
    respuesta = pd.DataFrame(respuesta['_c2'].to_list(), index=index_2, columns=['_c2'])
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c2
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    return respuesta


def pregunta_11():
    respuesta = tbl1.groupby('_c0')['_c4'].apply(list).reset_index(name='_c4')
    respuesta['_c4'] = respuesta['_c4'].apply(lambda x: sorted(x))
    respuesta['_c4'] = respuesta['_c4'].apply(lambda x: ','.join(map(str,x)))
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    return respuesta


def pregunta_12():
    #convertir en lista
    respuesta1 = tbl2.groupby('_c0')['_c5a'].apply(list).reset_index(name='_c5a')
     #convertir en lista
    respuesta2 = tbl2.groupby('_c0')['_c5b'].apply(list).reset_index(name='_c5b')
    #unir las 2 dataframes
    respuesta3 = pd.merge(respuesta1,respuesta2)
    respuesta3['_c5'] = respuesta3['_c5a']
    #Generar la union de las 2 columnas
    for x in range(0,len(respuesta3)):
        list_temp = []
        for y in range(0,len(respuesta3['_c5a'].iloc[x])):
            list_temp.append(str(respuesta3['_c5a'].iloc[x][y])+':'+str(respuesta3['_c5b'].iloc[x][y]))
        respuesta3['_c5'][x] = list_temp

    respuesta3['_c5'] = respuesta3['_c5'].apply(lambda x : sorted(x))
    respuesta3['_c5'] = respuesta3['_c5'].apply(lambda x: ','.join(map(str,x)))
    respuesta3 = respuesta3[['_c0','_c5']]
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return respuesta3


def pregunta_13():
    respuesta1 = tbl0[['_c0','_c1']]
    respuesta2 = tbl2[['_c0','_c5b']]

    respuesta3 = pd.merge(respuesta1,respuesta2)

    respuesta3 = respuesta3.groupby('_c1')['_c5b'].sum()
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return respuesta3
