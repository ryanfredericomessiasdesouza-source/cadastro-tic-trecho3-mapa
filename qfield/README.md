# Pacote QGIS — JU0014 sem borda preta

Esta pasta contém a versão do projeto QGIS preparada para uso móvel, com a camada raster `JU0014` apontando para `JU0014_sem_borda.tif`. O raster é um Cloud Optimized GeoTIFF (COG) com máscara transparente, pirâmides de visualização e compressão JPEG, mantendo a referência espacial EPSG:32723.

A versão publicada aqui é uma cópia compactada do raster usada para respeitar o limite de 100 MB por arquivo do GitHub. Ela tem aproximadamente 24 MB. O pacote operacional do QFieldCloud continua usando a versão `JU0014_sem_borda.tif` validada no projeto `Cadastro_Campo_TIC_14-09-2026`.

O arquivo `Cadastro_Campo_cloud.qgs` referencia o raster relativo `./JU0014_sem_borda.tif`. As demais camadas e bases do projeto permanecem gerenciadas no QFieldCloud e não são duplicadas nesta pasta.

As outras imagens seguem a associação do projeto QGIS: `LO_002` usa `odm_orthophoto1.tif`, `LO_003` usa `odm_orthophoto2.tif` e `VA_004` usa `odm_orthophoto.tif`. Os nomes dos arquivos são mantidos por compatibilidade com o projeto; a conferência espacial confirmou que os pontos `LO-001`, `LO-003` e `VA-004` caem, respectivamente, nas áreas das camadas `LO_002`, `LO_003` e `VA_004`.

## Classificação cadastral

Os pontos públicos do mapa usam a mesma separação operacional do DWG: **Concluído** para `OCUPAÇÕES CADASTRADAS`, **A cadastrar** para `OCUPAÇÕES NÃO CADASTRADAS` e **Recusa** para a camada `RECUSA`. Por solicitação do responsável pelo projeto, a ficha completa dos registros **Concluído** foi publicada no mapa web, incluindo os campos pessoais existentes na base; os registros não concluídos permanecem com os dados cadastrais reduzidos.

A camada privada `Croquis cadastrais` também usa a separação do DWG: verde para `OCUPAÇÕES CADASTRADAS`, laranja para `OCUPAÇÕES NÃO CADASTRADAS` e vermelho para `RECUSA`. O contorno dos croquis foi aumentado para **1,2 mm** para melhorar a leitura no QGIS e no QField.

O mapa web também publica a camada vetorial `croquis.geojson`, com os **28 croquis** do GeoPackage, separados por cor conforme a classe do DWG e com contorno espesso para leitura sobre a imagem aérea. A ficha aberta ao clicar em um ponto segue a ordem do formulário QGIS/modelo FC: `1. Ocupante`, `2. Região`, `3. Habitação e Serviços`, `4. Construção e Demolição` e `5. Croqui e Fotos`. O campo utilizado para a classificação construtiva é **Estado de conservação**, conforme a planilha cadastral.

## Verificação

| Item | Resultado |
| --- | --- |
| Raster | `JU0014_sem_borda.tif` |
| Formato | COG / GeoTIFF |
| Dimensões | 7.777 × 10.462 pixels |
| Sistema de referência | EPSG:32723 |
| Transparência | Máscara interna para remover a borda preta |
| Tamanho publicado | Aproximadamente 24 MB |
