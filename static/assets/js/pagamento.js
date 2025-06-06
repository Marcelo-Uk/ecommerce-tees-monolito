// Simulação de valor total vindo do carrinho (isso será substituído pelo backend/microserviço no futuro)
const totalValue = localStorage.getItem("totalValue") || "0.00";

// Atualiza o valor total na tela
document.addEventListener("DOMContentLoaded", () => {
    const totalValueElement = document.getElementById("total-value");
    if (totalValueElement) {
        totalValueElement.textContent = `Valor Total: R$ ${parseFloat(totalValue).toFixed(2)}`;
    }

    // Botão "Voltar para Produtos"
    const btnBackProd = document.getElementById("btn-back-prod");
    if (btnBackProd) {
        btnBackProd.addEventListener("click", () => {
            window.location.href = "/products/"; // Redirect to Django URL path
        });
    }

    // Botão "Voltar para Carrinho"
    const btnBackCart = document.getElementById("btn-back-cart");
    if (btnBackCart) {
        btnBackCart.addEventListener("click", () => {
            window.location.href = "/carrinho/"; // Redirect to Django URL path
        });
    }

    // Botão "Pagar"
    const btnPay = document.getElementById("btn-pay");
    if (btnPay) {
        btnPay.addEventListener("click", () => {
            window.location.href = "/cartoes/"; // Redirect to Django URL path
        });
    }
});

