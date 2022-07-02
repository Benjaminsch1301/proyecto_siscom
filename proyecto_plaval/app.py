from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='plaval_db'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)

# Settings
app.secret_key='mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

# EMPRESA ======================================================================================================
@app.route('/empresa')
def Index_empresa():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM empresa')
    data=cur.fetchall()
    return render_template('index_empresa.html', empresa = data)


@app.route('/empresa/add_empresa', methods=['POST'])
def add_empresa():
    if request.method =='POST':
        rut= request.form['Rut']
        Nombre_empresa= request.form['Nombre_empresa']
        Direccion= request.form['Dirección']
        Nombre_encargado= request.form['Nombre_encargado']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO empresa ( Rut, Nombre_empresa, Dirección, Nombre_encargado) VALUES ( %s, %s, %s, %s)',
        (rut, Nombre_empresa,Direccion,Nombre_encargado))
        mysql.connection.commit()
        flash('Empresa añadido')
        return redirect(url_for('Index_empresa'))

@app.route('/empresa/edit/<id>')
def get_empresa(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empresa WHERE id = %s',(id))
    data = cur.fetchall()
    return render_template('edit_empresa.html',empresa=data[0])

@app.route('/empresa/update/<id>',methods=['POST'])
def update_empresa(id):
    if request.method == 'POST':
        rut= request.form['Rut']
        Nombre_empresa= request.form['Nombre_empresa']
        Direccion= request.form['Dirección']
        Nombre_encargado= request.form['Nombre_encargado']
        cur=mysql.connection.cursor()
        cur.execute('''  
            UPDATE empresa
            SET Rut= %s,
                Nombre_empresa = %s,
                Dirección= %s,
                Nombre_encargado= %s
            WHERE id = %s
            ''', (rut, Nombre_empresa,Direccion,Nombre_encargado,id))
        mysql.connection.commit()
        flash('Empresa actualizado')
        return redirect(url_for('Index_empresa'))


@app.route('/empresa/delete/<string:id>')
def delete_empresa(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM empresa WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Empresa removido ')
    return redirect(url_for('Index_empresa'))

#=====================================================================================================

# TRABAJADORES ======================================================================================

@app.route('/trabajadores')
def Index_trabajadores():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM trabajadores')
    data=cur.fetchall()
    return render_template('index_trabajadores.html', trabajadores = data)


@app.route('/trabajadores/add_trabajador', methods=['POST'])
def add_trabajador():
    if request.method =='POST':
        Rut_trabajador= request.form['Rut_trabajador']
        Nombre= request.form['Nombre']
        Apellido= request.form['Apellido']
        Especializacion= request.form['Especializacion']
        periodo_contrato= request.form['periodo_contrato']
        contacto= request.form['contacto']

        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO trabajadores (Rut_trabajador, Nombre, Apellido, Especializacion, periodo_contrato, contacto) VALUES ( %s, %s, %s, %s,%s, %s)',
        (Rut_trabajador, Nombre, Apellido,Especializacion,periodo_contrato,contacto))
        mysql.connection.commit()
        flash('Trabajador añadido')
        return redirect(url_for('Index_trabajadores'))

@app.route('/trabajadores/edit/<id>')
def get_trabajador(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM trabajadores WHERE id = %s',(id,))
    data = cur.fetchall()
    return render_template('edit_trabajadores.html',trabajadores=data[0])

@app.route('/trabajadores/update/<id>',methods=['POST'])
def update_trabajador(id):
    if request.method == 'POST':
        Rut_trabajador= request.form['Rut_trabajador']
        Nombre= request.form['Nombre']
        Apellido= request.form['Apellido']
        Especializacion= request.form['Especializacion']
        periodo_contrato= request.form['periodo_contrato']
        contacto= request.form['contacto']

        cur=mysql.connection.cursor()
        cur.execute('''  
            UPDATE trabajadores
            SET Rut_trabajador= %s,
                Nombre = %s,
                Apellido= %s,
                Especializacion= %s,
                periodo_contrato= %s,
                contacto= %s

            WHERE id = %s
            ''', (Rut_trabajador, Nombre, Apellido,Especializacion,periodo_contrato,contacto,id))
        mysql.connection.commit()
        flash('Trabajador actualizado')
        return redirect(url_for('Index_trabajadores'))


@app.route('/trabajadores/delete/<string:id>')
def delete_trabajador(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM trabajadores WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Trabajador removido ')
    return redirect(url_for('Index_trabajadores'))

# OBRA================================================================================

if __name__=='__main__':
    app.run(port=3000, debug=True)




