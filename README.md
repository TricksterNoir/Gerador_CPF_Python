<h1>Gerador de CPF Válido</h1>

<p>Este é um programa simples em Python que gera um CPF válido de forma aleatória. Ele utiliza a biblioteca <code>random</code> para gerar os nove dígitos iniciais e, em seguida, calcula os dígitos verificadores usando uma fórmula específica. O objetivo deste programa é demonstrar o cálculo dos dígitos verificadores de um CPF válido.</p>

<h2>Funcionamento</h2>

<p>O código é composto por duas partes principais:</p>

<ol>
  <li>Geração dos nove dígitos iniciais:
    <ul>
      <li>É criada uma string vazia chamada <code>nove_digitos</code>.</li>
      <li>Um loop é executado até que nove dígitos sejam gerados:
        <ul>
          <li>A função <code>random.randrange(10)</code> é usada para gerar um dígito aleatório de 0 a 9.</li>
          <li>O dígito gerado é convertido para string e concatenado à variável <code>nove_digitos</code>.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Cálculo dos dígitos verificadores:
    <ul>
      <li>A função <code>calcula_digito()</code> é definida e recebe dois parâmetros: <code>nums</code> (os nove dígitos gerados anteriormente) e <code>qtd_digitos</code> (a quantidade de dígitos a serem calculados).</li>
      <li><strong>Explicação do cálculo:</strong></li>
      <ul>
        <li>Para calcular o primeiro dígito verificador, multiplica-se cada dígito pelos fatores de 10 a 2, somando os resultados.</li>
        <li>O resultado dessa soma é multiplicado por 10 e o resto da divisão por 11 é calculado.</li>
        <li>Se o resto for igual a 10, o primeiro dígito verificador é considerado 0. Caso contrário, é igual ao resto.</li>
        <li>Para calcular o segundo dígito verificador, é feito o mesmo processo, mas os fatores são de 11 a 2 e o cálculo final é realizado.</li>
      </ul>
      <li>A soma dos resultados da multiplicação é calculada e o resultado final é obtido aplicando a fórmula <code>(resultado_soma * 10) % 11</code>.</li>
      <li>O dígito verificador calculado é retornado pela função.</li>
    </ul>
  </li>
</ol>

<p>Após gerar os nove dígitos aleatórios e calcular os dígitos verificadores, o programa imprime na tela o CPF válido gerado, no formato: <code>CPF Válido gerado: &lt;nove_digitos&gt;&lt;digito1&gt;&lt;digito2&gt;</code>.</p>

<h2>Utilização</h2>

<ol>
  <li>Certifique-se de ter o Python instalado no seu sistema.</li>
  <li>Faça o download do código-fonte do programa.</li>
  <li>Execute o programa em um ambiente Python de sua escolha.</li>
  <li>O programa irá gerar um CPF válido e exibi-lo na tela.</li>
</ol>
