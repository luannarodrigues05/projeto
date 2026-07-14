<script lang="ts">
	import { goto } from '$app/navigation';

	interface Personagem {
		nome: string;
		vida: number;
		vidaMaxima: number;
		ataque: number;
		defesa: number;
		habilidade: string;
		elemento: string;
		emoji: string;
		cor: string;
		pontos?: number;
	}

	interface Inimigo {
		nome: string;
		vida: number;
		vidaMaxima: number;
		ataque: number;
		defesa: number;
		emoji: string;
		chefe?: boolean;
	}

	interface EstadoJogo {
		personagemSelecionado: Personagem | null;
		inimigoAtual: Inimigo | null;
		fase: number;
		mensagem: string;
		tela: string;
	}

	type Ataque = {
		nome: string;
		emoji: string;
		multiplicador: number;
		descricao: string;
	};

	let personagens: Personagem[] = [
		{
			nome: 'Fogo',
			vida: 160,
			vidaMaxima: 160,
			ataque: 39,
			defesa: 14,
			habilidade: 'Bola de Fogo',
			elemento: 'Fogo',
			emoji: '🔥',
			cor: '#FF0000',
			pontos: 0
		},
		{
			nome: 'Água',
			vida: 150,
			vidaMaxima: 150,
			ataque: 26,
			defesa: 15,
			habilidade: 'Onda Gigante',
			elemento: 'Água',
			emoji: '🌊',
			cor: '#3399ff',
			pontos: 0
		},
		{
			nome: 'Terra',
			vida: 145,
			vidaMaxima: 145,
			ataque: 22,
			defesa: 20,
			habilidade: 'Impacto de Pedra',
			elemento: 'Terra',
			emoji: '🪨',
			cor: '#964B00',
			pontos: 0
		},
        {
			nome: 'Ar',
			vida: 140,
			vidaMaxima: 140,
			ataque: 25,
			defesa: 19,
			habilidade: 'Tornado de Vento',
			elemento: 'Ar',
			emoji: '💨',
			cor: '#FFFFFF',
			pontos: 0
		}
	];

	let listaInimigosCompleta: Inimigo[] = [
		{ nome: 'Slime Verde', vida: 48, vidaMaxima: 48, ataque: 10, defesa: 3, emoji: '🟢' },
		{ nome: 'Goblin Saqueador', vida: 70, vidaMaxima: 70, ataque: 14, defesa: 5, emoji: '👹' },
		{ nome: 'Esqueleto Guerreiro', vida: 88, vidaMaxima: 88, ataque: 16, defesa: 7, emoji: '💀' },
		{ nome: 'Orco Enfurecido', vida: 105, vidaMaxima: 105, ataque: 18, defesa: 9, emoji: '🐗' },
		{ nome: 'Dragão Filhote (Chefe)', vida: 140, vidaMaxima: 140, ataque: 24, defesa: 10, emoji: '🐲', chefe: true},
		{ nome: 'Feiticeira das Sombras', vida: 118, vidaMaxima: 118, ataque: 21, defesa: 9, emoji: '🧙‍♀️'},
		{ nome: 'Servo de Cristal', vida: 125, vidaMaxima: 125, ataque: 20, defesa: 10, emoji: '🔷' },
		{ nome: 'Harpia do Vento', vida: 132, vidaMaxima: 132, ataque: 21, defesa: 10, emoji: '🐦' },
		{ nome: 'Guardião Flamejante', vida: 145, vidaMaxima: 145, ataque: 23, defesa: 11, emoji: '🔥'},
		{ nome: 'Rei das Ruínas (Chefe)', vida: 158, vidaMaxima: 158, ataque: 25, defesa: 12, emoji: '👑', chefe: true}
	];

	type ItemLoja = { id: string; nome: string; descricao: string; custo: number };
	let itensLoja: ItemLoja[] = [
		{ id: 'poção', nome: 'Poção de Vida', descricao: 'Restaura 50 de vida', custo: 25 },
		{ id: 'poção-grande', nome: 'Poção Maior', descricao: 'Restaura 120 de vida', custo: 75 },
		{
			id: 'elixir-ataque',
			nome: 'Elixir de Ataque',
			descricao: 'Aumenta ataque em 5 (permanente)',
			custo: 55
		}
	];

	function comprar(itemId: string) {
		if (!jogo.personagemSelecionado) return;
		const pontos = jogo.personagemSelecionado.pontos || 0;
		const item = itensLoja.find((i) => i.id === itemId);
		if (!item) return;
		if (pontos < item.custo) {
			jogo.mensagem = 'Moedas insuficientes para comprar este item.';
			return;
		}

		switch (item.id) {
			case 'poção':
				jogo.personagemSelecionado.vida = Math.min(
					jogo.personagemSelecionado.vida + 50,
					jogo.personagemSelecionado.vidaMaxima
				);
				break;
			case 'poção-grande':
				jogo.personagemSelecionado.vida = Math.min(
					jogo.personagemSelecionado.vida + 120,
					jogo.personagemSelecionado.vidaMaxima
				);
				break;
			case 'elixir-ataque':
				jogo.personagemSelecionado.ataque += 5;
				break;
			case 'anel-precisao':
				jogo.personagemSelecionado.ataque += 3;
				break;
			case 'escudo':
				jogo.personagemSelecionado.defesa += 3;
				break;
			case 'capa-leve':
				jogo.personagemSelecionado.defesa += 2;
				break;
			case 'vida-max':
				jogo.personagemSelecionado.vidaMaxima += 20;
				jogo.personagemSelecionado.vida += 20;
				break;
			case 'amulet-vida':
				jogo.personagemSelecionado.vidaMaxima += 50;
				jogo.personagemSelecionado.vida += 50;
				break;
		}

		jogo.personagemSelecionado.pontos = pontos - item.custo;
		jogo.mensagem = `Você comprou ${item.nome}!`;
	}

	let jogo: EstadoJogo = {
		personagemSelecionado: null,
		inimigoAtual: null,
		fase: 1,
		mensagem: '',
		tela: 'historia'
	};

	let heroiSofreDano = false;
	let inimigoSofreDano = false;
	let efeitoAtaque: string = '';
	let danoCausado = 0;
	let danoRecebido = 0;
	let logEventos: string[] = [];
	let pilhaTelas: string[] = [];
	const LIMITE_ATAQUES_ESPECIAIS = 3;
	let usosAtaquesEspeciais: Record<string, number> = {
		'Poder Especial': 0,
		'Golpe Elemental': 0
	};
	let ataquesDisponiveis: Ataque[] = [
		{ nome: 'Soco', emoji: '👊', multiplicador: 1.0, descricao: 'Ataque direto e estável' },
		{ nome: 'Chute', emoji: '🥊', multiplicador: 1.12, descricao: 'Golpe mais forte' },
		{ nome: 'Poder Especial', emoji: '✨', multiplicador: 1.35, descricao: 'Ataque devastador' },
		{ nome: 'Golpe Elemental', emoji: '⚡', multiplicador: 1.2, descricao: 'Ataque com poder do elemento' }
	];

	function ataqueEspecialAtingiuLimite(ataqueNome: string): boolean {
		if (ataqueNome !== 'Poder Especial' && ataqueNome !== 'Golpe Elemental') return false;
		return (usosAtaquesEspeciais[ataqueNome] ?? 0) >= LIMITE_ATAQUES_ESPECIAIS;
	}

	function restanteAtaqueEspecial(ataqueNome: string): number {
		if (ataqueNome !== 'Poder Especial' && ataqueNome !== 'Golpe Elemental') return 0;
		return LIMITE_ATAQUES_ESPECIAIS - (usosAtaquesEspeciais[ataqueNome] ?? 0);
	}

	function escolherPersonagem(personagem: Personagem) {
		jogo.personagemSelecionado = JSON.parse(JSON.stringify(personagem));
		jogo.fase = 1;
		logEventos = [];
		usosAtaquesEspeciais = {
			'Poder Especial': 0,
			'Golpe Elemental': 0
		};
		iniciarFase();
	}

	function iniciarFase() {
		// O inimigo muda estritamente baseado na fase (1 a 5)
		let inimigoDaFase = listaInimigosCompleta[jogo.fase - 1] || listaInimigosCompleta[0];

		jogo.inimigoAtual = JSON.parse(JSON.stringify(inimigoDaFase));
		// Se for um chefe, dar leve buff fixo para ser um adversário especial
		if (inimigoDaFase.chefe) {
			const fator = 1.1;
			jogo.inimigoAtual!.vidaMaxima = Math.round(jogo.inimigoAtual!.vidaMaxima * fator);
			jogo.inimigoAtual!.vida = jogo.inimigoAtual!.vidaMaxima;
			jogo.inimigoAtual!.ataque = Math.round(jogo.inimigoAtual!.ataque * fator);
			jogo.mensagem = `Fase ${jogo.fase} - Chefe ${jogo.inimigoAtual!.nome} surge mais forte!`;
		} else {
			jogo.mensagem = `Fase ${jogo.fase} - Um ${jogo.inimigoAtual?.nome} bloqueia o seu caminho!`;
		}
		navegarPara('mapa');
	}

	function navegarPara(novaTela: string) {
		if (jogo.tela) pilhaTelas.push(jogo.tela);
		jogo.tela = novaTela;
	}

	function voltarTela() {
		if (pilhaTelas.length > 0) {
			jogo.tela = pilhaTelas.pop() as string;
			jogo.mensagem = '';
		} else {
			goto('/');
		}
	}

	function irParaHome() {
		goto('/');
	}

	function atacar(tipoAtaque: string = 'Soco') {
		if (!jogo.personagemSelecionado || !jogo.inimigoAtual) return;

		const ataque =
			ataquesDisponiveis.find((item) => item.nome === tipoAtaque) ?? ataquesDisponiveis[0];

		if (ataqueEspecialAtingiuLimite(ataque.nome)) {
			jogo.mensagem = `${ataque.nome} já foi usado ${LIMITE_ATAQUES_ESPECIAIS} vezes nesta partida.`;
			return;
		}

		if (ataque.nome === 'Poder Especial' || ataque.nome === 'Golpe Elemental') {
			usosAtaquesEspeciais = {
				...usosAtaquesEspeciais,
				[ataque.nome]: (usosAtaquesEspeciais[ataque.nome] ?? 0) + 1
			};
		}

		const elemento = jogo.personagemSelecionado.elemento
			.toLowerCase()
			.normalize('NFD')
			.replace(/\p{Diacritic}/gu, '');
		efeitoAtaque = elemento;
		const danoInimigo = Math.max(
			Math.round(
				jogo.personagemSelecionado.ataque * (1.05 + ataque.multiplicador * 0.1) -
					jogo.inimigoAtual.defesa * 0.7
			),
			4
		);
		jogo.inimigoAtual.vida -= danoInimigo;
		jogo.inimigoAtual.vida = Math.max(0, jogo.inimigoAtual.vida);
		danoCausado = danoInimigo;
		jogo.mensagem = `${jogo.personagemSelecionado.nome} usou ${ataque.nome}!`;
		logEventos = [
			`${jogo.personagemSelecionado.nome} usou ${ataque.nome} e causou ${danoInimigo} de dano ao ${jogo.inimigoAtual.nome}.`,
			...logEventos.slice(0, 2)
		];
		inimigoSofreDano = true;
		setTimeout(() => (inimigoSofreDano = false), 300);
		setTimeout(() => (efeitoAtaque = ''), 450);
		setTimeout(() => (danoCausado = 0), 350);

		if (jogo.inimigoAtual.vida <= 0) {
			const recompensa = Math.max(
				12,
				Math.round(jogo.fase * 3 + jogo.inimigoAtual.vidaMaxima / 14)
			);
			if (typeof jogo.personagemSelecionado.pontos === 'number') {
				jogo.personagemSelecionado.pontos += recompensa;
			} else {
				jogo.personagemSelecionado.pontos = recompensa;
			}
			jogo.mensagem = `Você ganhou ${recompensa} moedas!`;
			if (jogo.fase >= 10) {
				navegarPara('fim');
				return;
			}
			jogo.fase++;
			iniciarFase();
			return;
		}

		const danoHeroi = Math.max(
			Math.round(jogo.inimigoAtual.ataque * 0.95 - jogo.personagemSelecionado.defesa * 0.7),
			4
		);
		jogo.personagemSelecionado.vida -= danoHeroi;
		danoRecebido = danoHeroi;
		logEventos = [
			`O ${jogo.inimigoAtual.nome} causou ${danoHeroi} de dano a você.`,
			...logEventos.slice(0, 2)
		];
		heroiSofreDano = true;
		setTimeout(() => (heroiSofreDano = false), 300);
		setTimeout(() => (danoRecebido = 0), 350);

		// Jogador derrotado
		if (jogo.personagemSelecionado.vida <= 0) {
			alert('🎯 GAME OVER! Seu herói caiu em combate.');
			reiniciarJogo();
		}
	}

	function reiniciarJogo() {
		jogo = {
			personagemSelecionado: null,
			inimigoAtual: null,
			fase: 1,
			mensagem: '',
			tela: 'menu'
		};
		pilhaTelas = [];
		logEventos = [];
		usosAtaquesEspeciais = {
			'Poder Especial': 0,
			'Golpe Elemental': 0
		};
	}

</script>

<main class="container-rpg">
	{#if jogo.tela == 'historia'}
		<div id="story-screen" class="hidden">
			<div class="story-content">
				<h1>O começo da odisseia</h1>
				<p>
					Você desperta em um mundo de fantasia, onde humanos e monstros dominam os
					poderes da água, terra, fogo e ar. Uma antiga ameaça coloca todo o reino de Helium em risco e apenas
					você pode mudar esse destino. Escolha um elemento para despertar seu poder e enfrentar
					inimigos lendários. <br /> Cada batalha aproxima você da salvação ou da ruína do mundo. Fortaleça
					suas habilidades, conquiste os Reinos Elementais em cada fase e decida o futuro de Helium!
				</p>
				<nav id="story-actions">
					<button
						on:click={() => {
							jogo.tela = 'menu';
						}}
						id="story-continue">Continuar</button
					>
					<a id="story-voltar" href="/">Voltar</a>
				</nav>
			</div>
		</div>
	{/if}

	{#if jogo.tela == 'menu'}
		<section class="menu-inicial">
			<h1>
				Os reinos estão em colapso.
				<p></p>
				O despertar começou.
			</h1>
			<h2>Escolha seu elemento</h2>

			<div class="cartas-container">
				{#each personagens as personagem}
					<button
						class="carta-heroi"
						style="--cor-tema: {personagem.cor}"
						on:click={() => escolherPersonagem(personagem)}
					>
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
			<div class="botao-voltar-wrapper">
				<button class="botao-voltar botao-acao" on:click={voltarTela}>Voltar</button>
			</div>
		</section>
	{/if}

	{#if jogo.tela == 'mapa' && jogo.personagemSelecionado && jogo.inimigoAtual}
		<section class="tela-mapa">
			<div
				class="hud-mapa"
				style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;"
			>
				<div>🏅 Moedas: <strong>{jogo.personagemSelecionado.pontos || 0}</strong></div>
			</div>
			<div class="conteudo-batalha">
				<div class="conteudo-principal">
					<div class="mapa-trilha">
						{#each Array(10) as _, index}
							{@const numFase = index + 1}
							<div
								class="fase-no {numFase === jogo.fase ? 'atual' : ''} {numFase < jogo.fase
									? 'concluida'
									: ''}"
							>
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
						<div
							class="card-combate heroi"
							class:sofrendo-dano={heroiSofreDano}
							style="border-color: {jogo.personagemSelecionado.cor}"
						>
							{#if danoRecebido > 0}
								<div class="damage-pop hero">-{danoRecebido}</div>
							{/if}
							<span class="combate-emoji">{jogo.personagemSelecionado.emoji}</span>
							<h3>{jogo.personagemSelecionado.nome}</h3>
							<div class="barra-vida-container">
								<div
									class="barra-vida"
									style="width: {(jogo.personagemSelecionado.vida /
										jogo.personagemSelecionado.vidaMaxima) *
										100}%; background-color: {jogo.personagemSelecionado.cor}"
								></div>
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
								<div
									class="barra-vida inimigo"
									style="width: {(jogo.inimigoAtual.vida / jogo.inimigoAtual.vidaMaxima) * 100}%"
								></div>
							</div>
							<p>❤️ {jogo.inimigoAtual.vida} / {jogo.inimigoAtual.vidaMaxima}</p>
						</div>
					</div>

					<div class="acoes-batalha">
						<p class="titulo-ataques">Escolha seu ataque</p>
						<div class="grupo-ataques">
							{#each ataquesDisponiveis as ataque}
								<button
									class="botao-ataque-opcao"
									on:click={() => atacar(ataque.nome)}
									disabled={ataqueEspecialAtingiuLimite(ataque.nome)}
								>
									<span class="emoji-ataque">{ataque.emoji}</span>
									<strong>{ataque.nome}</strong>
									<small>{ataque.descricao}</small>
									{#if ataque.nome === 'Poder Especial' || ataque.nome === 'Golpe Elemental'}
										<small>
											{ataqueEspecialAtingiuLimite(ataque.nome)
												? 'Limite atingido'
												: `${restanteAtaqueEspecial(ataque.nome)} restante(s)`}
										</small>
									{/if}
								</button>
							{/each}
						</div>
						<div class="grupo-botoes-secundarios">
							<button class="botao-voltar-batalha botao-acao" on:click={voltarTela}>Voltar</button>
							<button class="botao-voltar-batalha botao-acao" on:click={irParaHome}>Home</button>
						</div>
					</div>
				</div>

				{#if jogo.fase > 1}
					<aside class="tela-loja">
						<h2>🛒 Loja Fixa</h2>
						<p>Suas Moedas: <strong>{jogo.personagemSelecionado.pontos || 0}</strong></p>
						<div class="itens-loja">
							{#each itensLoja as item}
								<div class="item-loja">
									<h3>{item.nome}</h3>
									<p>{item.descricao}</p>
									<div class="custo-centro">{item.custo} pts</div>
									<div class="acoes-loja">
										<button class="botao-acao" on:click={() => comprar(item.id)}> Comprar </button>
									</div>
								</div>
							{/each}
						</div>
					</aside>
				{/if}
			</div>
		</section>
	{/if}

	{#if jogo.tela == 'fim'}
		<section class="tela-final">
			<div class="trofeu">🏆</div>
			<h1>PARABÉNS!</h1>
			<p>Você superou os perigos, conquistou os reinos e salvou o mundo!</p>
			<button class="botao-reiniciar" on:click={reiniciarJogo} style="margin-top: 1rem;">
				Jogar Novamente
			</button>
		</section>
	{/if}
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&display=swap');
	@import '../../styles/jogar.css';
</style>
