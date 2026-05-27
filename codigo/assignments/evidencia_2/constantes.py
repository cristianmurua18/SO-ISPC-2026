
##Declaro variables globales para las 3 pruebas (monohilo, multihilos y multiprocesos)

LIMITE_SUPERIOR = 150000

# División del problema en partes (paralelización manual)
RANGOS = [          
(1, 37500),
(37501, 75000),
(75001, 112500),
(112501, 150000)
]