<script lang="ts">
    import { goto } from '$app/navigation'

    // =========================
    // TIPOS
    // =========================

    interface Personagem {
        nome: string
        vida: number
        vidaMaxima: number
        ataque: number
        defesa: number
        habilidade: string
        elemento: string
        emoji: string
        cor: string
        pontos?: number
    }

    interface Inimigo {
        nome: string
        vida: number
        vidaMaxima: number
        ataque: number
        defesa: number
        emoji: string
        chefe?: boolean
    }

    interface EstadoJogo {
        personagemSelecionado: Personagem | null
        inimigoAtual: Inimigo | null
        fase: number
        mensagem: string
        tela: string
    }

    // =========================
    // PERSONAGENS (Máximo 5 com cores temáticas)
    // =========================

    let personagens: Personagem[] = [
        {
            nome: "Pyron",
            vida: 130,
            vidaMaxima: 130,
            ataque: 29,
            defesa: 14,
            habilidade: "Bola de Fogo",
            elemento: "Fogo",
            emoji: "🔥",
            cor: "#ff4d4d",
            pontos: 0
        },
        {
            nome: "Aquaris",
            vida: 145,
            vidaMaxima: 145,
            ataque: 26,
            defesa: 15,
            habilidade: "Onda Gigante",
            elemento: "Água",
            emoji: "🌊",
            cor: "#3399ff",
            pontos: 0
        },
        {
            nome: "Terron",
            vida: 165,
            vidaMaxima: 165,
            ataque: 22,
            defesa: 20,
            habilidade: "Impacto de Pedra",
            elemento: "Terra",
            emoji: "🪨",
            cor: "#8b5a2b",
            pontos: 0
        }
    ]

    // =========================
    // INIMIGOS (Surgem baseados na fase atual)
    // =========================

    let listaInimigosCompleta: Inimigo[] = [
        { nome: "Slime Verde", vida: 48, vidaMaxima: 48, ataque: 10, defesa: 3, emoji: "🟢" },
        { nome: "Goblin Saqueador", vida: 70, vidaMaxima: 70, ataque: 14, defesa: 5, emoji: "👹" },
        { nome: "Esqueleto Guerreiro", vida: 88, vidaMaxima: 88, ataque: 16, defesa: 7, emoji: "💀" },
        { nome: "Orco Enfurecido", vida: 105, vidaMaxima: 105, ataque: 18, defesa: 9, emoji: "🐗" },
        { nome: "Dragão Filhote (Chefe)", vida: 140, vidaMaxima: 140, ataque: 24, defesa: 10, emoji: "🐲", chefe: true },
        { nome: "Feiticeira das Sombras", vida: 118, vidaMaxima: 118, ataque: 21, defesa: 9, emoji: "🧙‍♀️" },
        { nome: "Servo de Cristal", vida: 125, vidaMaxima: 125, ataque: 20, defesa: 10, emoji: "🔷" },
        { nome: "Harpia do Vento", vida: 132, vidaMaxima: 132, ataque: 21, defesa: 10, emoji: "🐦" },
        { nome: "Guardião Flamejante", vida: 145, vidaMaxima: 145, ataque: 23, defesa: 11, emoji: "🔥" },
        { nome: "Rei das Ruínas", vida: 158, vidaMaxima: 158, ataque: 25, defesa: 12, emoji: "👑" }
    ]

    // ITENS DA LOJA
    type ItemLoja = { id: string; nome: string; descricao: string; custo: number }
    let itensLoja: ItemLoja[] = [
        { id: 'poção', nome: 'Poção de Vida', descricao: 'Restaura 50 de vida', custo: 25 },
        { id: 'poção-grande', nome: 'Poção Maior', descricao: 'Restaura 120 de vida', custo: 75 },
        { id: 'elixir-ataque', nome: 'Elixir de Ataque', descricao: 'Aumenta ataque em 5 (permanente)', custo: 55 },
    ]

    function comprar(itemId: string) {
        if (!jogo.personagemSelecionado) return
        const pontos = jogo.personagemSelecionado.pontos || 0
        const item = itensLoja.find(i => i.id === itemId)
        if (!item) return
        if (pontos < item.custo) {
            jogo.mensagem = "Moedas insuficientes para comprar este item."
            return
        }

        // aplicar efeito dos itens
        switch (item.id) {
            case 'poção':
                jogo.personagemSelecionado.vida = Math.min(jogo.personagemSelecionado.vida + 50, jogo.personagemSelecionado.vidaMaxima)
                break
            case 'poção-grande':
                jogo.personagemSelecionado.vida = Math.min(jogo.personagemSelecionado.vida + 120, jogo.personagemSelecionado.vidaMaxima)
                break
            case 'elixir-ataque':
                jogo.personagemSelecionado.ataque += 5
                break
            case 'anel-precisao':
                jogo.personagemSelecionado.ataque += 3
                break
            case 'escudo':
                jogo.personagemSelecionado.defesa += 3
                break
            case 'capa-leve':
                jogo.personagemSelecionado.defesa += 2
                break
            case 'vida-max':
                jogo.personagemSelecionado.vidaMaxima += 20
                jogo.personagemSelecionado.vida += 20
                break
            case 'amulet-vida':
                jogo.personagemSelecionado.vidaMaxima += 50
                jogo.personagemSelecionado.vida += 50
                break
        }

        jogo.personagemSelecionado.pontos = pontos - item.custo
        jogo.mensagem = `Você comprou ${item.nome}!`;
    }

    // =========================
    // ESTADO DO JOGO
    // =========================

    let jogo: EstadoJogo = {
        personagemSelecionado: null,
        inimigoAtual: null,
        fase: 1,
        mensagem: "",
        tela: "menu"
    }

    let heroiSofreDano = false
    let inimigoSofreDano = false
    let efeitoAtaque: string = ''
    let danoCausado = 0
    let danoRecebido = 0
    let logEventos: string[] = []
    let pilhaTelas: string[] = []

    // =========================
    // AÇÕES DO JOGO
    // =========================

    function escolherPersonagem(personagem: Personagem) {
        jogo.personagemSelecionado = JSON.parse(JSON.stringify(personagem));
        jogo.fase = 1;
        iniciarFase()
    }

    function iniciarFase() {
        // O inimigo muda estritamente baseado na fase (1 a 5)
        let inimigoDaFase = listaInimigosCompleta[jogo.fase - 1] || listaInimigosCompleta[0];

        jogo.inimigoAtual = JSON.parse(JSON.stringify(inimigoDaFase));
        // Se for um chefe, dar leve buff fixo para ser um adversário especial
        if (inimigoDaFase.chefe) {
            const fator = 1.1
            jogo.inimigoAtual!.vidaMaxima = Math.round(jogo.inimigoAtual!.vidaMaxima * fator)
            jogo.inimigoAtual!.vida = jogo.inimigoAtual!.vidaMaxima
            jogo.inimigoAtual!.ataque = Math.round(jogo.inimigoAtual!.ataque * fator)
            jogo.mensagem = `Fase ${jogo.fase} - Chefe ${jogo.inimigoAtual!.nome} surge mais forte!`
        } else {
            jogo.mensagem = `Fase ${jogo.fase} - Um ${jogo.inimigoAtual?.nome} bloqueia o seu caminho!`
        }
        navegarPara("mapa")
    }

    function navegarPara(novaTela: string) {
        if (jogo.tela) pilhaTelas.push(jogo.tela)
        jogo.tela = novaTela
    }

    function voltarTela() {
        if (pilhaTelas.length > 0) {
            jogo.tela = pilhaTelas.pop() as string
            jogo.mensagem = ""
        } else {
            goto('/')
        }
    }

    function atacar() {
        if (!jogo.personagemSelecionado || !jogo.inimigoAtual) return

        // Jogador ataca o inimigo
        const elemento = jogo.personagemSelecionado.elemento.toLowerCase().normalize('NFD').replace(/\p{Diacritic}/gu, '')
        efeitoAtaque = elemento
        const danoInimigo = Math.max(
            Math.round(jogo.personagemSelecionado.ataque * 1.05 - (jogo.inimigoAtual.defesa * 0.7)),
            4
        )
        jogo.inimigoAtual.vida -= danoInimigo
        jogo.inimigoAtual.vida = Math.max(0, jogo.inimigoAtual.vida)
        danoCausado = danoInimigo
        logEventos = [
            `Você causou ${danoInimigo} de dano ao ${jogo.inimigoAtual.nome}.`,
            ...logEventos.slice(0, 2)
        ]
        inimigoSofreDano = true
        setTimeout(() => inimigoSofreDano = false, 300)
        setTimeout(() => efeitoAtaque = '', 450)
        setTimeout(() => danoCausado = 0, 350)

        // Inimigo derrotado
        if (jogo.inimigoAtual.vida <= 0) {
            // conceder moedas por vitória com base na fase e força do inimigo
            const recompensa = Math.max(12, Math.round(jogo.fase * 3 + jogo.inimigoAtual.vidaMaxima / 14))
            if (typeof jogo.personagemSelecionado.pontos === 'number') {
                jogo.personagemSelecionado.pontos += recompensa
            } else {
                jogo.personagemSelecionado.pontos = recompensa
            }
            jogo.mensagem = `Você ganhou ${recompensa} moedas!`;
            if (jogo.fase >= 10) {
                navegarPara("fim")
                return
            }
            jogo.fase++
            iniciarFase()
            return
        }

        // Inimigo contra-ataca com equilíbrio entre ataque e defesa
        const danoHeroi = Math.max(
            Math.round(jogo.inimigoAtual.ataque * 0.95 - jogo.personagemSelecionado.defesa * 0.7),
            4
        );
        jogo.personagemSelecionado.vida -= danoHeroi
        danoRecebido = danoHeroi
        logEventos = [
            `O ${jogo.inimigoAtual.nome} causou ${danoHeroi} de dano a você.`,
            ...logEventos.slice(0, 2)
        ]
        heroiSofreDano = true
        setTimeout(() => heroiSofreDano = false, 300)
        setTimeout(() => danoRecebido = 0, 350)

        // Jogador derrotado
        if (jogo.personagemSelecionado.vida <= 0) {
            alert("🎯 GAME OVER! Seu herói caiu em combate.")
            reiniciarJogo()
        }
    }

    function reiniciarJogo() {
        jogo = {
            personagemSelecionado: null,
            inimigoAtual: null,
            fase: 1,
            mensagem: "",
            tela: "menu"
        }
        pilhaTelas = []
    }

    // função 'retornarMapa' removida: use `voltarTela()` para navegar ao estado anterior
</script>

<!-- LOJA -->
<!-- loja movida para baixo da arena -->

<main class="container-rpg">
    {#if jogo.tela == "menu"}
        <section class="menu-inicial">
            <h1>⚔️ RPG POR TURNOS</h1>
            <h2>Escolha seu Herói</h2>

            <div class="cartas-container">
                <div style="display:flex;justify-content:flex-start;width:100%;margin-bottom:12px;">
                    <button class="botao-voltar botao-acao" on:click={voltarTela}>⬅️ Voltar</button>
                </div>
                {#each personagens as personagem}
                    <button class="carta-heroi" style="--cor-tema: {personagem.cor}" on:click={() => escolherPersonagem(personagem)}>
                        <div class="foto-personagem {personagem.nome.toLowerCase()}">
                            <div class="foto-visor">
                                <span class="foto-emoji">{personagem.emoji}</span>
                                <div class="foto-det foto-det-1"></div>
                                <div class="foto-det foto-det-2"></div>
                            </div>
                        
                        </div>
                        <h3>{personagem.nome}</h3>
                        <div class="atributos">
                            <p>❤️ Vida: {personagem.vida}</p>
                            <p>⚔️ Ataque: {personagem.ataque}</p>
                            <p>🛡️ Defesa: {personagem.defesa}</p>
                        </div>
                        <div class="extras-cartao">
                            <span class="elemento-badge">{personagem.elemento}</span>
                            <span class="elemento-badge">{personagem.habilidade}</span>
                        </div>
                    </button>
                {/each}
            </div>
        </section>
    {/if}


    {#if jogo.tela == "mapa" && jogo.personagemSelecionado && jogo.inimigoAtual}
        <section class="tela-mapa">
            <div class="hud-mapa" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                <div>🏅 Moedas: <strong>{jogo.personagemSelecionado.pontos || 0}</strong></div>
                <div style="display:flex;gap:8px;">
                    <button class="botao-voltar botao-acao" on:click={voltarTela}>↩️ Voltar</button>
                </div>
            </div>
            <div class="mapa-trilha">
                {#each Array(10) as _, index}
                    {@const numFase = index + 1}
                    <div class="fase-no {numFase === jogo.fase ? 'atual' : ''} {numFase < jogo.fase ? 'concluida' : ''}">
                        <div class="marcador-fase">
                            {#if numFase === jogo.fase}
                                <span class="player-token">{jogo.personagemSelecionado.emoji}</span>
                            {:else if numFase == 5}
                                <span class="boss-token">👹</span>
                            {:else if numFase == 10}
                                👑
                            {:else}
                                {numFase}
                            {/if}
                        </div>
                        <span class="fase-label">Fase {numFase}</span>
                    </div>
                        {#if index < 9}
                        <div class="linha-conexao {numFase < jogo.fase ? 'ativa' : ''}"></div>
                    {/if}
                {/each}
            </div>

            <div class="caixa-mensagem">
                <p>{jogo.mensagem}</p>
                <div class="log-eventos">
                    {#each logEventos as evento}
                        <div class="item-log">{evento}</div>
                    {/each}
                </div>
            </div>

            <div class="arena-combate">
                <div class="card-combate heroi" class:sofrendo-dano={heroiSofreDano} style="border-color: {jogo.personagemSelecionado.cor}">
                    {#if danoRecebido > 0}
                        <div class="damage-pop hero">-{danoRecebido}</div>
                    {/if}
                    <span class="combate-emoji">{jogo.personagemSelecionado.emoji}</span>
                    <h3>{jogo.personagemSelecionado.nome}</h3>
                    <div class="barra-vida-container">
                        <div class="barra-vida" style="width: {(jogo.personagemSelecionado.vida / jogo.personagemSelecionado.vidaMaxima) * 100}%; background-color: {jogo.personagemSelecionado.cor}"></div>
                    </div>
                    <p>❤️ {jogo.personagemSelecionado.vida} / {jogo.personagemSelecionado.vidaMaxima}</p>
                </div>

                <div class="versus">VS</div>

                <div class="card-combate adversario" class:atingido={inimigoSofreDano}>
                    <div class="efeito-ataque {efeitoAtaque}"></div>
                    {#if danoCausado > 0}
                        <div class="damage-pop enemy">-{danoCausado}</div>
                    {/if}
                    <span class="combate-emoji">{jogo.inimigoAtual.emoji}</span>
                    <h3>{jogo.inimigoAtual.nome}</h3>
                    <div class="barra-vida-container">
                        <div class="barra-vida inimigo" style="width: {(jogo.inimigoAtual.vida / jogo.inimigoAtual.vidaMaxima) * 100}%"></div>
                    </div>
                    <p>❤️ {jogo.inimigoAtual.vida} / {jogo.inimigoAtual.vidaMaxima}</p>
                </div>
            </div>

            <div style="margin-top:16px; display:flex; gap:12px; justify-content:center;">
                <button class="botao-voltar-batalha botao-acao" on:click={voltarTela}>↩️ Voltar</button>
                <button class="botao-ataque" on:click={atacar}>
                    ⚔️ Desferir Ataque!
                </button>
            </div>
            {#if jogo.fase > 1}
                <div class="tela-loja" style="margin-top:18px;">
                    <h2>🛒 Loja Fixa</h2>
                    <p>Suas Moedas: <strong>{jogo.personagemSelecionado.pontos || 0}</strong></p>
                    <div class="itens-loja">
                        {#each itensLoja as item}
                            <div class="item-loja">
                                <h3>{item.nome}</h3>
                                <p>{item.descricao}</p>
                                <div class="custo-centro">{item.custo} pts</div>
                                <div style="display:flex;gap:8px;align-items:center;justify-content:center;margin-top:8px;">
                                    <button class="botao-acao" on:click={() => comprar(item.id)}>
                                        Comprar
                                    </button>
                                </div>
                            </div>
                        {/each}
                    </div>
                </div>
            {/if}
        </section>
    {/if}

    {#if jogo.tela == "fim"}
        <section class="tela-final">
            <div class="trofeu">🏆</div>
            <h1>PARABÉNS CORAJOSO JOGADOR!</h1>
            <p>Você superou os perigos das 10 fases e conquistou o reino!</p>
            <button class="botao-reiniciar" on:click={reiniciarJogo}>
                Jogar Novamente
            </button>
        </section>
    {/if}
</main>

<style>
    :global(body) {
        background-color: #121214;
        color: #e1e1e6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
    }

    .container-rpg {
        max-width: 900px;
        margin: 40px auto;
        padding: 20px;
        text-align: center;
    }

    h1 { color: #ffca28; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }

    /* MENU DE SELEÇÃO */
    .cartas-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 30px;
    }

    .carta-heroi {
        background: #202024;
        border: 3px solid var(--cor-tema);
        border-radius: 12px;
        padding: 20px;
        width: 200px;
        color: white;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
    }

    .botao-acao {
        background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        color: #fff;
        padding: 10px 14px;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 6px 14px rgba(0,0,0,0.45);
        transition: transform 0.14s ease, box-shadow 0.14s ease, opacity 0.12s ease;
        font-weight: 600;
    }

    .botao-acao:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.55); }
    .botao-acao:active { transform: translateY(0); opacity: 0.95 }

    .botao-ataque { background: linear-gradient(90deg,#ff7a45,#ff4d4d); border: none; }
    .botao-voltar { background: rgba(255,255,255,0.04); }
    .botao-voltar-batalha { background: rgba(0,0,0,0.45); }

    .boss-token { font-size: 1.15rem; filter: drop-shadow(0 2px 2px rgba(0,0,0,0.6)); }

    .carta-heroi:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 20px var(--cor-tema);
    }

    .emoji-avatar { font-size: 3.5rem; display: block; margin-bottom: 10px; }
    .foto-personagem {
        position: relative;
        width: 100%;
        min-height: 150px;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 18px;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding: 16px;
        color: white;
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.06);
    }
    .foto-personagem.pyron { background: radial-gradient(circle at top left, rgba(255,92,92,0.45), transparent 45%), linear-gradient(135deg, #7c1e1e, #2a0b0b); }
    .foto-personagem.aquaris { background: radial-gradient(circle at top left, rgba(89,173,255,0.35), transparent 45%), linear-gradient(135deg, #0d3f74, #071b2f); }
    .foto-personagem.terron { background: radial-gradient(circle at top left, rgba(187,142,58,0.35), transparent 45%), linear-gradient(135deg, #3f2e1a, #12110b); }

    .foto-visor {
        position: relative;
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: rgba(255,255,255,0.12);
        border: 2px solid rgba(255,255,255,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .foto-emoji {
        font-size: 3.2rem;
        z-index: 2;
        filter: drop-shadow(0 0 6px rgba(0,0,0,0.35));
    }
    .foto-det {
        position: absolute;
        border-radius: 999px;
        opacity: 0.75;
    }
    .foto-det-1 {
        width: 32px;
        height: 32px;
        bottom: 12px;
        right: 16px;
        background: rgba(255,255,255,0.25);
    }
    .foto-det-2 {
        width: 18px;
        height: 18px;
        top: 10px;
        left: 12px;
        background: rgba(255,255,255,0.18);
    }
    .foto-legenda {
        position: absolute;
        bottom: 12px;
        left: 16px;
        font-size: 0.8rem;
        color: rgba(255,255,255,0.8);
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .extras-cartao {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 14px;
    }
    .elemento-badge {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 999px;
        padding: 6px 12px;
        font-size: 0.82rem;
        color: #fafafa;
    }
    .atributos { text-align: left; background: #121214; padding: 10px; border-radius: 6px; margin: 15px 0; }
    .atributos p { margin: 5px 0; font-size: 0.95rem; }
    .habilidade-tag { background: #29292e; padding: 4px 8px; border-radius: 4px; font-size: 0.85rem; display: block; }

    /* MAPA EM LINHA (TRILHA DE 10 FASES) */
    .mapa-trilha {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #202024;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 30px;
        border: 1px solid #323238;
    }

    .fase-no {
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
    }

    .marcador-fase {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #323238;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        border: 3px solid #48484a;
        transition: all 0.3s;
        z-index: 2;
    }

    .fase-no.atual .marcador-fase {
        border-color: #ffca28;
        background: #ffca28;
        box-shadow: 0 0 15px #ffca28;
        transform: scale(1.15);
    }

    .fase-no.concluida .marcador-fase {
        border-color: #4cd964;
        background: #1e3a1e;
        color: #4cd964;
    }

    .player-token { font-size: 1.8rem; position: absolute; }
    .fase-label { font-size: 0.8rem; margin-top: 8px; color: #a8a8b3; }

    .linha-conexao {
        flex-grow: 1;
        height: 4px;
        background: #323238;
        margin: 0 -5px;
        transform: translateY(-10px);
        z-index: 1;
    }

    .linha-conexao.ativa { background: #4cd964; }

    /* ARENA DE BATALHA */
    .caixa-mensagem { background: #29292e; padding: 12px; border-radius: 8px; margin-bottom: 20px; font-weight: bold; }
    
    .arena-combate {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin: 30px 0;
    }

    .card-combate {
        background: #202024;
        padding: 20px;
        border-radius: 12px;
        width: 220px;
        border: 2px solid #323238;
    }

    .card-combate.adversario { border-color: #ff4d4d; position: relative; overflow: hidden; }
    .card-combate.atingido { animation: impacto-inimigo 0.28s ease-in-out; box-shadow: 0 0 0 8px rgba(255,77,77,0.25); }
    .card-combate.sofrendo-dano { animation: impacto-heroi 0.28s ease-in-out; box-shadow: 0 0 0 8px rgba(255,187,0,0.25); }
    .card-combate.atingido .combate-emoji,
    .card-combate.sofrendo-dano .combate-emoji { animation: pulso-hit 0.28s ease-in-out; }
    .efeito-ataque {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 180px;
        height: 180px;
        opacity: 0;
        border-radius: 50%;
        transform: translate(-50%, -50%) scale(0.4);
        pointer-events: none;
        transition: opacity 0.15s ease, transform 0.25s ease;
    }
    .efeito-ataque.fogo { background: radial-gradient(circle, rgba(255,158,70,0.75) 0%, rgba(255,59,0,0.15) 60%, transparent 90%); }
    .efeito-ataque.agua { background: radial-gradient(circle, rgba(81,169,255,0.75) 0%, rgba(80,135,255,0.18) 55%, transparent 90%); }
    .efeito-ataque.terra { background: radial-gradient(circle, rgba(180,145,80,0.75) 0%, rgba(97,66,25,0.18) 55%, transparent 90%); }
    .efeito-ataque.fogo, .efeito-ataque.agua, .efeito-ataque.terra {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
        animation: efeito-ataque 0.45s ease-out;
    }
    @keyframes efeito-ataque {
        0% { opacity: 0; transform: translate(-50%, -50%) scale(0.4); }
        40% { opacity: 1; transform: translate(-50%, -50%) scale(1.15); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(1.4); }
    }
    .damage-pop {
        position: absolute;
        top: 12px;
        left: 50%;
        transform: translateX(-50%);
        padding: 7px 14px;
        border-radius: 999px;
        font-weight: 700;
        color: #fff;
        opacity: 0;
        pointer-events: none;
        animation: dano-pop 0.4s ease-out forwards;
        z-index: 5;
    }
    .damage-pop.hero { background: rgba(255, 75, 75, 0.92); }
    .damage-pop.enemy { background: rgba(255, 196, 61, 0.92); }
    @keyframes dano-pop {
        0% { opacity: 1; transform: translate(-50%, 0) scale(1); }
        50% { opacity: 1; transform: translate(-50%, -20px) scale(1.05); }
        100% { opacity: 0; transform: translate(-50%, -32px) scale(1.1); }
    }
    .log-eventos {
        display: grid;
        gap: 6px;
        margin-top: 12px;
        text-align: left;
    }
    .item-log {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 8px 12px;
        font-size: 0.92rem;
        color: #f4f4f9;
    }
    .combate-emoji { font-size: 4rem; display: block; margin-bottom: 10px; }
    .versus { font-size: 2rem; font-weight: bold; color: #ff4d4d; font-style: italic; }

    @keyframes impacto-inimigo {
        0% { transform: translateX(0) scale(1); }
        25% { transform: translateX(-5px) scale(1.02); }
        50% { transform: translateX(5px) scale(1.04); }
        75% { transform: translateX(-3px) scale(1.02); }
        100% { transform: translateX(0) scale(1); }
    }

    @keyframes impacto-heroi {
        0% { transform: translateX(0) scale(1); }
        25% { transform: translateX(5px) scale(1.02); }
        50% { transform: translateX(-5px) scale(1.04); }
        75% { transform: translateX(3px) scale(1.02); }
        100% { transform: translateX(0) scale(1); }
    }

    @keyframes pulso-hit {
        0% { transform: scale(1); }
        50% { transform: scale(1.12); }
        100% { transform: scale(1); }
    }

    /* BARRA DE VIDA */
    .barra-vida-container {
        background: #121214;
        border-radius: 10px;
        height: 14px;
        width: 100%;
        overflow: hidden;
        margin: 10px 0;
    }
    .barra-vida { height: 100%; transition: width 0.3s ease; }
    .barra-vida.inimigo { background-color: #ff4d4d; }

    /* BOTÕES */
    .botao-ataque, .botao-reiniciar {
        background: #ffca28;
        color: #121214;
        border: none;
        padding: 15px 40px;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: background 0.2s, transform 0.1s;
    }
    .botao-ataque:hover { background: #ffe082; transform: translateY(-2px); }
    .botao-ataque:active { transform: translateY(0); }

    .tela-final .trofeu { font-size: 6rem; margin-bottom: 20px; animation: bounce 2s infinite; }

    /* LOJA */
    .tela-loja { display:flex; flex-direction:column; align-items:center; justify-content:flex-start; padding: 24px; gap: 12px; }
    .tela-loja h2 { margin: 6px 0 4px; }
    .itens-loja { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; width:100%; max-width:820px; margin-top:12px; }
    .item-loja { background: #171718; border: 1px solid #2b2b2f; padding: 16px; border-radius: 12px; text-align:center; color: #eaeaea; display:flex; flex-direction:column; justify-content:space-between; }
    .item-loja h3 { margin: 0 0 6px; }
    .item-loja p { margin: 0; color: #bdbdc2; font-size: 0.95rem }
    .tela-loja .botao-acao { padding: 10px 12px; }
    .custo-centro { margin-top:10px; font-weight:700; font-size:1rem; color:#ffd166; }
    .hud-mapa { width:100%; max-width:900px }
</style>