document.addEventListener('DOMContentLoaded', function() {
    const catalogoContainer = document.getElementById('catalogo-container');

    // URL base da API V1
    const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/';

    // Função para buscar os filmes
    fetch(`${API_BASE_URL}filmes/`)
        .then(response => response.json())
        .then(filmes => {
            // Para cada filme, cria um card e busca suas avaliações
            filmes.forEach(filme => {
                const filmeCard = document.createElement('div');
                filmeCard.classList.add('filme-card');
                filmeCard.innerHTML = `
                    <h2>${filme.titulo}</h2>
                    <p><strong>URL:</strong> <a href="${filme.url}" target="_blank">${filme.url}</a></p>
                    <div class="avaliacoes-list" id="avaliacoes-filme-${filme.id}">
                        <h3>Avaliações:</h3>
                        </div>
                `;
                catalogoContainer.appendChild(filmeCard);

                // Agora, busca as avaliações para este filme específico
                fetch(`${API_BASE_URL}filmes/${filme.id}/avaliacoes/`)
                    .then(response => response.json())
                    .then(avaliacoes => {
                        const avaliacoesList = document.getElementById(`avaliacoes-filme-${filme.id}`);
                        if (avaliacoes.length > 0) {
                            avaliacoes.forEach(avaliacao => {
                                const avaliacaoDiv = document.createElement('div');
                                avaliacaoDiv.classList.add('avaliacao');
                                avaliacaoDiv.innerHTML = `
                                    <h4>${avaliacao.nome} - Nota: ${avaliacao.avaliacao}</h4>
                                    <p>${avaliacao.comentario}</p>
                                `;
                                avaliacoesList.appendChild(avaliacaoDiv);
                            });
                        } else {
                            avaliacoesList.innerHTML += '<p>Ainda não há avaliações para este filme.</p>';
                        }
                    })
                    .catch(error => console.error(`Erro ao buscar avaliações para o filme ${filme.id}:`, error));
            });
        })
        .catch(error => console.error('Erro ao buscar filmes:', error));
});