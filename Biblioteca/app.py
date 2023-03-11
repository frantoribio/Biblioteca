from sqlmodel import Session, select

from src.database import create_db_and_tables, engine
from src.models import Libro


def menu():
    print("Biblioteca")
    print("1. Introducir libro")
    print("2. Listar libros.")
    print("0. Salir")

    opcion = input("Introduzca una opción: ")
    if opcion == "0":
        print("Hasta pronto.")
        exit()
    elif opcion == "1":
        introducir_libro()
    elif opcion == "2":
        consultar_libros()
    else:
        print("Opción incorrecta, introduzca una opción entre 0 y 1")


def introducir_libro():
    titulo = input("Introduzca el título del libro: ")
    isbn = input("Introduzca el isbn del libro: ")
    paginas = input("Introduzca el número de páginas: ")
    with Session(engine) as session:
        libro = Libro(titulo=titulo, isbn=isbn, paginas=paginas)
        session.add(libro)
        session.commit()


def consultar_libros():
    with Session(engine) as session:
        statement = select(Libro)
        results = session.exec(statement)
        for libro in results:
            print(libro)


def main():
    create_db_and_tables()
    while True:
        menu()
        pass


if __name__ == "__main__":
    main()
