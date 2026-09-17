# Atualização do formulário — relatório fotográfico

## O que mudou

O campo visual de **Croqui do imóvel (anexo)** foi retirado do formulário de coleta. O arquivo/campo foi preservado na base para não apagar informações antigas, mas não é mais apresentado ao cadastrador.

O formulário agora termina com duas etapas:

1. **Relatório fotográfico** — relação de fotos do imóvel;
2. **Observação final** — um único campo de observação, localizado depois das fotos.

O campo antigo **Observação da região** (`obs_regiao`) deixou de ser apresentado no formulário. A observação que deve ser preenchida pelo cadastrador é **Observação final** (`observacoes`).

## Como registrar várias fotos do mesmo local

A seção **Relatório fotográfico** é uma relação de um cadastro para várias fotos. Não existe limite de uma foto por imóvel ou por cômodo.

Para registrar três fotos de um quarto, por exemplo:

1. Abra o cadastro do imóvel.
2. Entre em **Relatório fotográfico**.
3. Use o botão de adicionar para criar o primeiro registro.
4. Tire ou selecione a primeira foto.
5. Preencha **Descrição da foto / local**, por exemplo: `Quarto — parede lateral`.
6. Salve o registro da foto.
7. Use novamente o botão de adicionar para criar a segunda foto e repita o procedimento.
8. Faça o mesmo para a terceira foto.
9. Ao terminar todas as imagens, preencha **Observação final** no fim do cadastro.

Cada fotografia fica em uma linha própria da camada `fotos_trecho3`, vinculada ao mesmo `id_imovel`. Assim, todas as imagens do quarto podem ser consultadas separadamente, cada uma com sua descrição.

## Sincronização

No computador, substitua o arquivo `Cadastro_Campo_cloud.qgs` pelo arquivo desta atualização na pasta local do projeto. No QFieldSync:

1. Atualize a lista de arquivos;
2. Para `Cadastro_Campo_cloud.qgs`, escolha atualizar/substituir o arquivo existente;
3. Não crie uma segunda cópia com outro nome;
4. Execute o push/sincronização;
5. No celular, sincronize o projeto e reabra-o.

Não é necessário substituir o `cadastro_trecho3.gpkg` para esta alteração de formulário. A camada de fotos existente já possui os campos `id_imovel`, `foto` e `descricao` e aceita várias linhas para o mesmo imóvel.
