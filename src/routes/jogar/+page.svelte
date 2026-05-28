<script lang="ts">
    import { goto } from '$app/navigation'

    // =========================
    // TIPOS
    // =========================

    interface Personagem {
        nome: string
        vida: number
        ataque: number
        defesa: number
        habilidade: string
        emoji: string
    }

    interface Inimigo {
        nome: string
        vida: number
        ataque: number
        emoji: string
    }

    interface EstadoJogo {
        personagemSelecionado: Personagem | null
        inimigoAtual: Inimigo | null
        fase: number
        mensagem: string
        tela: string
        mapa: number[][]
    }

    // =========================
    // PERSONAGENS
    // =========================

    let personagens: Personagem[] = [
        {
            nome: "Pyron",
            vida: 100,
            ataque: 30,
            defesa: 10,
            habilidade: "Bola de Fogo",
            emoji: "🔥"
        },
        {
            nome: "Aquaris",
            vida: 120,
            ataque: 20,
            defesa: 15,
            habilidade: "Onda Gigante",
            emoji: "🌊"
        },
        {
            nome: "Terron",
            vida: 150,
            ataque: 15,
            defesa: 20,
            habilidade: "Impacto de Pedra",
            emoji: "🪨"
        }
    ]

    // =========================
    // INIMIGOS
    // =========================

    let inimigos: Inimigo[] = [
        {
            nome: "Slime",
            vida: 40,
            ataque: 10,
            emoji: "🟢"
        },
        {
            nome: "Goblin",
            vida: 60,
            ataque: 15,
            emoji: "👹"
        },
        {
            nome: "Esqueleto",
            vida: 80,
            ataque: 20,
            emoji: "💀"
        }
    ]

    // =========================
    // MAPA
    // =========================

    function criarMapa(): number[][] {
        return [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    }

    // =========================
    // ESTADO DO JOGO
    // =========================

    let jogo: EstadoJogo = {
        personagemSelecionado: null,
        inimigoAtual: null,
        fase: 1,
        mensagem: "",
        tela: "menu",
        mapa: criarMapa()
    }

    // =========================
    // ESCOLHER PERSONAGEM
    // =========================

    function escolherPersonagem(personagem: Personagem) {
        jogo.personagemSelecionado = {
            ...personagem
        }

        iniciarFase()
    }

    // =========================
    // INICIAR FASE
    // =========================

    function iniciarFase() {
        let inimigoAleatorio =
            inimigos[Math.floor(Math.random() * inimigos.length)]

        jogo.inimigoAtual = {
            ...inimigoAleatorio
        }

        jogo.tela = "mapa"

        jogo.mensagem =
            "Fase " + jogo.fase + " - Um inimigo apareceu!"
    }

    // =========================
    // ATAQUE
    // =========================

    function atacar() {

        if (!jogo.personagemSelecionado || !jogo.inimigoAtual) {
            return
        }

        // jogador ataca
        jogo.inimigoAtual.vida -=
            jogo.personagemSelecionado.ataque

        // inimigo morreu
        if (jogo.inimigoAtual.vida <= 0) {

            if (jogo.fase >= 5) {
                jogo.tela = "fim"
                return
            }

            jogo.fase++
            jogo.mensagem = "Você venceu a fase!"
            iniciarFase()
            return
        }

        // inimigo ataca
        jogo.personagemSelecionado.vida -=
            Math.max(
                jogo.inimigoAtual.ataque -
                jogo.personagemSelecionado.defesa,
                5
            )

        // jogador perdeu
        if (jogo.personagemSelecionado.vida <= 0) {
            alert("GAME OVER")
            reiniciarJogo()
        }
    }

    // =========================
    // REINICIAR
    // =========================

    function reiniciarJogo() {

        jogo = {
            personagemSelecionado: null,
            inimigoAtual: null,
            fase: 1,
            mensagem: "",
            tela: "menu",
            mapa: criarMapa()
        }
    }
</script>

<!-- ========================= -->
<!-- MENU -->
<!-- ========================= -->

{#if jogo.tela == "menu"}

<h1>⚔️ RPG POR TURNOS</h1>

<h2>Escolha seu personagem</h2>

<div class="cartas">

    {#each personagens as personagem}

        <div
            class="carta"
            on:click={() => escolherPersonagem(personagem)}
        >
            <h2>{personagem.emoji}</h2>

            <h3>{personagem.nome}</h3>

            <p>❤️ Vida: {personagem.vida}</p>

            <p>⚔️ Ataque: {personagem.ataque}</p>

            <p>🛡️ Defesa: {personagem.defesa}</p>

            <p>✨ {personagem.habilidade}</p>
        </div>

    {/each}

</div>

{/if}

<!-- ========================= -->
<!-- MAPA -->
<!-- ========================= -->

{#if jogo.tela == "mapa"}

<h1>🗺️ Fase {jogo.fase}</h1>

<p>{jogo.mensagem}</p>

<table>

    {#each jogo.mapa as linha, i}

        <tr>

            {#each linha as celula, j}

                {#if i == 4 && j == 4}

                    <td class="objetivo"></td>

                {:else if celula == 1}

                    <td class="parede"></td>

                {:else}

                    <td class="caminho"></td>

                {/if}

            {/each}

        </tr>

    {/each}

</table>

<br>

<div class="batalha">

    <div class="status">

        <h2>
            {jogo.personagemSelecionado?.emoji}
            {jogo.personagemSelecionado?.nome}
        </h2>

        <p>
            ❤️ Vida:
            {jogo.personagemSelecionado?.vida}
        </p>

    </div>

    <div class="status">

        <h2>
            {jogo.inimigoAtual?.emoji}
            {jogo.inimigoAtual?.nome}
        </h2>

        <p>
            ❤️ Vida:
            {jogo.inimigoAtual?.vida}
        </p>

    </div>

</div>

<button on:click={atacar}>
    ⚔️ Atacar
</button>

{/if}

<!-- ========================= -->
<!-- FINAL -->
<!-- ========================= -->

{#if jogo.tela == "fim"}

<h1>🏆 PARABÉNS!</h1>

<p>
    Você completou as 5 fases do jogo!
</p>

<button on:click={reiniciarJogo}>
    Jogar Novamente
</button>

{/if}

<style>

    body {
        font-family: Arial;
    }

    h1, h2, h3, p {
        text-align: center;
    }

    /* ========================= */
    /* CARTAS */
    /* ========================= */

    .cartas {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin-top: 30px;
        flex-wrap: wrap;
    }

    .carta {
        width: 220px;
        border: 3px solid black;
        border-radius: 10px;
        padding: 15px;
        cursor: pointer;
        background-color: #0a0648;
        transition: 0.2s;
    }

    .carta:hover {
        transform: scale(1.05);
        background-color: #d2aeae;
    }

    /* ========================= */
    /* MAPA */
    /* ========================= */

    table {
        margin: auto;
        border-collapse: collapse;
        margin-top: 20px;
    }

    td {
        width: 50px;
        height: 50px;
        border: 1px solid black;
    }

    .caminho {
        background-color: white;
    }

    .parede {
        background-color: black;
    }

    .objetivo {
        background-color: purple;
    }

    /* ========================= */
    /* BATALHA */
    /* ========================= */

    .batalha {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 30px;
    }

    .status {
        border: 2px solid black;
        padding: 20px;
        width: 200px;
        text-align: center;
        border-radius: 10px;
    }

    button {
        display: block;
        margin: auto;
        margin-top: 20px;
        padding: 15px 25px;
        font-size: 18px;
        cursor: pointer;
    }

</style>