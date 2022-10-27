# Creacion de un dashboard

- Creo un directorio y me posiciono en el mismo
    ```sh
    $ mkdir dashboard
    $ cd dashboard
    ```
- Creo el entorno virtual:
    ```sh
    $ python3.8 -m venv ./
    ```
    
- Activo el entorno e instalo modulos:

    ```sh
    $ source bin/activate
    (dashboard) $ pip3 install hvplot
    (dashboard) $ pip3 install jupyterlab
    (dashboard) $ pip3 install panel
    (dashboard) $ jupyter lab # en caso de no tener anaconda 
    ```