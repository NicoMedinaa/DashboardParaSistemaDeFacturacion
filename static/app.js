document.addEventListener("DOMContentLoaded", function() {
    function handleResponse(response){
        if(!response.ok){
            return Promise.reject({message:"HTTP Code: "+ response.status+" - Description: "+ response.statusText})
        }
        else{return response.json()}
        }

    document.getElementById("productoForm").addEventListener("submit", function(e) {
        e.preventDefault();
        
        // Recopilar los datos del formulario
        const id = document.getElementById("id").value;
        const nombre = document.getElementById("nombre").value;
        const descripcion = document.getElementById("descripcion").value;
        const precio = document.getElementById("precio").value;
        const stock = document.getElementById("stock").value;
        const categoria = document.getElementById("categoria").value;
        const proveedor = document.getElementById("proveedor").value;
        const fecha_lanzamiento = document.getElementById("fecha_lanzamiento").value;
        const fecha_vencimiento = document.getElementById("fecha_vencimiento").value;
        const fecha_modificacion = document.getElementById("fecha_modificacion").value;
        const empresa = document.getElementById("empresa").value;

        // Crear un objeto con los datos del producto
        const productoData = {
            id: id,
            nombre: nombre,
            descripcion: descripcion,
            precio: parseFloat(precio),
            stock: parseInt(stock),
            categoria: categoria,
            proveedor: proveedor, 
            fecha_lanzamiento: fecha_lanzamiento,
            fecha_vencimiento: fecha_vencimiento,
            fecha_modificacion: fecha_modificacion,
            empresa: empresa
        };

        // Enviar los datos al servidor
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify(productoData)}
        fetch('/productos', requestOptions)
        .then(response => handleResponse(response))
        .then((data) => {
            document.getElementById("mensaje").textContent = "Producto guardado con éxito. ID: " + data.id;
        })
        .catch((error) => {
            document.getElementById("mensaje").textContent = "Hubo un error al guardar el producto.";
        });

    });

 
});