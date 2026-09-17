# Atualização do formulário — relatório fotográfico

## O que mudou

O campo visual de **Croqui do imóvel (anexo)** foi retirado do formulário de coleta. O arquivo/campo foi preservado na base para não apagar informações antigas, mas não é mais apresentado ao cadastrador.

O formulário agora termina com duas etapas:

1. **Relatório fotográfico** — relação de fotos do imóvel;
2. **Observação final** — um único campo de observação, localizado depois das fotos.

O campo antigo **Observação da região** (`obs_regiao`) deixou de ser apresentado no formulário. A observação que deve ser preenchida pelo cadastrador é **Observação final** (`observacoes`).

## Melhor fluxo para várias fotos do mesmo cômodo

A relação `cad_fotos` foi configurada como **Composition** e continua sendo de um cadastro para várias fotos. A partir do QField **4.2**, o QField pode transformar automaticamente essa relação em uma **Galeria de fotos** quando a camada filha tem um campo de anexo. O QField **4.3** é recomendado, pois trouxe melhorias recentes na câmera.

Atualize o QField do computador/celular para a versão 4.3 ou mais recente. Depois de sincronizar o projeto, a seção **Relatório fotográfico** deverá aparecer como uma galeria, com miniaturas e um botão rápido de captura.

Fluxo recomendado:

1. Abra o cadastro do imóvel.
2. Entre em **Relatório fotográfico**.
3. Use o botão rápido de câmera da galeria.
4. Tire a foto e confirme no botão verde.
5. Use novamente o botão rápido da galeria para a próxima foto do mesmo cômodo.
6. Repita até terminar o cômodo.
7. Selecione as fotos para editar e preencha **Descrição da foto / local**. Para uma descrição comum, use, por exemplo, `Quarto — paredes, janela e porta`; para descrições diferentes, edite cada foto separadamente.
8. Ao terminar todas as imagens, preencha **Observação final** no fim do cadastro.

Cada fotografia fica em uma linha própria da camada `fotos_trecho3`, vinculada ao mesmo `id_imovel`.

## Limite da câmera contínua

O QGS não possui uma configuração capaz de obrigar a câmera interna do QField a permanecer aberta depois do botão verde. A melhoria nativa disponível é a **Galeria de fotos com captura rápida**, que reduz o fluxo para confirmar a foto e tocar novamente no botão de câmera.

Manter a câmera aberta automaticamente, tirar várias fotos e só depois retornar ao formulário exigiria um plugin QField personalizado. Não foi distribuído um plugin experimental no projeto operacional, pois ele precisa ser testado na mesma versão do QField e no dispositivo de campo para evitar perda ou duplicação de fotos.

## Sincronização

No computador, substitua o arquivo `Cadastro_Campo_cloud.qgs` pelo arquivo desta atualização na pasta local do projeto. No QFieldSync:

1. Atualize a lista de arquivos;
2. Para `Cadastro_Campo_cloud.qgs`, escolha atualizar/substituir o arquivo existente;
3. Não crie uma segunda cópia com outro nome;
4. Execute o push/sincronização;
5. No celular, sincronize o projeto e atualize/reabra o QField.

Não é necessário substituir o `cadastro_trecho3.gpkg` para esta alteração de formulário. A camada de fotos existente já possui os campos `id_imovel`, `foto` e `descricao` e aceita várias linhas para o mesmo imóvel.

## Referências oficiais

- [QField — Attachment widget](https://docs.qfield.org/how-to/project-setup/pictures/)
- [QField — Relation Reference widget e Gallery Relation Editor](https://docs.qfield.org/how-to/project-setup/relation-reference-widget/)
- [QField 4.2 — Gallery Editor e captura rápida](https://qfield.org/blog/2026/06/09/qfield-4.2-coral-sea-reaching-sub-centimeter-accuracy-out-of-the-box/)
- [QField 4.3 — melhorias da câmera](https://qfield.org/blog/2026/09/08/qfield-4.3-danube-summer-of-stability/)
