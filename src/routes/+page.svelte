<script lang="ts">
	let tituloDoJogo: string = 'YU-GI-OH';
</script>

<div class="page">
	<div class="page-box">
		<span class="label">Bem-vindo</span>
		<h1>{tituloDoJogo}</h1>
		<p class="subtitle">
			Escolha o duelo ou conheça a equipe que criou este jogo inspirado no universo dos cards.
		</p>

		<nav class="menu">
			<a href="/jogar">Jogar</a>
			<a href="/sobre">Sobre</a>
		</nav>
	</div>
</div>

<style>
	.page {
		min-height: 100vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 24px 18px;
		background: radial-gradient(circle at top, rgba(160, 60, 35, 0.16), transparent 30%),
			linear-gradient(180deg, #0f0508 0%, #080205 100%);
	}

	.page-box {
		position: relative;
		width: min(700px, 100%);
		padding: 44px 34px;
		border-radius: 40px;
		background: rgba(10, 6, 10, 0.95);
		border: 1px solid rgba(255, 255, 255, 0.08);
		box-shadow: 0 40px 100px rgba(0, 0, 0, 0.4);
		text-align: center;
		overflow: hidden;
	}

	.page-box::before {
		content: '';
		position: absolute;
		inset: -35px;
		background: radial-gradient(circle at top, rgba(210, 110, 55, 0.16), transparent 42%);
		pointer-events: none;
	}

	.label {
		display: inline-flex;
		margin-bottom: 16px;
		color: #f5d78e;
		letter-spacing: 0.3em;
		text-transform: uppercase;
		font-size: 0.78rem;
		opacity: 0.95;
	}

	h1 {
		margin: 0;
		font-size: clamp(3rem, 6vw, 4.4rem);
		color: #f5d78e;
		text-shadow: 0 10px 28px rgba(0, 0, 0, 0.28);
	}

	.subtitle {
		margin: 18px auto 0;
		max-width: 560px;
		color: rgba(245, 215, 142, 0.92);
		line-height: 1.88;
		font-size: 1rem;
	}

	.menu {
		display: grid;
		gap: 16px;
		margin-top: 36px;
		width: min(380px, 100%);
		margin: 0 auto;
	}

	.menu a {
		display: inline-flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		min-height: 64px;
		padding: 0 24px;
		border-radius: 22px;
		font-weight: 800;
		letter-spacing: 0.03em;
		text-decoration: none;
		color: #fde3a4;
		background: linear-gradient(135deg, #3d0908 0%, #7d2913 35%, #c9853f 68%, #7a2a12 100%);
		box-shadow: 0 20px 40px rgba(0, 0, 0, 0.22);
		transition:
			transform 0.22s ease,
			box-shadow 0.22s ease,
			background 0.22s ease;
	}

	.menu a:hover {
		transform: translateY(-3px);
		box-shadow: 0 26px 46px rgba(0, 0, 0, 0.28);
	}

	@media (max-width: 660px) {
		.page-box {
			padding: 30px 20px;
		}

		h1 {
			font-size: 3rem;
		}

		.subtitle {
			font-size: 0.95rem;
		}

		.menu {
			width: 100%;
		}

		.menu a {
			min-height: 58px;
			padding: 0 18px;
		}
	}
</style>
