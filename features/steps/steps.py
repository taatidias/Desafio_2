from behave import given, when, then


@given('que eu esteja na tela de {name_screen}')
def step_impl(context, name_screen):
    try:
        el1 = context.driver.find_element_by_xpath('//*[@text='+name_screen+']')
        if el1.text != '':
            print('Tela encontrada. Teste conluido')
        else:
            raise Exception('Tela não encontrada. Fim do Cenario')
    except Exception as e:
        print(e)


@when('eu clico na opção {name_link}')
def step_impl(context, name_link):
    component_link = context.driver.find_element_by_accessibility_id(name_link)
    try:
        component_link.click()
    except Exception as e:
        print('Erro Inesperado')


@when('eu preencho o campo {field} com {field_value}')
def step_iml(context, field, field_value):
    component_field = context.driver.find_element_by_xpath('//*[@text='+field+']')
    try:
        component_field.text = field_value
    except Exception as e:
        print('Erro inesperado.')


@when('eu clico no botão {button}')
def step_impl(context, button):
    component_button = context.driver.find_element_by_class_name(button)
    try:
        component_button[0].click()
    except Exception as e:
        print('Mensagem não encontrada. Fim do Cenario')


@then('que exiba a tela {name_screen}')
def step_impl(context, name_screen):
    try:
        el1 = context.driver.find_element_by_xpath('//*[@text='+name_screen+']')
        if el1.text != '':
            print('Tela encontrada. Teste conluido')
        else:
            raise Exception('Mensagem não encontrada. Fim do Cenario')
    except Exception as e:
        print(e)


@then('eu recebo a mensagem {message}')
def step_impl(context, message):
    try:
        component_message = context.driver.find_element_by_accessibility_id(message)
        if component_message.text != '':
            print('Mensagem encontrada com sucesso. Fim do Cenario')
        else:
            raise Exception('Mensagem não encontrada. Fim do Cenario')
    except Exception as e:
        print(e)


