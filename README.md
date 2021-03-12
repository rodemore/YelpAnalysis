# HackathonTAWS
Caso de estudio planteado para el Hackathon TAWS 2021 de Ciencias de Datos

## Integrantes
* Robert Moreno  
* Camilo Gutierrez
* Milca Valdez
* Stefannie Zeas

## Datasets

Los datasets sin procesar se deberán encontrar dentro de una carpeta "./Blueberry". Entre estos datasets tenemos: 
| Nombre archivo   |      Descripción      |
|----------|:-------------:|
| negocio.csv | Contiene información de cada uno de los negocios de la plataforma. |
| usuario.csv | Contiene información de los usuarios registrados en la plataforma. |
| resenia.csv | Contiene información de las reseñas de usuarios a negocios, cuantificadas con estrellas del 1 al 5. |
| checkin.csv | Contiene información de fecha-hora de los checkin de usuarios por cada negocio. |

## Metodología
Para lalalals asa jashaksa
1. lalala
2. lelele
3. lilililili

## Scripts y Notebooks
#### 0_datasets
Notebook que contiene la *lectura* de los datasets mencionados en la Sección Datasets.

#### 1_selecciónCategorias
Notebook que muestra la representatividad de las categorías de negocios para la plataforma, que porcentaje existe por cada categoría. Y la selección de las categorías de consumo, con las cuales se trabajó de ahora en adelante.  

#### 2_preProcesamientoResenias
Notebook que contiene el preprocesamiento del texto de las reseñas, incluye:
* lowercase
* remove punctuation
* remove stop words
* stemming (Posteriormente fue descartado)  

Además, contiene la distribución de palabras por reseña. 

#### 3_topicDetectionLDA
Contiene la aplicación del algorítmo LDA sobre el texto de las reseñas preprocesadas. Y que genera un dashboard HTML que estará guardado en la carpeta *"/datasets_consumo"*

#### 4_Ngrams
Contiene el uso de algoritmos de nltk que permiten la extracción de Bigrams, Trigrams y Fourgrams del texto preprocesado. 

#### 4_categorySimilarity
##### Requerimiento de uso: 

*Para que este notebook funcione correctamente es necesario descargar un Word Embedding en un archivo .vec, y colocarlo en una carpeta llamada **/Embeddings** en la raiz del repositorio. El embedding utilizado en este repositorio se lo puede obtener en el siguiente enlace ........*  

Este notebook hace uso de Word Embeddings que permitan vectorizar una frase. 

* Establece los vectores de cada categoría.
* Toma una muestra de 100000 reseñas. 
* Prepara una algoritmo que calcula la distancia coseno entre vectores. 
* Calcula la distancia de cada reseña a cada categoría.
* Estandariza los scores obtenidos usando MinMaxScaler
* Guarda los resultados en un archivo llamado reseña_scores.csv



## Evaluación de modelo
#### Métrica de rendimiento elegida
lalalalallalalalalalalalalalalal


#### Modelo creado vs Modelo entrenado de Facebook
lalalalalalalallalala


## Uso de modelo
Dentro de la carpeta */Models* se encuentra un archivo llamado predict.py, para hacer la predicción dentro de la terminal o cmd se debe ejecutarse de acuer
#### Predicción de review
Se utiliza como primer argumento **-r** para determinar que es una predicción de reseña, y como segundo argumento recibe el texto de la reseña, como se muestra a continuación: 

```
$ python predict.py -r "In general I really liked this restaurant, especially the customer service, I thought it was very good"
    { category_label: ["food", "service"],
      category_result: [0, 1],
      category_score: [0.49, 0.83]
     }
    
```

#### Predicción de dataset de reviews
Para que esta predicción sea exitosa el dataset debe ser un archivo *.csv* y debe contener el texto de las reviews en una columna llamada *texto*
Se utiliza como primer argumento **-d** para determinar que es una predicción de dataset,y como segundo argumento recibe el directorio de algún dataset de prueba, como se muestra a continuación: 
```
$ python predict.py -d "../dataset_prueba.csv"
    Prediction Completed
    
```
Esta predicción guardará un archivo .csv con los resultados de la predicción. El archivo resultante tendrá el nombre del archivo ingresado más "_results_" y más un timestamp que funcione como identificador único. Por ejemplo en este caso el archivo generado con las predicciones tendría el nombre de *dataset_prueba_results_1272121982.csv* . 
