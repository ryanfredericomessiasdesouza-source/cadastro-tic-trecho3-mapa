# Atualização da faixa de servidão e dos KMs

Esta atualização substitui as faixas antigas da CPTM/RUMO e a quilometragem anterior pelo arquivo recebido `FaixadeServidão.dxf`, convertido para o GeoPackage operacional `faixa_servidao.gpkg`.

## Arquivos que devem ser sincronizados

1. `Cadastro_Campo_cloud.qgs` — projeto atualizado, com as camadas antigas removidas.
2. `faixa_servidao.gpkg` — arquivo novo com a faixa e os KMs que vieram no DXF:
   - `faixa_servidao` — 8 trechos de faixa;
   - `km_faixa_servidao` — 81 marcos, de `64+140 m` a `91+420 m`.
3. `referencias_tic.gpkg` — mesma base de referências recebidas, com o quadrado vazio removido da camada `Vetorização — polígonos` (142 polígonos restantes).

A base cadastral `cadastro_trecho3.gpkg` não foi alterada nesta revisão.

## Pela tela de sincronização do QFieldSync

1. Copie os três arquivos acima para a pasta local do projeto, mantendo-os junto do QGS.
2. Abra o QFieldSync e atualize a lista de arquivos.
3. Para `faixa_servidao.gpkg`, selecione **Create file on the cloud** — é um arquivo novo.
4. Para `referencias_tic.gpkg`, selecione a ação de atualizar/substituir o arquivo existente.
5. Para `Cadastro_Campo_cloud.qgs`, selecione a ação de atualizar/substituir o arquivo existente; não crie uma segunda cópia.
6. Execute a sincronização/push.
7. No celular, faça a sincronização do projeto e reabra o projeto se o QField solicitar.

## Resultado visual esperado

O grupo **FAIXA DE SERVIDÃO — arquivo recebido** fica aberto e ligado por padrão. Ele contém:

- **Faixa de Servidão — recebida** — traço amarelo tracejado com contorno escuro para leitura sobre a imagem aérea;
- **KM — Faixa de Servidão** — pontos amarelos com contorno escuro e rótulos com halo branco.

As camadas **FAIXA DE DOMÍNIO RUMO**, **Domínios_CPTM_L7**, **KM TIC Jundiaí — completa** e **Marcos KM** foram retiradas do projeto para evitar sobreposição e duplicidade.

A camada **Vetorização — polígonos** permanece no grupo **REFERÊNCIAS RECEBIDAS — VISÍVEIS**. Foi removida somente a feição identificada como quadrado vazio, `FID 89 / EntityHandle F82`, da classe `Edificações`; as demais referências foram preservadas.

## Sistema de referência

O DXF não informava CRS, mas suas coordenadas são compatíveis com **UTM 23S / WGS 84 — EPSG:32723**. A nova base foi reprojetada para **WGS 84 — EPSG:4326**, igual ao CRS do projeto QGIS.

## Arquivos antigos

Os arquivos antigos foram retirados do pacote operacional e mantidos apenas em uma cópia de segurança local, em `backups/20260918_antes_faixa_servidao`. Eles não devem ser recopiados para a pasta sincronizada, pois reintroduziriam camadas duplicadas.
