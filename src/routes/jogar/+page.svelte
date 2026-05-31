<script lang="ts">
    import { goto } from '$app/navigation'

    // === TIPOS ===

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
        mensagem: string
        tela: string
    }

    // === PERSONAGENS ===

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

    // === INIMIGOS ===

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

    // === ESTADO DO JOGO ===

    let jogo: EstadoJogo = {
        personagemSelecionado: null,
        inimigoAtual: null,
        mensagem: "",
        tela: "menu",
    }

</script>

<!-- MENU -->

{#if jogo.tela == "menu"}

<h1>⚔️ THE ORIGIN OF AETHER ⚔️</h1>

<h2>Escolha seu personagem</h2>

<div class="cartas">

    {#each personagens as personagem}

        <div
            class="carta"
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

<!-- FINAL -->

<style>

    body {
        font-family: Arial;
    }

    h1, h2, h3, p {
        text-align: center;
    }

    /*  CARTAS */

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

</style>