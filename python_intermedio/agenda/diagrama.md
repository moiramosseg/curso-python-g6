# Diagrama UML – Agenda y Contacto

```mermaid
classDiagram
    direction LR

    class Agenda {
        -str propietario
        -list~Contacto~ contactos
        +agregar_contacto(contacto) bool
        +buscar_contacto(nombre) Contacto
        +eliminar_contacto(nombre) bool
        +editar_telefono(nombre, tel) bool
        +listar_contactos() None
        +total_contactos() int
    }

    class Contacto {
        -str nombre
        -str telefono
        -str email
        +get_nombre() str
        +get_telefono() str
        +get_email() str
        +set_telefono(telefono) None
        +set_email(email) None
        +mostrar() str
    }

    Agenda "1" o-- "0..*" Contacto : tiene
```

## Leyenda

| Símbolo | Significado |
|---------|-------------|
| `-` | Atributo/método privado |
| `+` | Atributo/método público |
| `o--` | Agregación: la Agenda tiene Contactos |
| `1` / `0..*` | Una agenda tiene cero o muchos contactos |