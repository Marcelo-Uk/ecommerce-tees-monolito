// static/assets/js/cartoes.js
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("cardForm");
  const amountInput = document.getElementById("amount");
  const amountDisplay = document.getElementById("amountDisplay");
  const backBtn = document.getElementById("btn-back-cart");
  const submitBtn = document.getElementById("btn-submit");
  const successMsg = document.getElementById("successMessage");

  // URLs vindas do template (data-attributes)
  const VALIDATE_URL = form.dataset.validateUrl || `${window.location.origin}/api/pagamentos/validar/`;
  const SUCCESS_URL  = form.dataset.successUrl  || `${window.location.origin}/`;
  const CART_URL     = form.dataset.cartUrl     || `${window.location.origin}/carrinho/`;

  // 1) Recupera o total do carrinho
  let totalValue = localStorage.getItem("totalValue");
  if (totalValue && !isNaN(totalValue)) {
    amountInput.value = Number.parseFloat(totalValue).toFixed(2);
    amountDisplay.textContent = `R$ ${Number.parseFloat(totalValue).toFixed(2)}`;
  } else {
    amountInput.value = "0.00";
    amountDisplay.textContent = "R$ 0,00";
    console.warn("totalValue não encontrado no localStorage.");
  }

  // 2) Envio do formulário (JSON para a API do monolito)
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const numeroCartao = document.getElementById("cardNumber").value.trim();
    const nomeCartao   = document.getElementById("cardName").value.trim();
    const dataValidade = document.getElementById("cardExpiry").value.trim();  // MM/AA
    const cvv          = document.getElementById("cardCVV").value.trim();
    const tipoPagamento = document.querySelector('input[name="paymentType"]:checked')?.value;

    const valor = amountInput.value || "0.00";
    if (!tipoPagamento) {
      alert("Selecione o tipo de pagamento.");
      return;
    }
    if (!valor || isNaN(valor) || Number(valor) <= 0) {
      alert("Valor total inválido. Volte ao carrinho para recalcular.");
      return;
    }

    const payload = {
      numero_cartao: numeroCartao,
      nome_cartao: nomeCartao,
      data_validade: dataValidade,
      cvv: cvv,
      tipo_pagamento: tipoPagamento, // "debito" ou "credito"
      valor: String(valor)           // melhor para Decimal() no backend
    };

    // UX: evitar duplo clique
    submitBtn.disabled = true;
    const oldLabel = submitBtn.textContent;
    submitBtn.textContent = "Processando...";

    try {
      const response = await fetch(VALIDATE_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const result = await response.json();

      if (response.ok) {
        // Limpa carrinho e total após pagamento aprovado
        localStorage.removeItem("cart");
        localStorage.removeItem("totalValue");

        // Mostra mensagem amigável antes do redirecionamento
        if (successMsg) {
          successMsg.textContent = "Pagamento realizado com sucesso, redirecionando para a página inicial!";
          successMsg.classList.add("show");
        } else {
          // fallback
          alert("Pagamento realizado com sucesso, redirecionando para a página inicial!");
        }

        // Aguarda um tempo e redireciona para a listagem de produtos
        setTimeout(() => {
          window.location.href = SUCCESS_URL;
        }, 2200);
      } else {
        alert(result.mensagem || `Erro no pagamento (HTTP ${response.status})`);
        submitBtn.disabled = false;
        submitBtn.textContent = oldLabel;
      }
    } catch (error) {
      console.error("Erro na requisição:", error);
      alert("Ocorreu um erro ao processar o pagamento. Tente novamente.");
      submitBtn.disabled = false;
      submitBtn.textContent = oldLabel;
    }
  });

  // 3) Voltar ao carrinho
  backBtn.addEventListener("click", () => {
    window.location.href = CART_URL;
  });
});
