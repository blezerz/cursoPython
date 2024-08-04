function calcular() {
    // Obtener valores de los campos de entrada
    let x1 = parseFloat(document.getElementById('x1').value);
    let y1 = parseFloat(document.getElementById('y1').value);
    let x2 = parseFloat(document.getElementById('x2').value);
    let y2 = parseFloat(document.getElementById('y2').value);

    // Crear el objeto de datos
    let datos = {
        x1: x1,
        y1: y1,
        x2: x2,
        y2: y2
    };

    // Hacer la solicitud al servidor Flask
    fetch('/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        let resultado = `Distancia: ${data.distancia.toFixed(2)} metros<br>Pendiente: ${data.pendiente !== null ? data.pendiente.toFixed(2) : 'Indefinida (línea vertical)'}`;
        document.getElementById('resultado').innerHTML = resultado;
    })
    .catch(error => console.error('Error:', error));
}
