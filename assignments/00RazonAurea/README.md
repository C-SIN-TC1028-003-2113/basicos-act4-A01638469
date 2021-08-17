![Tec de Monterrey](../../images/logotecmty.png)
# Razón Aurea


Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    #El mensaje para recibir el dato debe ser **"Area a pintar en metros: ** y **Rendimiento (m2/l): ** "
    #El mensaje para la salida debe ser **"Litros a comprar: **"
    

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema

La razón áurea es un número irracional,​ representado por la letra griega phi en honor al escultor griego Fidias. Este número aparece repetidamente en el mundo que nos rodea, La proporción áurea podremos encontrarla en el arte, la música e incluso en las proporciones de nuestro cuerpo. En matemáticas, la razón áurea será una forma de dividir un segmento en 2 partes: lo pequeño es a lo grande como lo grande es al todo. Su valor se calcula de la siguiente manera:

varphi = (1+sqrt(5))/2


**Entradas:**
Un número flotante que representa el número por el cuál se multiplicará la razón aurea (resultado de la fórmula).
Un entero que representa el número de cifras decimales para el despliegue del número.
(Los valores se deben ingresar cada uno en un renglón y en el orden indicado).

**Salida:**
La razón áurea

Ejemplo:
```
Número: 1.5
Decimales a mostrar: 3
Razón áurea: 2.427
```
Ejemplo 2:
```
Número: 4.7
Decimales a mostrar: 5
Razón áurea: 7.60476
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
