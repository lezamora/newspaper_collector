# Newspaper collector

Proyecto para realizar scraping de sitios de noticias.


### Prerequisites

Ver requirements.txt para ver los paquetes utilizados.


### Running

Para correr el recolector de urls.
Los sitios implementados son rosario_3 y el_ciudadano.

El limite para rosario_3 es una fecha con formato dd-mm-YYYY.
El limite para el_ciudadano es numero de paginas.

```
python url_collector.py --website rosario_3 --limit 01-01-2019
```

Para correr el recolector de noticias.

```
python text_recolector.py --nrows 100
```

Donde nrows es el numero de noticias a descargar.


 Ver el makefile para mas informacion.
 
## Built With

* [Newspaper3k](https://newspaper.readthedocs.io/en/latest/) - Article scraping and curation
* [SqlAlchemy](https://www.sqlalchemy.org/) - ORM
* [Selenium Webdriver](https://www.seleniumhq.org/) - Selenium automates browsers

p://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Lucas Zamora** - *Initial work* - [lezamora](https://github.com/lezamora)

