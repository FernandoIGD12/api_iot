from pydantic import BaseModel

class Item(BaseModel):
    sensor_tamaño_mineral: float
    flujometro_agua: float
    velocidad_molino: float
    potencia_molino: float
    presion_descanso: float
    TPH: float