# mcmedel
Este repositorio incluye pequeños scripts y notebooks utilizadas para generar las gráficas del preprint
***Método de Monte Carlo vía Cadenas de Markov: brevísima introducción***, a cargo de 
*Ricardo Medel Esquive*l (IPN), *Isidro Gómez Vargas* (IPN), *J. Alberto Vazquez* (UNAM) y *Ricardo García Salcedo* (IPN). 
El artículo 
tiene una orientación didáctica para presentar los fundamentos de los métodos MCMC. Se espera que en breve
se encuentre disponible al público.

A continuación, una breve descripción del contenido del repositorio: 

  - ***sumariemann.py*** permite calcular una integral por el método de sumas de Riemann y graficar la respectiva representación 
  (***riemannmedel.png***). Este mismo código se incluye en el notebook ***MCMedel.ipynb***.
  - ***randomwalk.py*** grafica una caminata *totalmente* aleatoria.
  - ***metropolisMedel.ipynb*** implementa un MCMC Metropolis-Hastings para el proceso aleatorio de varios 
  lanzamientos de monedas, genera varias cadenas y las grafica para verificar la convergencia del método. 
  - ***caminantesNoHayCamino.ipynb*** es una notebook que contiene el código para graficar los caminantes seudo-aleatorios 
  trazando las regiones de confianza. Se utiliza un MCMC Metropolis-Hastings para la estimación de parámetros 
  de una distribución 3D introducida en el código. 
