from pathlib import Path
p = Path('src/routes/jogar/+page.svelte')
t = p.read_text(encoding='utf-8')
old = '''				<table class="mapa-grid">
					{#each mapa as linha, r}
						<tr>
							{#each linha as celula, c}
								{#if celula === 'obstacle'}
									<td class={"celula tile " + celula} style={estiloTile(celula, r, c)}>
										⬛
									</td>
								{:else if playerPosition.r === r && playerPosition.c === c}
									<td class={"celula tile " + celula + ' player'} style={estiloTile(celula, r, c)}>
										{personagemAtivo?.emoji ?? '👤'}
									</td>
								{:else}
									{#if caminho.length}
										{#if caminho.findIndex(p => p.r === r && p.c === c) >= 0 && caminho.findIndex(p => p.r === r && p.c === c) <= destaqueIndex}
											<td class={"celula tile " + celula + ' highlight'} style={estiloTile(celula, r, c)}>
												{#if celula === 'start'}
													🏁
												{:else if celula === 'goal'}
													🎯
												{:else if celula === 'challenge'}
													❗
												{:else}
													
												{/if}
											</td>
									{:else}
										<td class={"celula tile " + celula} style={estiloTile(celula, r, c)}>
											{#if celula === 'start'}
												🏁
											{:else if celula === 'goal'}
												🎯
											{:else if celula === 'challenge'}
												❗
											{:else}
												
												{/if}
										</td>
									{/if}
									{/if}
								{/if}
							{/each}
						</tr>
					{/each}
				</table>
'''
new = '''				<table class="mapa-grid">
					{#each mapa as linha, r}
						<tr>
							{#each linha as celula, c}
								{#if celula === 'obstacle'}
									<td class={"celula tile " + celula} style={estiloTile(celula, r, c)}>
										⬛
									</td>
								{:else if playerPosition.r === r && playerPosition.c === c}
									<td class={"celula tile " + celula + ' player'} style={estiloTile(celula, r, c)}>
										{personagemAtivo?.emoji ?? '👤'}
									</td>
								{:else}
									<td class={"celula tile " + celula + (destaqueNoCaminho(r, c) ? ' highlight' : '')} style={estiloTile(celula, r, c)}>
										{#if celula === 'start'}
											🏁
										{:else if celula === 'goal'}
											🎯
										{:else if celula === 'challenge'}
											❗
										{:else if celula === 'battle'}
											⚔️
										{:else if celula === 'locked'}
											🔒
										{:else if celula === 'obstacle'}
											⬛
										{:else}
											
											{/if}
									</td>
								{/if}
							{/each}
						</tr>
					{/each}
				</table>
'''
if old not in t:
    raise SystemExit('old block not found')
t = t.replace(old, new)
p.write_text(t, encoding='utf-8')
