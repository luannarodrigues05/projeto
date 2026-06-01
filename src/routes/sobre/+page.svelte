<script>
	import "../../styles/sobre.css";

	let participantes = [
		{
			nome: 'Alex Gabriel',
			cor: 'linear-gradient(135deg, #1b0505 0%, #7d1d1d 35%, #a95a28 55%, #2c0e0e 100%)'
		},
		{
			nome: 'Geany Floro',
			cor: 'linear-gradient(135deg, #1b0505 0%, #7d1d1d 35%, #a95a28 55%, #2c0e0e 100%)'
		},
		{
			nome: 'Luanna Kely',
			cor: 'linear-gradient(135deg, #1b0505 0%, #7d1d1d 35%, #a95a28 55%, #2c0e0e 100%)'
		},
		{
			nome: 'Matheus Miguel',
			cor: 'linear-gradient(135deg, #1b0505 0%, #7d1d1d 35%, #a95a28 55%, #2c0e0e 100%)'
		},
		{
			nome: 'Thiago de Oliveira',
			cor: 'linear-gradient(135deg, #1b0505 0%, #7d1d1d 35%, #a95a28 55%, #2c0e0e 100%)'
		}
	];
</script>

<div class="page">
	<div class="page-inner">
		<header class="hero">
			<span class="label">DESENVOLVEDORES</span>
			<h1>The Origin of Aether</h1>
			<p>Os duelistas que colocaram o jogo em campo, reunidos neste deck de talentos.</p>
		</header>

		<div class="container">
			{#each participantes as participante}
				<div class="card" style="background: {participante.cor}">
					<h2>{participante.nome}</h2>
				</div>
			{/each}
		</div>

		<a class="back" href="/">Voltar</a>
	</div>
</div>