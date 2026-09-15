# Pacote QGIS — JU0014 sem borda preta

Esta pasta contém a versão do projeto QGIS preparada para uso móvel, com a camada raster `JU0014` apontando para `JU0014_sem_borda.tif`. O raster é um Cloud Optimized GeoTIFF (COG) com máscara transparente, pirâmides de visualização e compressão JPEG, mantendo a referência espacial EPSG:32723.

A versão publicada aqui é uma cópia compactada do raster usada para respeitar o limite de 100 MB por arquivo do GitHub. Ela tem aproximadamente 24 MB. O pacote operacional do QFieldCloud continua usando a versão `JU0014_sem_borda.tif` validada no projeto `Cadastro_Campo_TIC_14-09-2026`.

O arquivo `Cadastro_Campo_cloud.qgs` referencia o raster relativo `./JU0014_sem_borda.tif`. As demais camadas e bases do projeto permanecem gerenciadas no QFieldCloud e não são duplicadas nesta pasta.

## Verificação

| Item | Resultado |
| --- | --- |
| Raster | `JU0014_sem_borda.tif` |
| Formato | COG / GeoTIFF |
| Dimensões | 7.777 × 10.462 pixels |
| Sistema de referência | EPSG:32723 |
| Transparência | Máscara interna para remover a borda preta |
| Tamanho publicado | Aproximadamente 24 MB |
