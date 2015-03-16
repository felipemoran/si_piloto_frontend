import re

caso = 2

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc neque, tempus nec erat vel, egestas pulvinar lorem. Nam hendrerit lacinia imperdiet. Vivamus iaculis pretium scelerisque. Curabitur enim dui, sodales id varius non, semper sed ligula. Maecenas sit amet lorem eu leo imperdiet tempus. Mauris mattis nulla non metus condimentum, eu gravida quam posuere. Phasellus fermentum leo a auctor suscipit. Duis tincidunt elementum lobortis. Morbi egestas condimentum fermentum. Aenean placerat dui dictum euismod convallis. Cras vitae leo nec turpis viverra condimentum. In vitae risus congue lorem viverra tristique. Cras consectetur purus nibh, quis placerat elit aliquet quis.\n\
Sed sem magna, pretium quis lacus et, scelerisque pellentesque libero. Suspendisse vel maximus magna, vitae egestas nunc. Suspendisse cursus semper dapibus. Mauris tristique, felis at condimentum fringilla, ex turpis vulputate justo, sit amet sodales orci enim vitae sapien. Pellentesque elementum elementum metus in euismod. Nulla luctus mi ipsum, eget interdum nunc venenatis lobortis. Aliquam quis quam ornare, iaculis diam tincidunt, eleifend arcu. In sed magna ornare, iaculis nisi eget, dapibus dui. Donec vitae finibus diam, a dictum lectus.'

print '******'

if caso == 1:
    corta_n = re.compile('.{1,200}')
    corta_ponto = re.compile('\.')

    resultado = re.findall(corta_n, texto)

    print '------'

    for coisa in resultado:
        print coisa
        print '--'

        corte = coisa.rsplit('.',1)

        for coisa2 in corte:
            print coisa2 + '.'
            print '....'
elif caso == 2:
    lista_paragrafos = texto.split('\n')

    print lista_paragrafos

    for elem in lista_paragrafos:
        print elem
        print '888'
