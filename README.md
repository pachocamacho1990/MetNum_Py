# Métodos Numéricos con Python
El material contenido en este repositorio sirve de soporte dinámico para un curso general de métodos numéricos para ciencias e ingeniería. 

# Pautas para empezar

Para descarga de una copia local del repositorio: 

* hacer click en la opcion _Clone or download_ y luego escoger _Download ZIP_ 

* usando [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) en sistemas LINUX/UNIX, usar en la terminal:
```
git clone https://github.com/pachocamacho1990/MetNum_Py.git
```
Para poder usar los contenidos de este repositorio desde un computador personal se recomienda instalar la version completa de [Anaconda](https://conda.io/docs/user-guide/install/index.html) (que incluye iPython y Jupyter Notebook). Luego, se sugiere cargar los notebooks de Jupyter usando [Jupyter lab](http://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html). 

* La base de ejecucion en los notebooks de Jupyter es el lenguaje iPython, se recomienda leer la documentacion sobre su uso [aquí](http://ipython.org/documentation.html).

* Los notebooks también se pueden cargar online desde la pagina de [Jupyter](http://jupyter.org) (en la opcion **Try it in your browser**). 

* El repositorio puede cargarse online en un ambiente interactivo usando binder: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/pachocamacho1990/MetNum_Py/master)

# Contenidos

Solución numérica de ecuaciones

* Métodos de Bisección y posición Falsa
* Métodos de Newton y Secante
* Método del punto fijo

[Métodos de Interpolación](https://github.com/pachocamacho1990/MetNum_Py/tree/master/Interpolacion)

* Polinomios de Newton y Lagrange
* Teorema de Interpolacion
* Trazadores Cúbicos

[Métodos de Regresion](https://github.com/pachocamacho1990/MetNum_Py/tree/master/Regresion)

* Mínimos cuadrados lineales
* Introduccion a Scikit-Learn
    
Solución de sistemas de ecuaciones

* Reducción Gaussiana
* Factorizacion LU

Solución de ecuaciones diferenciales ordinarias

* Método de Euler y Euler Mejorado
* Métodos de Taylor
* Métodos de Runge-Kutta
* Método de Verlet

Ecuaciones en derivadas parciales: diferencias finitas.

* Modelos 1D: Advección y difusión
* Modelos 2D: Advección y difusión
* Cuantificación del error numérico
* Ecuación de Navier-Stokes

# Exámenes antiguos

### Solución de ecuaciones en una variable:
* [**Examen de primer corte (2018-I)**](https://github.com/pachocamacho1990/MetNum_Py/blob/master/Examen_1/sol_1erParcial-2018-1.ipynb) 

### Métodos de Interpolacion y Regresión:
* [**Examen de segundo corte (2017-II)**](https://github.com/pachocamacho1990/MetNum_Py/blob/master/Examen_2/sol_2doParcial-2017-II.ipynb)

* [**Examen de segundo corte (2018-I)**](https://github.com/pachocamacho1990/MetNum_Py/blob/master/Examen_2/sol_2doParcial-2017-II.ipynb)

# Agradecimientos (Bibliografía)
Parte del contenido de este curso se apoya en los siguientes libros: 

* **Arévalo Ovalle, D., Bernal Yermanos, M. A., & Posada Restrepo, J. A.** (2017), *Matemáticas para Ingeniería. Métodos numéricos con Python*, Bogotá: Editorial Politécnico Grancolombiano ([click aquí](http://editorial.poligran.edu.co/matematicas-para-ingenieria-metodos-numericos-con-python.html#.WtFfwyOZPOQ)). 

* **Sauer, Timothy**, Análisis numérico. Segunda edición. PEARSON EDUCACIÓN. México. 2013([click aquí](http://recursosmcc.pearsonenespanol.com/sauer/)).

y en las siguientes publicaciones:

* **Fanaee-T, Hadi, and Gama, Joao**, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, [doi:10.1007/s13748-013-0040-3](http://dx.doi.org/10.1007/s13748-013-0040-3).
