# An introduction to Markov Chain Monte Carlo.

Este repositorio contiene scripts y notebooks diseñados para generar las gráficas presentadas en el artículo:

	Medel Esquivel, R., Gómez-Vargas, I., Vázquez, JA, y García Salcedo, R. (2021). Una introducción a Markov Chain Monte Carlo. *Boletín de Estadística e Investigación Operativa*, 37(1), 47-74.

El artículo está disponible para su descarga [aquí](https://www.researchgate.net/publication/350485874_An_introduction_to_Markov_Chain_Monte_Carlo).

El propósito del artículo es ofrecer una introducción didáctica a los fundamentos de los métodos de Cadena de Markov Monte Carlo (MCMC).

## Contenido del Repositorio

- **sumariemann.py**: Script para calcular integrales utilizando el método de sumas de Riemann. Este código también se encuentra en el notebook **SumasRiemannGrandesNumeros.ipynb**, que adicionalmente incluye el cálculo de integrales mediante la ley de los grandes números.
- **randomwalk.py**: Script para graficar una caminata aleatoria.
- **metropolisHastings.ipynb**: Notebook que implementa un MCMC Metropolis-Hastings para simular varios lanzamientos de moneda, generando múltiples cadenas y graficando sus convergencias.
- **caminantes.ipynb**: Notebook que muestra la trayectoria de caminantes pseudoaleatorios y traza las regiones de confianza. Se utiliza un MCMC Metropolis-Hastings para la estimación de parámetros de una distribución específica.
- **EjemploMCMC.ipynb**: Notebook para ajustar un conjunto de datos sintéticos a un modelo lineal mediante simulación MCMC.

## Cómo Citar

Si utilizas contenido de este repositorio, por favor cita el artículo de la siguiente manera:

```bibtex
@article{esquivel2021introduction,
  title={An introduction to markov chain monte carlo},
  author={Medel Esquivel, Ricardo, and G{\'o}mez-Vargas, Isidro and V{\'a}zquez, J Alberto and Salcedo, Ricardo Garc{\'\i}a},
  journal={Bolet{\'\i}n de Estad{\'\i}stica e Investigaci{\'o}n Operativa},
  volume={1},
  number={37},
  pages={47--74},
  year={2021},
  DOI={DOI: 10.13140/RG.2.2.15462.43849}
}
```


