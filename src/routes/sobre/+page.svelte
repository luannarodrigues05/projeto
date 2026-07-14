<script lang="ts">
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
  @import '../../styles/sobre.css';
</style>
