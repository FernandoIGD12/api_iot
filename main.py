from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
import mysql.connector
import schemas

app = FastAPI()

origins = ['*'] # Permite que el Api Rest se consuma desde cualquier origen

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

host_name = "172.31.17.120" # IPv4 privada de "MV Bases de Datos"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_iot"  

# Get echo test for load balancer's health check
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Get all variables_tph
@app.get("/variables_tph")
def get_tphs():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM variables_tph")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"variables_tph": result}

# Get an_tph by ID
@app.get("/variables_tph/{id}")
def get_tph(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM variables_tph WHERE id = {id}")
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return {"variables_tph": result}

# Add a new_tph
@app.post("/variables_tph")
def add_tph(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    sensor_tamaño_mineral = item.sensor_tamaño_mineral
    flujometro_agua = item.flujometro_agua
    velocidad_molino = item.velocidad_molino
    potencia_molino = item.potencia_molino
    presion_descanso = item.presion_descanso
    TPH = item.TPH
    id = item.id
    cursor = mydb.cursor()
    sql = """INSERT INTO variables_tph (sensor_tamaño_mineral, flujometro_agua, 
            velocidad_molino, potencia_molino, presion_descanso, TPH), VALUES (%s, %s, %s, %s, %s, %s);"""
    val = (sensor_tamaño_mineral, flujometro_agua, velocidad_molino, potencia_molino, presion_descanso, TPH)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Variables added successfully"}

# Modify an_tph
@app.put("/variables_tph/{id}")
def update_tph(id:int, item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    sensor_tamaño_mineral = item.sensor_tamaño_mineral
    flujometro_agua = item.flujometro_agua
    velocidad_molino = item.velocidad_molino
    potencia_molino = item.potencia_molino
    presion_descanso = item.presion_descanso
    TPH = item.TPH
    id = item.id
    cursor = mydb.cursor()
    sql = """UPDATE variables_tph SET sensor_tamaño_mineral=%s, flujometro_agua=%s, 
         velocidad_molino=%s, potencia_molino=%s, presion_descanso=%s, TPH=%s 
         WHERE id=%s;"""
    val = (sensor_tamaño_mineral, flujometro_agua, velocidad_molino, potencia_molino, presion_descanso, TPH, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Variables modified successfully"}

# Delete an_tph by ID
@app.delete("/variables_tph/{id}")
def delete_tph(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM variables_tph WHERE id = {id}")
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Variables deleted successfully"}