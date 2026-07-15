import { readFileSync, writeFileSync } from 'node:fs';

const targetPath = 'src/routes/jogar/+page.svelte';
let content = readFileSync(targetPath, 'utf8');

const oldBlock = `				<table class="mapa-grid">
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
`;

const newBlock = `				<table class="mapa-grid">
					{#each mapa as linha, r}
						<tr>
							{#each linha as celula, c}
								{#if playerPosition.r === r && playerPosition.c === c}
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
										{/if}
									</td>
								{/if}
							{/each}
						</tr>
					{/each}
				</table>
`;

if (!content.includes(oldBlock)) {
	console.error('Old block not found.');
	process.exit(1);
}

writeFileSync(targetPath, content.replace(oldBlock, newBlock), 'utf8');
console.log('patched');
