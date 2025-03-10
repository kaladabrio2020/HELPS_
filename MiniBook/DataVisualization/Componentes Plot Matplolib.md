# Componentes do matplotlolib

## legends

1. **loc**: Define a posição da legenda no gráfico. Pode ser um valor de string ou um valor numérico. Alguns valores de string comuns são:
   
   - `'best'`: Escolhe automaticamente a melhor posição para a legenda.
   - `'upper right'`, `'upper left'`, `'lower right'`, `'lower left'`: Posições específicas nos cantos.
   - `'center'`, `'center left'`, `'center right'`: Posições centradas nos lados.

2. **bbox_to_anchor**: Especifica a posição da legenda em coordenadas relativas ao eixo, permitindo colocar a legenda fora da área do gráfico.
   
   *  `bbox_to_anchor`: **( x, y, width, height )**

3. **title**: Título da legenda.

4. **labels**: Lista de rótulos para os elementos gráficos.

5. **handlelength** e **handletextpad**: Controlam o comprimento da linha (ou símbolo) da legenda e o espaçamento entre a linha e o texto, respectivamente.

6. **borderaxespad**: Espaçamento entre a legenda e os eixos.

7. **borderpad**: Espaçamento interno da legenda.

8. **shadow**: Se verdadeiro, a legenda terá uma sombra.

9. **frameon**: Se verdadeiro, a legenda será desenhada com um quadro.

10. **ncol**: Número de colunas na legenda quando há vários rótulos.

11. **mode**: Pode ser `'expand'` para preencher todo o espaço disponível na caixa da legenda.

12. **fontsize**: Tamanho da fonte para o texto da legenda.

13. **markerfirst**: Se verdadeiro, o marcador (linha, símbolo, etc.) será exibido antes do texto na legenda.

14. **labelspacing**: Espaçamento vertical entre rótulos na legenda.

15. **framealpha**: Transparência do quadro da legenda.

16. **facecolor**: Cor de fundo da legenda.

17. **edgecolor**: Cor da borda da legenda.

18. **fancybox**: Se verdadeiro, a legenda terá um estilo "fancybox".

&nbsp;

## Yaxis e Xaxis

1. **ax.yaxis.set_major_locator(locator):** Define o localizador (estratégia de posicionamento) para os principais marcadores no eixo Y.

2. **ax.yaxis.set_major_formatter(formatter):** Define o formatador para os principais marcadores no eixo Y.

3. **ax.yaxis.set_minor_locator(locator):** Define o localizador para os marcadores menores no eixo Y.

4. **ax.yaxis.set_minor_formatter(formatter):** Define o formatador para os marcadores menores no eixo Y.

5. **ax.yaxis.grid(which='major'):** Adiciona grades ao eixo Y.

6. **ax.yaxis.tick_params(axis='y'):** Define os parâmetros dos marcadores do eixo Y, como largura, cor, estilo, tamanho da fonte, etc.

7. **ax.yaxis.set_label_position():** posição do titulo do label [`right`,`left`]

8. **ax.invert_yaxis()**: Inverte a direção do eixo Y (útil em gráficos de barras e outros tipos de gráficos).

9. **ax.set_ybound(lower=None, upper=None):** Define os limites superior e inferior para o eixo Y.

&nbsp;

## X e Y , no axis

1. **plt.ylabel(label, **kwargs):** Define o rótulo do eixo Y para o gráfico.
   
   *  `label`: O texto que você deseja exibir como rótulo do eixo.
   
   * `fontdict`: Um dicionário que especifica as propriedades da fonte do rótulo.
   
   * `labelpad`: O espaçamento entre o rótulo e o eixo.
   
   * `loc`: Posição do rótulo em relação ao eixo. Valores comuns incluem `'center'`, `'left'`, `'right'`, `'top'`, `'bottom'`, entre outros.

2. **plt.ylim(bottom=None, top=None, emit=True, auto=False, **kwargs):** Define os limites do eixo Y. Você pode especificar os valores mínimo e máximo.

3. **plt.yscale(value, **kwargs):** Define a escala do eixo Y. Alguns valores comuns para `value` são `'linear'` (escala linear), `'log'` (escala logarítmica), `'symlog'` (escala logarítmica simétrica) e `'logit'` (escala logística).

4. **plt.yticks(ticks=None, labels=None, **kwargs):** Define as posições e rótulos dos marcadores no eixo Y.

## fontsize

> parametro de alguma função

1. `fontsize` ou `size`: Tamanho da fonte.

2. `fontweight` ou `weight`: Peso da fonte (por exemplo, `'normal'`, `'bold'`, `'light'`, `'heavy'`, etc.).

3. `fontstyle` ou `style`: Estilo da fonte (por exemplo, `'normal'`, `'italic'`, `'oblique'`).

4. `family`: Família da fonte (por exemplo, `'serif'`, `'sans-serif'`, `'cursive'`, `'fantasy'`, `'monospace'`).

5. `color` ou `c`: Cor da fonte.

6. `backgroundcolor` ou `bg`: Cor de fundo do texto.

7. `verticalalignment` ou `va`: Alinhamento vertical do texto (por exemplo, `'center'`, `'top'`, `'bottom'`).

8. `horizontalalignment` ou `ha`: Alinhamento horizontal do texto (por exemplo, `'center'`, `'left'`, `'right'`).

9. `rotation`: Ângulo de rotação do texto.

10. `linespacing`: Espaçamento entre linhas do texto.

11. `letterspacing`: Espaçamento entre caracteres do texto.

12. `fontdict` também pode conter outros parâmetros específicos da fonte, dependendo da sua saída, como `fontproperties` para texto TeX.

&nbsp;

## Anotação

```python
for p in bar.patches:
    if p.get_width() != 0:
        bar.annotate("%.2f" % p.get_width(), 
        xy        = (p.get_width(), 
        p.get_y()+p.get_height()/2), 
        xytext    = (0, 0), 
        textcoords= 'offset points', 
        ha        = 'right', 
        va        = "center"
)
```
