# language: pt

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
