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

<div class="jogar-content">
	<!-- HISTÓRIA -->

	{#if jogo.tela == 'historia'}
		<!-- TODO: RESOLVER GAMBIARRA -->
		<h1 style="margin-bottom: -80px;">📜 SUA HISTÓRIA 📜</h1>

		<div class="jogar-page">
			<div class="jogar-page-box">
				<p>
					Nascido na tranquila vila de Vale Lunaris, você sempre sonhou em descobrir o que
					aconteceu com seu pai, um explorador desaparecido nas antigas ruínas da região. Sua única
					pista era um diário incompleto que mencionava uma misteriosa verdade ligada ao Éter, a
					energia que sustenta o equilíbrio do mundo. <br /><br /> Quando criaturas pacíficas
					começam a agir de forma violenta, você sai em busca de respostas e encontra sua primeira criatura 
					que irá se tornar seu fiel companheiro, chamado Aethro. 
					Durante sua jornada, você descobre que os ataques
					são causados por uma corrupção no Éter e que uma organização conhecida como Ordem do
					Eclipse pode estar por trás dos acontecimentos. <br /><br /> Enquanto explora terras
					distantes, enfrenta desafios e fortalece seus laços com as criaturas, você reúne
					fragmentos de informações sobre seu pai e sobre a lendária Coroa Celestial, um reino
					perdido acima das nuvens. Dizem que esse lugar guarda a origem do Éter e as respostas para
					os mistérios que ameaçam a existência de todos. <br /><br /> Agora, sua missão é alcançar a Coroa Celestial
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

		<div class="jogar-cartas">
			{#each personagens as personagem}
				<div class="jogar-carta">
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
