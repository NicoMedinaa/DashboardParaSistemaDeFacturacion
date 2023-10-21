document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("productoForm").addEventListener("submit", function(e) {
        e.preventDefault();
        
        // Recopilar los datos del formulario
        const nombre = document.getElementById("nombre").value;
        const descripcion = document.getElementById("descripcion").value;
        const precio = document.getElementById("precio").value;
        const stock = document.getElementById("stock").value;
        const categoria = document.getElementById("categoria").value;
        const proveedor = document.getElementById("proveedor").value;
        const fecha_lanzamiento = document.getElementById("fecha_lanzamiento").value;
        const fecha_vencimiento = document.getElementById("fecha_vencimiento").value;

        // Crear un objeto con los datos del producto
        const productoData = {
            nombre: nombre,
            descripcion: descripcion,
            precio: parseFloat(precio),
            stock: parseInt(stock),
            categoria: parseInt(categoria), // Asegúrate de que sea un entero
            proveedor: parseInt(proveedor), // Asegúrate de que sea un entero
            fecha_lanzamiento: fecha_lanzamiento,
            fecha_vencimiento: fecha_vencimiento
        };

        // Enviar los datos al servidor
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify(productoData)}
        fetch('/productos', requestOptions)
        .then(response => response.json())
        .then(data => {
            document.getElementById("mensaje").textContent = "Producto guardado con éxito. ID: " + data.id;
        })
        .catch(error => {
            document.getElementById("mensaje").textContent = "Hubo un error al guardar el producto.";
        });

    });
    
});
