from django.core.management.base import BaseCommand

from tienda_app.models import Inventario, Libro

LIBROS = [
    ("Clean Architecture", "120000.00", 10),
    ("Design Patterns (GoF)", "150000.00", 8),
    ("Domain-Driven Design", "135000.00", 5),
]


class Command(BaseCommand):
    help = "Crea libros e inventario de ejemplo si la tienda esta vacia (no destructivo)."

    def handle(self, *args, **options):
        if Libro.objects.exists():
            self.stdout.write("Catalogo existente, no se modifica.")
            return
        for titulo, precio, cantidad in LIBROS:
            libro = Libro.objects.create(titulo=titulo, precio=precio)
            Inventario.objects.create(libro=libro, cantidad=cantidad)
        self.stdout.write(self.style.SUCCESS(f"{len(LIBROS)} libros creados."))
