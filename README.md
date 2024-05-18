# BioBackHack
Extraccion de datos de CHEMBL DATABASE para extraer descriptores moleculares de farmacos que pudieran ser posibles farmacos candidatos
Utilizamos tecnicas de analisis de datos para extraer los farmacos candidatos, este trabajo supone el primer paso para el desarrollo de nuevos farmacos implementado inteligencia artificial generativa.
Link de nuestro google colab : https://drive.google.com/drive/folders/1K3miyPSfYD9l2OvEY6i3ecwt6QlLwfiX?usp=drive_link


# ChEMBL (ChEMBLdb) 
ChEMBL (ChEMBLdb) es una base de datos de acceso abierto que contiene información detallada sobre moléculas bioactivas con propiedades farmacológicas. Es mantenida por el Instituto Europeo de Bioinformática (EBI), y es una herramienta fundamental en la investigación y desarrollo de nuevos fármacos.

Características principales:

Datos curados manualmente: ChEMBL es reconocida por su alta calidad, ya que los datos son revisados y curados manualmente por expertos.
Amplia cobertura: Contiene información sobre millones de mediciones de bioactividad, abarcando una gran variedad de compuestos y dianas terapéuticas.
Diversidad de datos: Incluye datos de actividad biológica (Ki, Kd, IC50, EC50), estructuras químicas, información sobre dianas farmacológicas y datos genómicos.
Herramientas de análisis: Proporciona herramientas para filtrar, buscar y analizar los datos, facilitando la identificación de compuestos líderes en el descubrimiento de fármacos.

Nosotros la utilizamos para el descubrimiento de fármacos, especificamente para identificar nuevos compuestos con potencial terapéutico.






# Lipinski's rule of five

Para evaluar si determinado compuesto tiene potencial terapéutico, utilizamos Lipinski's rule of five
La regla de cinco de Lipinski, también conocida como la regla de cinco de Pfizer o simplemente la regla de cinco (RO5), es una regla práctica utilizada para evaluar la probabilidad de que un compuesto químico con cierta actividad biológica tenga propiedades que lo hagan adecuado para ser un fármaco de administración oral en humanos.

Fue formulada por Christopher A. Lipinski en 1997, basándose en la observación de que la mayoría de los fármacos administrados por vía oral son moléculas relativamente pequeñas y moderadamente lipofílicas.

**Componentes de la regla:**

La regla de Lipinski establece que, en general, un fármaco activo por vía oral no debe violar más de uno de los siguientes criterios:

* **No más de 5 donantes de enlaces de hidrógeno:** (el número total de enlaces nitrógeno-hidrógeno y oxígeno-hidrógeno).
* **No más de 10 aceptores de enlaces de hidrógeno:** (todos los átomos de nitrógeno u oxígeno).
* **Una masa molecular inferior a 500 daltons.**
* **Un coeficiente de partición octanol-agua calculado (ClogP) que no exceda de 5.**

**Importancia:**

La regla de cinco de Lipinski se utiliza ampliamente en el descubrimiento de fármacos para filtrar y priorizar compuestos con mayor probabilidad de éxito en el desarrollo clínico. Sin embargo, es importante tener en cuenta que es una regla general y que existen excepciones. Algunos fármacos aprobados violan más de uno de los criterios de la regla, especialmente en áreas terapéuticas como los antibióticos y los agentes antineoplásicos.

**Limitaciones:**

* No predice si un compuesto será activo biológicamente.
* No tiene en cuenta otros factores importantes para la biodisponibilidad oral, como la solubilidad y la estabilidad metabólica.
* Puede no ser aplicable a ciertas clases de fármacos, como los péptidos y los oligonucleótidos.

A pesar de sus limitaciones, la regla de cinco de Lipinski sigue siendo una herramienta valiosa en el descubrimiento de fármacos y ha contribuido significativamente al desarrollo de nuevos medicamentos.
