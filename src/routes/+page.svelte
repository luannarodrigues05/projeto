<script lang="ts">
	let tituloDoJogo: string = 'The Origin of Aether';
</script>

<div class="page">
	<div class="page-box">
		<span class="label">Bem-vindo a</span>
		<h1>{tituloDoJogo}</h1>
		<p class="subtitle">Descubra a verdade além das nuvens.</p>

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
		background: radial-gradient(circle at top, #1e3a5f, transparent 30%),
			linear-gradient(180deg, #6ecbf5 0%, #f7c948 100%);
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

	.page-box::before {
		content: '';
		position: absolute;
		inset: -35px;
		background: radial-gradient(circle at top, rgba(210, 110, 55, 0.16), transparent 42%);
		pointer-events: none;
	}

	.label {
		display: inline-flex;
		margin-bottom: 20px;
		color:  #F8FAFF;
		letter-spacing: 0.3em;
		text-transform: uppercase;
		font-size: 0.78rem;
		opacity: 0.95;
	}

	h1 {
		margin: 0;
		font-size: clamp(3rem, 6vw, 4.4rem);
		color: #FFD700;
		text-shadow: 0 10px 28px rgba(0, 0, 0, 0.28);
	}

	.subtitle {
		margin: 20px auto 12px;
		max-width: 560px;
		color: #F8FAFF;
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
		color: rgba(0,0,0,0.7);
		background: #F8FAFF;
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
