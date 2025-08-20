// Referencias a los elementos
const productSelect = document.getElementById("product");
const batchDateInput = document.getElementById("batch_date");

// Poner la fecha de hoy por defecto
const today = new Date().toISOString().split("T")[0]; // yyyy-mm-dd
batchDateInput.value = today;

// Función para cargar productos desde el backend
async function loadProducts() {
    try {
        const response = await fetch("http://127.0.0.1:8000/products");
        const products = await response.json();

        // Limpiar opciones existentes
        productSelect.innerHTML = "";

        // Llenar el select
        products.forEach(prod => {
            const option = document.createElement("option");
            option.value = prod;
            option.textContent = prod;
            productSelect.appendChild(option);
        });
    } catch (error) {
        console.error("Error al cargar productos:", error);
        alert("No se pudieron cargar los productos desde el backend");
    }
}

// Llamar a la función al cargar la página
loadProducts();

// Botón calcular
document.getElementById("calculateBtn").addEventListener("click", async () => {
    const product = productSelect.value;
    let batch_date = batchDateInput.value;

    if (!batch_date) {
        batch_date = today; // si el usuario borra la fecha
    }

    try {
        const url = `http://127.0.0.1:8000/calculate?product=${encodeURIComponent(product)}&batch_date=${batch_date}`;
        console.log(url);
        const response = await fetch(url);
        const data = await response.json();

        const resultsDiv = document.getElementById("results");

        if (data.error) {
            resultsDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
        } else {
            resultsDiv.innerHTML = `
                <p>Producto: ${data.product}</p>
                <p>Fecha de lote: ${data["batch date"]}</p>
                <p>Días hasta retirada: ${data["R days"]}</p>
                <p>Fecha de retirada: ${data["R date"]}</p>
                <p>Días hasta caducidad: ${data["expiry days"]}</p>
                <p>Fecha de caducidad: ${data["expiry date"]}</p>
            `;
        }
    } catch (error) {
        console.error(error);
        alert("Error al conectar con el backend");
    }
});
