# Atualização cadastral — DWG + planilha

Esta atualização incorpora ao projeto os 16 registros que possuíam correspondência simultânea entre o DWG, a planilha cadastral e um polígono de croqui. Também foram adicionados diretamente do DWG os 12 registros `LO-003`, com FIDs novos 110 a 121, porque eles não possuíam FID na planilha recebida. A base final possui 118 pontos e 28 croquis.

Os pontos foram posicionados pelas coordenadas dos textos do DWG, convertidas de UTM 23S (EPSG:32723) para WGS 84 (EPSG:4326). Os polígonos foram importados em uma camada separada chamada `Croquis cadastrais`, com o campo `fid_cadastro` vinculando cada croqui ao cadastro correspondente.

Os registros que não estão no DWG não foram alterados. Os 16 registros associados à planilha mantiveram os FIDs originais. Os 12 registros LO-003 receberam FIDs sequenciais novos, sem preencher `fid_planilha`, e foram marcados no campo de observação como importação direta do DWG.

No formulário, o grupo **1. Ocupante** agora contém **Selagem**, com o código `LO-001-009`, e **Ocupação**, com o texto `OC-TIC-LO-001-RE-009-O`. Os campos auxiliares **Ocupante** e **Classificação DWG** não são exibidos no formulário.

A separação do DWG foi preservada. Entre os 28 registros originados do DWG, `OCUPAÇÕES CADASTRADAS` corresponde a **Concluído** (21 registros), `OCUPAÇÕES NÃO CADASTRADAS` corresponde a **A cadastrar** (5 registros) e `RECUSA` corresponde a **Recusa** (2 registros). A camada `Cadastro_Campo` usa simbologia categorizada por esse status.

A camada `Croquis cadastrais` usa a mesma separação visual: verde para `OCUPAÇÕES CADASTRADAS`, laranja para `OCUPAÇÕES NÃO CADASTRADAS` e vermelho para `RECUSA`. O contorno foi configurado com **1,2 mm** para facilitar a visualização no QGIS e no QField.

Os textos `LO-003-004`, `LO-003-005` e `LO-003-012` compartilham o mesmo polígono de origem, handle `4E55`, no DWG. Os três pontos foram inseridos, e os três croquis foram mantidos com a mesma geometria de origem, sem inventar limites que não existem no arquivo CAD.

## Novas referências recebidas

Os três arquivos enviados foram consolidados em `referencias_tic.gpkg`, sem alterar os dados cadastrais existentes:

| Camada no QGIS/QField | Origem | Conteúdo | Visibilidade |
|---|---|---|---|
| `Vetorização — polígonos` | `vetorização.dxf` | 142 polígonos após a retirada do quadrado vazio | Ligada |
| `Vetorização — linhas` | `vetorização.dxf` | 485 linhas | Ligada |
| `Vetorização — pontos` | `vetorização.dxf` | 110 pontos | Ligada |
| `Áreas Executivo / Reassentamento` | `ÁreasExecutivo-Reassentamento.kml` | 87 áreas | Ligada |
| `PAR — áreas` | `PAR.kmz` | 44 áreas | Ligada |

O DXF recebido estava em **DXF binário e sem CRS declarado**. Ele foi convertido para leitura pelo QGIS e tratado como **UTM 23S / WGS 84 (EPSG:32723)**, a mesma referência adotada para o DWG cadastral anterior, sendo reprojetado para WGS 84 (EPSG:4326). As entidades de metadados localizadas na origem `(0,0)` foram descartadas para evitar que o enquadramento do projeto fosse deslocado para fora da área de trabalho.

As novas camadas ficam dentro do grupo aberto **REFERÊNCIAS RECEBIDAS — VISÍVEIS**, logo abaixo de `Croquis cadastrais`, com cores fortes e linhas espessas para facilitar a visualização no QGIS e no QField.

Na revisão visual, a vetorização foi categorizada por tema: polígonos de edificações em azul, calçadas em cinza e piscinas em ciano; linhas ferroviárias em preto, limites de ocupação em magenta, lotes em laranja e limites de faixa em vermelho. As áreas Executivo/Reassentamento foram configuradas em verde translúcido e as áreas PAR em laranja translúcido, ambas com contorno espesso. A imagem `JU0014` permanece como voo principal ligado por padrão; os demais voos ficam disponíveis na legenda, mas desligados inicialmente para não encobrir as referências. Foi removida somente a feição identificada como quadrado vazio, `FID 89 / EntityHandle F82`, mantendo as demais 142 feições de polígonos.

## Faixa de servidão e KMs recebidos

O DXF `FaixadeServidão.dxf` foi convertido para `faixa_servidao.gpkg`. A base contém **8 trechos de faixa** e **81 marcos quilométricos** do próprio arquivo, de `64+140 m` a `91+420 m`, em WGS 84 (EPSG:4326). A faixa aparece em amarelo tracejado com contorno escuro; os KMs aparecem como pontos amarelos com rótulos e halo branco.

Para evitar a duplicação de informação, as camadas antigas **FAIXA DE DOMÍNIO RUMO**, **Domínios_CPTM_L7**, **KM TIC Jundiaí — completa** e **Marcos KM** foram removidas do projeto operacional. A nova camada fica no grupo **FAIXA DE SERVIDÃO — arquivo recebido**, ligado e aberto por padrão.

Para usar no QGIS/QField, mantenha o arquivo `Cadastro_Campo_cloud.qgs` na mesma pasta do `cadastro_trecho3.gpkg`, de `referencias_tic.gpkg` atualizado e dos demais arquivos auxiliares já existentes no projeto. Depois de sincronizar o projeto, expanda o grupo **REFERÊNCIAS RECEBIDAS — VISÍVEIS** para conferir as cinco camadas.

## Formulário atualizado — relatório fotográfico

O campo visual **Croqui do imóvel (anexo)** foi retirado do formulário de coleta, sem apagar o campo da base. O formulário termina agora com a relação **Relatório fotográfico** e, depois dela, um único campo **Observação final** (`observacoes`). O antigo campo `obs_regiao` não é mais apresentado ao cadastrador.

A relação `cad_fotos` é de um cadastro para várias fotos e está configurada como `Composition`. No QField 4.2 ou mais recente, preferencialmente 4.3, ela pode aparecer como galeria com captura rápida. O cadastrador pode adicionar várias imagens para o mesmo cômodo ou local; cada imagem fica em uma linha própria da camada `fotos_trecho3` e pode receber sua própria **Descrição da foto / local**. A relação está configurada com todos os botões de adicionar, editar e remover.

## Formulário único — Cadastro de Imóvel e Cadastro de Proprietário

O `Cadastro_Campo_cloud.qgs` foi reorganizado em um único formulário com dois blocos principais: **Cadastro de Imóvel** e **Cadastro de Proprietário**. O primeiro contém identificação, localização/endereço, registro/documentação, região, habitação/serviços, construção/demolição, relatório fotográfico e observação final. O segundo contém identificação, endereço, vínculo/contato e documentos do proprietário.

Para reproduzir os campos das telas enviadas, foram acrescentados ao `cadastro_trecho3.gpkg` os campos de UF, número, KM inicial/final, nome da propriedade, endereço detalhado, cartório/RGI, tipo/origem/data de nascimento/sexo e endereço do proprietário. Eles foram criados vazios, sem substituir dados existentes. Consulte `INSTRUCOES_FORMULARIO_UNICO.md` e o Excel `Cadastro_TIC_Formulario_Unico_Subdivisoes.xlsx`.

## Planilha de preenchimento com opções

A planilha `Cadastro_TIC_Formulario_Unico_Subdivisoes.xlsx` agora apresenta a coluna **Opções de preenchimento** e a coluna **Valor / preenchimento**. A aba `Listas de opções` reúne as alternativas dos campos ValueMap do QGS. O campo `proprietarios` também foi acrescentado à camada cadastral para representar o campo existente na tela enviada; como ainda não existe uma tabela oficial de proprietários no projeto, ele permanece como texto até a definição da relação de busca.
