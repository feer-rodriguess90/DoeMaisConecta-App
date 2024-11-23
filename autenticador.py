import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.height = 700
    page.window.width = 350
    page.window_maximizable = False 

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def registrar(e):
        page.remove(login)
        page.add(register)
        page.update()

    login = ft.Column([
        ft.Container(
            #bgcolor=ft.colors.RED_200,
            width=page.window.width - 10,
            height=page.window.height - 60,
            border_radius=10,
            image_src="assets/DoeMais.png",
            image_fit=ft.ImageFit.COVER,
        

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE38,
                    width=300,
                    height=300,
                    border_radius=10,
                

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),

                            content= ft.Column([
                                ft.Text(
                                    value='LOG IN',
                                    weight='bold',
                                    size=20,
                                    color="#AB092A",
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Email',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text='Senha',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.ElevatedButton(
                                text='LOG IN',
                                bgcolor="#AB092A",
                                color="#FFFFFF",
                                on_hover="#FF4D72",
                                width=250,
                                height=40,
                                style=ft.ButtonStyle(
                                    text_style=ft.TextStyle(weight="bold") 
                                ),
                            ),

                            ft.Row([
                                ft.TextButton(
                                    'Recuperar Senha', 
                                    style=ft.ButtonStyle(color="#AB092A")),
                                ft.TextButton(
                                    text='Criar nova conta',
                                    on_click=registrar,
                                    style=ft.ButtonStyle(color="#AB092A"))
                            ],width=250,alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing=10),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.ALTERNATE_EMAIL,
                                          icon_color="white",
                                          icon_size=30,
                                          tooltip="Email"), 
                            ft.IconButton(icon=ft.icons.FACEBOOK,
                                          icon_color="white",
                                          icon_size=30,
                                          tooltip="Facebook"),             
                        ],alignment='center')

                    ],horizontal_alignment='center')
                )
            ],horizontal_alignment='center',alignment='center')
        )

    ])

    register = ft.Column([
        ft.Container(
            #bgcolor=ft.colors.RED_200,
            width=page.window.width - 10,
            height=page.window.height - 60,
            border_radius=10,
            image_src="assets/DoeMais.png",
            image_fit=ft.ImageFit.COVER,
        

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE38,
                    width=300,
                    height=420,
                    border_radius=10,
                

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),

                            content= ft.Column([
                                ft.Text(
                                    value='CADASTRAR',
                                    weight='bold',
                                    size=20,
                                    color="#AB092A",
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Nome',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text='Email',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.EMAIL,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text='Senha',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.TextField(
                                hint_text='Confirmar Senha',
                                width=250,
                                height=40,
                                border_radius=10,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.ElevatedButton(
                                text='CADASTRAR',
                                bgcolor="#AB092A",
                                color="#FFFFFF",
                                on_hover="#FF4D72",
                                width=250,
                                height=40,
                                style=ft.ButtonStyle(
                                    text_style=ft.TextStyle(weight="bold") 
                                ),
                            ),

                            ft.Row([
                                ft.TextButton(
                                    'Recuperar Senha', 
                                    style=ft.ButtonStyle(color="#AB092A")),
                                ft.TextButton(
                                    text='Já possuo conta',
                                    on_click=logar,
                                    style=ft.ButtonStyle(color="#AB092A"))
                            ],width=250,alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing=10),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.ALTERNATE_EMAIL,
                                          icon_color="white",
                                          icon_size=30,
                                          tooltip="Email"), 
                            ft.IconButton(icon=ft.icons.FACEBOOK,
                                          icon_color="white",
                                          icon_size=30,
                                          tooltip="Facebook"),             
                        ],alignment='center')

                    ],horizontal_alignment='center')
                )
            ],horizontal_alignment='center',alignment='center')
        )

    ])


    page.add(login)



if __name__ == '__main__':
    ft.app(target=main)