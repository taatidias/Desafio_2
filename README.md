# Projeto Teste WebService/API

Esse projeto tem como objetivo realizar teste para android com o intuito de validar o cadastro do usuario e o login no app.

## Introdução

As instruções a seguir fornecerão meios de como iniciar o projeto Desafio2 para fins de testes para android.

### Pré requisitos

```
1.Necessário ter instalado o sistema operacional Windows.
2.Python 3.8.5
3.Pycharm 2020.1.4 x64
4.Appium
5.Behave
6.PIP 
7.Environment.py esteja configurado de acordo com as especificações do dispositivo testado.
```

### Automatizando os testes

Após realizar a instalação com exito do Python e do Pycharm, é preciso baixar o projeto Desafio2 no GitHub e extrair o projeto na pasta desejada.
Para abrir o projeto pelo Pycharm:

```
- Clicar em File
- Opção Open
- Selecionar a pasta Desafio2-master
- Clicar no botão Ok
```

## Executando os testes

Antes de iniciar a execução dos testes, é necessário a instalação do requirements.txt, para isso rode o seguinte comando.

```
~\Desafio2-master> pip install -r requirements.txt
```
As dependências declaradas no arquivo requirements.txt são o behave, selenium e appium indicando o uso de uma determinada versão ou uma versão mais atualizada.


### Detalhamento dos testes

Para iniciar a execução de testes, é necessário contruir cenários que simulam o objetivo proposto pelo teste com o intuito de validar e retornar o status(passed ou fail). Sendo assim, para atender de forma abragente foi realizado quatro cenários, dentre eles: acessar a página de registro, preencher a pagina de registro, testar o login válido e testar o login inválido conforme o exemplo abaixo:

```
Funcionalidade: Registrar um novo usuário

      Cenario: Acessar a página de registro
          Dado que eu esteja na tela de "Login"
          Quando eu clico na opção "New User? Register"
          Entao que exiba a tela "Registration"

      Cenario: Preencher a pagina de registro
          Dado que eu esteja na tela "Registration"
          Quando eu preencho o campo "Name" com "Kurtis Weissnat"
          E eu preencho o campo "Phone number" com "58804-1099"
          E eu preencho o campo "Gmail" com "Telly.Hoeger@gmail.com"
          E eu preencho o campo "Password" com "Abc12345"
          E eu clico no botão "Register"
          Entao eu recebo a mensagem "Registration Successful"

      Cenario: Testar o login válido
          Dado que eu esteja na tela de "Login"
          Quando eu preencho o campo "Email" com "Telly.Hoeger@gmail.com"
          E eu preencho o campo "Password" com "Abc12345"
          Então eu recebo a mensagem "Login Success"

       Cenario: Testar o login inválido
          Dado que eu esteja na tela de "Login"
          Quando eu preencho o campo "Email" com "Telly.Hoeger@gmail.com"
          E eu preencho o campo "Password" com "Abc123"
          Então eu recebo a mensagem "Login Error"


```
Dentre diversas ferramentas para automatizar os testes, a escolhida foi o Appium. Diante de algumas buscas e analises foi possivel verificar que essa ferramenta além de ser gratuita e funcionar com a liguagem Python, ela também é multiplataforma (Linux, Windows e MAC). 
Além disso, por não ter conhecimento em testes para android, essa ferramenta ganhou destaque quando pesquisei sobre seu uso e impacto ao retornar a validação dos testes, e encontrei sites com grande conteudo informativo e detalhado sobre o mesmo.

Ao utilizar o Appium, existe alguns valores padrões necessários para especificar seu android, conforme o exemplo a seguir:

```
app = os.path.abspath(app)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': None,
            'udid': '01a135891395669f',
            'appActivity': '.HomeActivity',
            'appPackage': 'com.android.mobile'

```
 O Appium já traz preenchido alguns campos, dentre eles: Remote Host: 127.0.0.1, Remote Path: /wd/hub e Remote Port: 4327 (pode ser alterada de acordo com o valor desejado). Para iniciar a sessão, entretando dois campos ao menos devem ser preenchidos de acordo com a informação desejada. ('platformName:' e 'deviceName').

### Resultado esperado da bateria de testes

Para que tenha o resultado esperado, é necessário o uso de um emulador(dispositivo que simula um celular real) e de ADB (responsável pela comunicação entre o computador e o dispositivo móvel Android) para obter todas as configurações desejadas do app. Além disso exige que seu computador possua algumas configurações especificas para conseguir rodar o emulador desejado.

```
Conseguir cadastrar com o usuário;
Logar no sistema com exito;
Verificar a segurança/ eficácia do login (login inválido).

```
Logo acima temos os 3 resultados esperados ao executar os testes, de acordo com os cenários informados na sua funcionalidade.

## Autora

* **Tatiane Gomes Dias** 


