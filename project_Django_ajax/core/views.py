
from django.shortcuts import render
from django.http import JsonResponse
import json 

# Simulación de datos (Mock Data)
ESTADOS_MUNICIPIOS = {
    "1": {"nombre": "Aguascalientes", "municipios": ["Aguascalientes", "Asientos", "Calvillo"]},
    "2": {"nombre": "Baja California", "municipios": ["Mexicali", "Tijuana", "Ensenada"]},
    "3": {"nombre": "Baja California Sur", "municipios": ["La Paz", "Los Cabos", "Comondú"]},
    "4": {"nombre": "Campeche", "municipios": ["Campeche", "Carmen", "Champotón"]},
    "5": {"nombre": "Chiapas", "municipios": ["Tuxtla Gutiérrez", "Tapachula", "San Cristóbal de las Casas"]},
    "6": {"nombre": "Chihuahua", "municipios": ["Chihuahua", "Juárez", "Delicias"]},
    "7": {"nombre": "Coahuila de Zaragoza", "municipios": ["Saltillo", "Torreón", "Monclova"]},
    "8": {"nombre": "Colima", "municipios": ["Colima", "Manzanillo", "Villa de Álvarez"]},
    "9": {"nombre": "Ciudad de México", "municipios": ["Álvaro Obregón", "Coyoacán", "Cuauhtémoc"]},
    "10": {"nombre": "Durango", "municipios": ["Durango", "Gómez Palacio", "Lerdo"]},
    "11": {"nombre": "Guanajuato", "municipios": ["León", "Irapuato", "Celaya"]},
    "12": {"nombre": "Guerrero", "municipios": ["Acapulco de Juárez", "Chilpancingo de los Bravo", "Iguala de la Independencia"]},
    "13": {"nombre": "Hidalgo", "municipios": ["Pachuca de Soto", "Tulancingo de Bravo", "Tula de Allende"]},
    "14": {"nombre": "Jalisco", "municipios": ["Guadalajara", "Zapopan", "Tlaquepaque"]},
    "15": {"nombre": "México", "municipios": ["Toluca", "Ecatepec de Morelos", "Nezahualcóyotl"]},
    "16": {"nombre": "Michoacán de Ocampo", "municipios": ["Morelia", "Uruapan", "Zamora"]},
    "17": {"nombre": "Morelos", "municipios": ["Cuernavaca", "Jiutepec", "Cuautla"]},
    "18": {"nombre": "Nayarit", "municipios": ["Tepic", "Bahía de Banderas", "Santiago Ixcuintla"]},
    "19": {"nombre": "Nuevo León", "municipios": ["Monterrey", "Guadalupe", "Apodaca"]},
    "20": {"nombre": "Oaxaca", "municipios": ["Oaxaca de Juárez", "San Juan Bautista Tuxtepec", "Salina Cruz"]},
    "21": {"nombre": "Puebla", "municipios": ["Puebla", "Tehuacán", "Atlixco"]},
    "22": {"nombre": "Querétaro", "municipios": ["Querétaro", "San Juan del Río", "Corregidora"]},
    "23": {"nombre": "Quintana Roo", "municipios": ["Benito Juárez", "Othón P. Blanco", "Solidaridad"]},
    "24": {"nombre": "San Luis Potosí", "municipios": ["San Luis Potosí", "Soledad de Graciano Sánchez", "Matehuala"]},
    "25": {"nombre": "Sinaloa", "municipios": ["Culiacán", "Mazatlán", "Ahome"]},
    "26": {"nombre": "Sonora", "municipios": ["Hermosillo", "Cajeme", "Nogales"]},
    "27": {"nombre": "Tabasco", "municipios": ["Centro", "Cárdenas", "Comalcalco"]},
    "28": {"nombre": "Tamaulipas", "municipios": ["Reynosa", "Matamoros", "Nuevo Laredo"]},
    "29": {"nombre": "Tlaxcala", "municipios": ["Tlaxcala", "Apizaco", "Huamantla"]},
    "30": {"nombre": "Veracruz de Ignacio de la Llave", "municipios": ["Veracruz", "Xalapa", "Coatzacoalcos"]},
    "31": {"nombre": "Yucatán", "municipios": ["Mérida", "Kanasín", "Valladolid"]},
    "32": {"nombre": "Zacatecas", "municipios": ["Zacatecas", "Fresnillo", "Guadalupe"]},
}

# 1. Vista que renderiza la plantilla principal
def selects_view(request):
    """Renderiza el formulario con la lista inicial de estados."""
    estados = [{"id": id, "nombre": data["nombre"]} for id, data in ESTADOS_MUNICIPIOS.items()]
    return render(request, 'selects.html', {'estados': estados})

# 2. Vista que maneja la petición AJAX (GET)
def get_municipios(request, estado_id):
    
    # verificación de AJAX
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' 

    
    if request.method == 'GET':
        estado_data = ESTADOS_MUNICIPIOS.get(str(estado_id))
        
        if estado_data:
            # Retorna la lista de municipios como JSON
            return JsonResponse({'municipios': estado_data['municipios']}, status=200)
        
        # Estado no encontrado
        return JsonResponse({'error': 'Estado no encontrado'}, status=404)
    
    # Si la solicitud no es GET (ej. es POST, PUT, etc.), devolvemos 405.
    return JsonResponse({'error': 'Método no permitido'}, status=405)