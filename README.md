# IntroMCMC
Este repositorio incluye pequeños scripts y notebooks utilizados para generar las gráficas del artículo
***An introduction to Markov Chain Monte Carlo***, a cargo de 
Ricardo Medel Esquivel (IPN), Isidro Gómez Vargas (IPN), J. Alberto Vazquez (UNAM) y Ricardo García Salcedo (IPN). 

El artículo tiene una orientación didáctica para presentar los fundamentos de los métodos MCMC. Se espera que en breve
se encuentre disponible al público.

A continuación, una breve descripción del contenido del repositorio: 

  - ***sumariemann.py*** permite calcular una integral por el método de sumas de Riemann. Este mismo código se incluye en el notebook ***SumasRiemannGrandesNumeros.ipynb***, mismo que también incluye el cálculo de una integral por medio de la ley de los grandes números.
  - ***randomwalk.py*** grafica una caminata *totalmente* aleatoria.
  - ***metropolisHastings.ipynb*** implementa un MCMC Metropolis-Hastings para el proceso aleatorio de varios 
  lanzamientos de monedas, genera varias cadenas y las grafica para verificar la convergencia del método. 
  - ***caminantes.ipynb*** es una notebook que grafica la ruta de los caminantes seudo-aleatorios 
  trazando las regiones de confianza. Se utiliza un MCMC Metropolis-Hastings para la estimación de parámetros 
  de una distribución dada en el código. 
 - ***EjemploMCMC.ipynb*** es una notebook que ajusta un conjunto de datos sintéticos a un modelo lineal mediante una simulación MCMC.
