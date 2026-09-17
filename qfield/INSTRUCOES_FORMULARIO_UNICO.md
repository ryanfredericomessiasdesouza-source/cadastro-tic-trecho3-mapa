# Formulário único — Cadastro TIC Trens

## Estrutura

O projeto QGIS/QField agora usa um único formulário por imóvel, com dois blocos principais e subdivisões internas:

### 1. Cadastro de Imóvel

- **Identificação do imóvel:** FC TBG Nova, FC Nº Antiga, Código TIC, Selagem, Ocupação, número, tipo, classificação, status, situação, trecho, KM e referências de DWG.
- **Localização e endereço:** UF, município, bairro, nome da propriedade, endereço, número, CEP, zona e coordenadas.
- **Registro e documentação:** matrícula, cartório, livro de registro, RGI, área e documentos rurais/urbanos.
- **Região — características e melhoramentos:** infraestrutura local, padrão de ocupação, vias de acesso, localização do lote, greide, topografia, aproveitamento/uso e melhoramentos urbanos.
- **Habitação e serviços:** tamanho da edificação, tempo de residência, materiais, água, escoadouro, composição dos cômodos, pavimentos e demais características habitacionais.
- **Construção e demolição:** descrição, idade, estado de conservação, perímetro, área, tipo de edificação, faixa de domínio, desnível, prioridade, risco e demolição parcial.
- **Relatório fotográfico:** relação 1:N de fotografias, mantendo várias fotos para o mesmo imóvel e descrição individual por imagem.
- **Observação final:** campo único de observação depois do relatório fotográfico.

### 2. Cadastro de Proprietário

- **Identificação do proprietário:** tipo, nome, CPF/CNPJ, RG/IE, origem, data de nascimento e sexo.
- **Endereço do proprietário:** CEP, endereço, número, complemento, UF e município.
- **Vínculo e contato:** tipo de vínculo, percentual de titularidade, estado civil, profissão, telefone e e-mail.
- **Documentos do proprietário:** documentos de identificação, estado civil e contrato social, quando aplicável.

## Campos acrescentados ao GeoPackage

Foram adicionados ao arquivo `cadastro_trecho3.gpkg`, na camada `cadastro_trecho3`, os campos identificados nas telas enviadas que não existiam na estrutura anterior:

`fc_tbg_nova`, `fc_n_antiga`, `uf_imovel`, `numero_imovel`, `km_inicial`, `km_final`, `nome_propriedade`, `cep_imovel`, `numero_endereco`, `cartorio`, `livro_registro`, `numero_rgi`, `trecho`, `tipo_proprietario`, `origem_proprietario`, `data_nascimento`, `sexo`, `cep_proprietario`, `endereco_proprietario`, `numero_proprietario`, `complemento_proprietario`, `uf_proprietario` e `municipio_proprietario`.

Os campos foram criados vazios para preenchimento. Nenhum valor cadastral existente foi apagado ou sobrescrito.

## Excel

O arquivo `Cadastro_TIC_Formulario_Unico_Subdivisoes.xlsx` contém:

- **Formulário único:** visão geral da sequência e das subdivisões;
- **Cadastro Imóvel:** campos do primeiro bloco, com ordem, subdivisão, campo técnico, rótulo, tipo, origem, situação e coluna para preenchimento;
- **Cadastro Proprietário:** campos do segundo bloco, com a mesma estrutura;
- **Base QGIS atual:** consulta de referência da camada cadastral.

## Sincronização

1. Copie para a pasta local do projeto o `Cadastro_Campo_cloud.qgs` atualizado e o `cadastro_trecho3.gpkg` atualizado.
2. Abra o projeto no QGIS e confirme se a camada `Cadastro_Campo` está carregando sem erro.
3. Pelo QFieldSync, escolha atualizar/substituir os arquivos existentes, sem criar cópias duplicadas.
4. Faça o upload/push para o QFieldCloud.
5. Sincronize o QField no celular e feche/reabra o projeto.

A cópia de segurança da base anterior é `cadastro_trecho3.pre_formulario_unico.bak.gpkg`. A cópia de segurança do projeto é `Cadastro_Campo_cloud.pre_formulario_unico.bak`.

## Observação sobre proprietários múltiplos

Esta atualização cria o bloco de Proprietário dentro do formulário único, preservando a estrutura atual de um registro cadastral. Os campos de proprietário continuam na camada principal. Caso um imóvel possa ter vários proprietários independentes, a evolução recomendada é criar uma tabela filha `proprietarios` e uma relação 1:N; essa alteração não foi feita automaticamente nesta etapa para não modificar os vínculos existentes.
