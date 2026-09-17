# Pacote QGIS — JU0014 sem borda preta

Esta pasta contém a versão do projeto QGIS preparada para uso móvel, com a camada raster `JU0014` apontando para `JU0014_sem_borda.tif`. O raster é um Cloud Optimized GeoTIFF (COG) com máscara transparente, pirâmides de visualização e compressão JPEG, mantendo a referência espacial EPSG:32723.

A versão publicada aqui é uma cópia compactada do raster usada para respeitar o limite de 100 MB por arquivo do GitHub. Ela tem aproximadamente 24 MB. O pacote operacional do QFieldCloud continua usando a versão `JU0014_sem_borda.tif` validada no projeto `Cadastro_Campo_TIC_14-09-2026`.

O arquivo `Cadastro_Campo_cloud.qgs` referencia o raster relativo `./JU0014_sem_borda.tif`. As demais camadas e bases do projeto permanecem gerenciadas no QFieldCloud e não são duplicadas nesta pasta.

O pacote também inclui `referencias_tic.gpkg`, com as cinco camadas recebidas e já apontadas pelo QGS: **Vetorização — polígonos** (143 feições), **Vetorização — linhas** (485), **Vetorização — pontos** (110), **Áreas Executivo / Reassentamento** (87 polígonos) e **PAR — áreas** (44 polígonos). Todas ficam no grupo aberto **REFERÊNCIAS RECEBIDAS — VISÍVEIS** e entram ligadas por padrão.

O DXF binário foi convertido e tratado como UTM 23S / WGS 84 (EPSG:32723), mesma referência usada no DWG cadastral anterior, e as camadas foram gravadas no GeoPackage em WGS 84 (EPSG:4326). As entidades de metadados na origem `(0,0)` foram descartadas para não deslocar o enquadramento do projeto.

As outras imagens seguem a associação do projeto QGIS: `LO_002` usa `odm_orthophoto1.tif`, `LO_003` usa `odm_orthophoto2.tif` e `VA_004` usa `odm_orthophoto.tif`. Os nomes dos arquivos são mantidos por compatibilidade com o projeto; a conferência espacial confirmou que os pontos `LO-001`, `LO-003` e `VA-004` caem, respectivamente, nas áreas das camadas `LO_002`, `LO_003` e `VA_004`.

## Classificação cadastral

Os pontos públicos do mapa usam a mesma separação operacional do DWG: **Concluído** para `OCUPAÇÕES CADASTRADAS`, **A cadastrar** para `OCUPAÇÕES NÃO CADASTRADAS` e **Recusa** para a camada `RECUSA`. Por solicitação do responsável pelo projeto, a ficha completa dos registros **Concluído** foi publicada no mapa web, incluindo os campos pessoais existentes na base; os registros não concluídos permanecem com os dados cadastrais reduzidos.

A camada privada `Croquis cadastrais` também usa a separação do DWG: verde para `OCUPAÇÕES CADASTRADAS`, laranja para `OCUPAÇÕES NÃO CADASTRADAS` e vermelho para `RECUSA`. O contorno dos croquis foi aumentado para **1,2 mm** para melhorar a leitura no QGIS e no QField.

O mapa web também publica a camada vetorial `croquis.geojson`, com os **28 croquis** do GeoPackage, separados por cor conforme a classe do DWG e com contorno espesso para leitura sobre a imagem aérea. A ficha aberta ao clicar em um ponto segue a ordem do formulário QGIS/modelo FC: `1. Ocupante`, `2. Região`, `3. Habitação e Serviços`, `4. Construção e Demolição` e `5. Croqui e Fotos`. O campo utilizado para a classificação construtiva é **Estado de conservação**, conforme a planilha cadastral.

Os campos **Perímetro (m)** e **Área (m²)** dos imóveis que possuem croqui foram calculados a partir da geometria do croqui em EPSG:32723 e gravados na camada cadastral. Os valores também estão disponíveis no `dados.geojson` e no tooltip da camada web de croquis.

Na seção **4. Construção e Demolição**, foi incluída a pergunta **“Pode ocorrer demolição parcial?”**, com opções **Sim** e **Não**. Quando a resposta for **Não**, o formulário QGIS/QField abre o campo **“Justificativa da não demolição parcial”**.

## Formulário fotográfico

O formulário de coleta não exibe mais o campo visual de Croqui. Ele termina com a relação **5. Relatório fotográfico** e, depois das fotos, com **6. Observação final**. A relação de fotos é 1:N: o cadastrador pode adicionar várias imagens do mesmo imóvel ou cômodo, e cada imagem possui sua própria **Descrição da foto / local**. O passo a passo está em [`INSTRUCOES_FORMULARIO_FOTOGRAFICO.md`](INSTRUCOES_FORMULARIO_FOTOGRAFICO.md).

## Verificação

| Item | Resultado |
| --- | --- |
| Raster | `JU0014_sem_borda.tif` |
| Formato | COG / GeoTIFF |
| Dimensões | 7.777 × 10.462 pixels |
| Sistema de referência | EPSG:32723 |
| Transparência | Máscara interna para remover a borda preta |
| Tamanho publicado | Aproximadamente 24 MB |
