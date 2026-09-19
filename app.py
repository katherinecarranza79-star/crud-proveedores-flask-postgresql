from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)


# ==============================
# PÁGINA DE INICIO
# ==============================

@app.route("/")
def inicio():
    return render_template("inicio.html")


# ==============================
# LISTAR PROVEEDORES
# ==============================

@app.route("/proveedores")
def proveedores():
    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, nit, telefono, correo, direccion, activo, fecha_registro
        FROM proveedores
        ORDER BY id DESC
    """)

    lista_proveedores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "proveedores.html",
        proveedores=lista_proveedores
    )


# ==============================
# CREAR PROVEEDOR
# ==============================

@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def nuevo_proveedor():

    if request.method == "POST":
        nombre = request.form["nombre"]
        nit = request.form["nit"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        direccion = request.form["direccion"]
        activo = "activo" in request.form

        conexion = get_db_connection()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO proveedores
            (nombre, nit, telefono, correo, direccion, activo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            nit,
            telefono,
            correo,
            direccion,
            activo
        ))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("proveedores"))

    return render_template("nuevo_proveedor.html")


# ==============================
# EDITAR PROVEEDOR
# ==============================

@app.route("/proveedores/editar/<int:id>", methods=["GET", "POST"])
def editar_proveedor(id):

    conexion = get_db_connection()
    cursor = conexion.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        nit = request.form["nit"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        direccion = request.form["direccion"]
        activo = "activo" in request.form

        cursor.execute("""
            UPDATE proveedores
            SET nombre = %s,
                nit = %s,
                telefono = %s,
                correo = %s,
                direccion = %s,
                activo = %s
            WHERE id = %s
        """, (
            nombre,
            nit,
            telefono,
            correo,
            direccion,
            activo,
            id
        ))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("proveedores"))

    cursor.execute("""
        SELECT id, nombre, nit, telefono, correo, direccion, activo
        FROM proveedores
        WHERE id = %s
    """, (id,))

    proveedor = cursor.fetchone()

    cursor.close()
    conexion.close()

    if proveedor is None:
        return redirect(url_for("proveedores"))

    return render_template(
        "editar_proveedor.html",
        proveedor=proveedor
    )


# ==============================
# ELIMINAR PROVEEDOR
# ==============================

@app.route("/proveedores/eliminar/<int:id>", methods=["POST"])
def eliminar_proveedor(id):

    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM proveedores
        WHERE id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for("proveedores"))


# ==============================
# EJECUTAR APLICACIÓN
# ==============================

if __name__ == "__main__":
    app.run(debug=True)