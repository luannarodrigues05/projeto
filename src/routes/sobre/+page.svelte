<script>
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

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		min-height: 100vh;
		font-family:
			Inter,
			system-ui,
			-apple-system,
			BlinkMacSystemFont,
			'Segoe UI',
			sans-serif;
		background: #070307;
		color: #f5e3b0;
	}

	.page {
		min-height: 100vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 18px 14px;
		background: radial-gradient(circle at top, #1e3a5f, transparent 30%),
			linear-gradient(180deg, #6ecbf5 0%, #f7c948 100%);
		background-size: cover;
		background-position: center;
	}

	.page-inner {
		position: relative;
		width: min(860px, 100%);
		padding: 32px 28px;
		border-radius: 36px;
		background: linear-gradient(135deg, #0b1026, #1a1f4b, #243b6b);
		border: 1px solid rgba(255, 255, 255, 0.08);
		box-shadow: 0 35px 90px rgba(0, 0, 0, 0.44);
		display: flex;
		flex-direction: column;
		align-items: center;
		overflow: hidden;
	}

	.page-inner::before {
		content: '';
		position: absolute;
		inset: -30px;
		background: radial-gradient(circle at top, rgba(195, 95, 50, 0.12), transparent 44%);
		pointer-events: none;
	}

	.hero {
		text-align: center;
		margin-bottom: 28px;
		position: relative;
	}

	.hero::after {
		content: '';
		display: block;
		margin: 20px auto 0;
		width: 64px;
		height: 2px;
		background: rgba(245, 215, 142, 0.35);
		border-radius: 999px;
	}

	.label {
		display: inline-flex;
		margin-bottom: 14px;
		color: #F8FAFF;
		letter-spacing: 0.35em;
		text-transform: uppercase;
		font-size: 0.78rem;
		opacity: 0.95;
	}

	.hero h1 {
		margin: 0;
		font-size: clamp(2.75rem, 4vw, 4.25rem);
		color: #FFD700;
		text-shadow: 0 10px 26px rgba(0, 0, 0, 0.25);
	}

	.hero p {
		margin: 18px auto 0;
		max-width: 680px;
		color: #F8FAFF;
		line-height: 1.85;
		font-size: 1rem;
	}

	.container {
		display: grid;
		gap: 14px;
		width: 100%;
		max-width: 820px;
	}

	.card {
		position: relative;
		width: 100%;
		min-height: 60px;
		padding: 0 24px;
		border-radius: 24px;
		display: flex;
		justify-content: center;
		align-items: center;
		overflow: hidden;
		box-shadow:
			inset 0 0 0 1px rgba(255, 255, 255, 0.05),
			0 22px 52px rgba(0, 0, 0, 0.24);
		transition:
			transform 0.25s ease,
			filter 0.25s ease,
			box-shadow 0.25s ease;
	}

	.card::before {
		content: '';
		position: absolute;
		inset: 0;
		background: #F8FAFF;
		pointer-events: none;
	}

	.card:hover {
		transform: translateY(-6px) scale(1.005);
		filter: brightness(1.08);
		box-shadow:
			inset 0 0 0 1px rgba(255, 255, 255, 0.08),
			0 32px 72px rgba(0, 0, 0, 0.32);
	}

	.card h2 {
		position: relative;
		margin: 0;
		font-size: clamp(1.5rem, 1.8vw, 2.6rem);
		color: rgba(0,0,0,0.7);
		background: linear-gradient(135deg, #f5d78e, #ffd38a 45%, #f5d78e);
		-webkit-background-clip: text;
		background-clip: text;
		text-shadow: 0 2px 8px rgba(0, 0, 0, 0.22);
	}

	.back {
		display: inline-flex;
		justify-content: center;
		align-items: center;
		margin: 36px auto 0;
		padding: 16px 42px;
		border-radius: 24px;
		background: #F8FAFF;
		color: rgba(0,0,0,0.7);
		font-size: 1rem;
		font-weight: 700;
		text-decoration: none;
		text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.22);
		box-shadow: 0 18px 38px rgba(0, 0, 0, 0.25);
		transition:
			transform 0.22s ease,
			box-shadow 0.22s ease;
	}

	.back:hover {
		transform: translateY(-3px);
		box-shadow: 0 22px 40px rgba(0, 0, 0, 0.32);
	}

	@media (max-width: 720px) {
		.page-inner {
			padding: 22px 18px;
		}

		.hero h1 {
			font-size: 2.2rem;
		}

		.hero p {
			font-size: 0.95rem;
		}

		.card {
			min-height: 76px;
			padding: 0 18px;
		}

		.card h2 {
			font-size: clamp(1.6rem, 4vw, 2rem);
		}

		.back {
			width: 100%;
			padding: 14px 0;
		}
	}
</style>
