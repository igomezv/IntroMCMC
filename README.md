# mcmedel
Este repositorio incluye pequeños scripts y notebooks utilizadas para generar las gráficas del preprint
***Método de Monte Carlo vía Cadenas de Markov: brevísima introducción***, a cargo de 
*Ricardo Medel Esquive*l (IPN), *Isidro Gómez Vargas* (IPN), *J. Alberto Vazquez* (UNAM) y *Ricardo García Salcedo* (IPN). 
El artículo 
tiene una orientación didáctica para presentar los fundamentos de los métodos MCMC. Se espera que en breve
se encuentre disponible al público.

A continuación, una breve descripción del contenido del repositorio: 

  - ***sumariemann.py*** permite calcular una integral por el método de sumas de Riemann. Este mismo código se incluye en el notebook ***SumasRiemannGrandesNumeros.ipynb***, mismo que incluye       también el cálculo de la integral por medio de la ley de los grandes números.
  - ***randomwalk.py*** grafica una caminata *totalmente* aleatoria.
  - ***metropolisHastings.ipynb*** implementa un MCMC Metropolis-Hastings para el proceso aleatorio de varios 
  lanzamientos de monedas, genera varias cadenas y las grafica para verificar la convergencia del método. 
  - ***caminantes.ipynb*** es una notebook que grafica la ruta de los caminantes seudo-aleatorios 
  trazando las regiones de confianza. Se utiliza un MCMC Metropolis-Hastings para la estimación de parámetros 
  de una distribución dada en el código. 
