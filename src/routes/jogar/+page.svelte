<script lang="ts">
	import { goto } from '$app/navigation';

	// === TIPOS ===

	interface Personagem {
		nome: string;
		vida: number;
		ataque: number;
		defesa: number;
		habilidade: string;
		emoji: string;
	}

	interface Inimigo {
		nome: string;
		vida: number;
		ataque: number;
		emoji: string;
	}

	interface EstadoJogo {
		personagemSelecionado: Personagem | null;
		inimigoAtual: Inimigo | null;
		mensagem: string;
		tela: string;
	}

	// === PERSONAGENS ===

	let personagens: Personagem[] = [
		{
			nome: 'Pyron',
			vida: 100,
			ataque: 30,
			defesa: 10,
			habilidade: 'Bola de Fogo',
			emoji: '🔥'
		},
		{
			nome: 'Aquaris',
			vida: 120,
			ataque: 20,
			defesa: 15,
			habilidade: 'Onda Gigante',
			emoji: '🌊'
		},
		{
			nome: 'Terron',
			vida: 150,
			ataque: 15,
			defesa: 20,
			habilidade: 'Impacto de Pedra',
			emoji: '🪨'
		}
	];

	// === INIMIGOS ===

	let inimigos: Inimigo[] = [
		{
			nome: 'Slime',
			vida: 40,
			ataque: 10,
			emoji: '🟢'
		},
		{
			nome: 'Goblin',
			vida: 60,
			ataque: 15,
			emoji: '👹'
		},
		{
			nome: 'Esqueleto',
			vida: 80,
			ataque: 20,
			emoji: '💀'
		}
	];

	// === ESTADO DO JOGO ===

	let jogo: EstadoJogo = {
		personagemSelecionado: null,
		inimigoAtual: null,
		mensagem: '',
		tela: 'historia'
	};
</script>

<div class="content">
	<!-- HISTÓRIA -->

	{#if jogo.tela == 'historia'}
		<!-- TODO: RESOLVER GAMBIARRA -->
		<h1 style="margin-bottom: -80px;">📜 SUA HISTÓRIA 📜</h1>

		<div class="page">
			<div class="page-box">
				<p>
					Nascido na tranquila vila de Vale Lunaris, o protagonista sempre sonhou em descobrir o que
					aconteceu com seu pai, um explorador desaparecido nas antigas ruínas da região. Sua única
					pista era um diário incompleto que mencionava uma misteriosa verdade ligada ao Éter, a
					energia que sustenta o equilíbrio do mundo. <br /><br /> Quando criaturas pacíficas
					começam a agir de forma violenta, o jovem ajuda a pesquisadora Dra. Selene, que lhe
					entrega seu primeiro companheiro, Aethro. Durante sua jornada, ele descobre que os ataques
					são causados por uma corrupção do Éter e que uma organização conhecida como Ordem do
					Eclipse pode estar por trás dos acontecimentos. <br /><br /> Enquanto explora terras
					distantes, enfrenta desafios e fortalece seus laços com as criaturas, o protagonista reúne
					fragmentos de informações sobre seu pai e sobre a lendária Coroa Celestial, um reino
					perdido acima das nuvens. Dizem que esse lugar guarda a origem do Éter e as respostas para
					os mistérios que ameaçam Aetherion. <br /><br /> Agora, sua missão é alcançar a Coroa Celestial
					antes que a corrupção consuma o mundo, revelando a verdade sobre seu pai e o destino que o
					liga ao equilíbrio de toda a existência.
				</p>
			</div>

			<button type="button" id="continue" on:click={() => (jogo.tela = 'menu')}>Continuar</button>
		</div>
	{/if}

	<!-- MENU -->

	{#if jogo.tela == 'menu'}
		<h1>⚔️ THE ORIGIN OF AETHER ⚔️</h1>

		<h2>Escolha seu personagem</h2>

		<div class="cartas">
			{#each personagens as personagem}
				<div class="carta">
					<h2>{personagem.emoji}</h2>

					<h3>{personagem.nome}</h3>

					<p>❤️ Vida: {personagem.vida}</p>

					<p>⚔️ Ataque: {personagem.ataque}</p>

					<p>🛡️ Defesa: {personagem.defesa}</p>

					<p>✨ {personagem.habilidade}</p>
				</div>
			{/each}
		</div>
		<a href="/" id="back">Voltar ao menu principal</a>
	{/if}

	<!-- FINAL -->
</div>

<style>
	body {
		font-family: Arial;
		margin: 0;
	}

	.content {
		min-height: 100vh;
		background: radial-gradient(circle at top, #1e3a5f, transparent 30%),
			linear-gradient(180deg, #6ecbf5 0%, #f7c948 100%);
		background-repeat: no-repeat;
		background-size: cover;
		padding-top: 12px;
	}

	:global(body) {
		background: radial-gradient(circle at top, #1e3a5f, transparent 30%),
			linear-gradient(180deg, #6ecbf5 0%, #f7c948 100%);
		background-repeat: no-repeat;
		background-size: cover;
	}

	h1,
	h2,
	h3,
	p {
		text-align: center;
		margin: 0;
	}

	h1 {
		margin-bottom: 8px;
		color: #ffd700;
	}

	/* HISTÓRIA */

	.page {
		min-height: 100vh;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px 18px;
		background: transparent;
	}

	.page-box {
		position: relative;
		width: min(800px, 100%);
		padding: 20px 20px;
		border-radius: 40px;
		background: linear-gradient(135deg, #0b1026, #1a1f4b, #243b6b);
		border: 1px solid rgba(255, 255, 255, 0.08);
		box-shadow: 0 40px 100px rgba(0, 0, 0, 0.4);
		text-align: center;
		overflow: hidden;
	}

	button#continue, a#back {
		margin-top: 30px;
		display: inline-flex;
		justify-content: center;
		align-items: center;
		min-height: 64px;
		padding: 0 24px;
		border-radius: 22px;
		font-weight: 800;
		font-size: 1.2rem;
		letter-spacing: 0.03em;
		text-decoration: none;
		color: rgba(0, 0, 0, 0.7);
		background: #f8faff;
		box-shadow: 0 20px 40px rgba(0, 0, 0, 0.22);
		cursor: pointer;
		transition:
			transform 0.22s ease,
			box-shadow 0.22s ease,
			background 0.22s ease;
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
