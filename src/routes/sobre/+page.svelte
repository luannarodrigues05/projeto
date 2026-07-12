<script lang="ts">
    // Lista simplificada apenas com os nomes
    const desenvolvedores: string[] = [
        'Alex Gabriel',
        'Geany Floro',
        'Luanna Kely',
        'Matheus Miguel',
        'Thiago de Oliveira'
    ];
</script>

<div class="sobre-page">
    <div class="content">
        <h1 id="desenvolvedores-h1">DESENVOLVEDORES</h1>

        <div class="lista-nomes">
            {#each desenvolvedores as nome}
                <div class="nome-card">
                    {nome}
                </div>
            {/each}
        </div>

        <a class="btn-voltar" href="/">Voltar</a> 
    </div>
</div>

<style>
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
}

.sobre-page {
    width: 100vw;
    height: 100vh;
    /* Aplica sua imagem como plano de fundo */
    background-image: url('images/background.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
}

.content {
    background: rgba(0, 0, 0, 0.5); /* Leve escurecimento para melhorar leitura */
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    backdrop-filter: blur(5px); /* Efeito de vidro fosco opcional */
}

h1 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.lista-nomes {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 2rem;
}

.nome-card {
    font-size: 1.2rem;
    padding: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-voltar {
    display: inline-block;
    padding: 10px 20px;
    background: #5a2828;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s;
}

.btn-voltar:hover {
    background: #7d1d1d;
}

#desenvolvedores-h1 {
    font-family: sans-serif;
}
</style> 
