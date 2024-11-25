import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.title = 'Opções'
    page.window.height = 700
    page.window.width = 350
    page.window.maximizable = False

    page.bgcolor = ft.colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="assets/DoeMais.png",
            fit=ft.ImageFit.COVER,
            opacity=1,
        )
    )

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor= '#FF5175',
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, icon_color='#AB092A', icon_size=30),
                ft.IconButton(icon=ft.icons.LOCAL_HOSPITAL, icon_color=ft.colors.WHITE, icon_size=30),
                ft.IconButton(icon=ft.icons.HEALTH_AND_SAFETY, icon_color=ft.colors.WHITE, icon_size=30),
                ft.IconButton(icon=ft.icons.BLOODTYPE_OUTLINED, icon_color=ft.colors.WHITE, icon_size=30),
                ft.IconButton(icon=ft.icons.CHAT, icon_color=ft.colors.WHITE,icon_size=30),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.appbar = ft.AppBar(
        title=ft.Text("Home", color='white', font_family="Verdana"),
        center_title=True,
        bgcolor='#FF5175',
        leading=ft.IconButton(
            icon=ft.icons.MENU,
            icon_color='white',
            on_click=lambda e: print("Menu clicado"),
        ),
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOCAL_HOSPITAL, color='#FF5175', size=35),
                            ft.Text(
                                "Encontre posto de coleta", color='#FF5175', size=18, font_family="Verdana",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,  
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                    ), 
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=80,
                    border_radius=5,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.HEALTH_AND_SAFETY, color='#FF5175', size=35),
                            ft.Text(
                                "Agendamento de doações", color='#FF5175', size=18, font_family="Verdana",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,  
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                    ), 
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=80,
                    border_radius=5,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.BLOODTYPE_OUTLINED, color='#FF5175', size=35),
                            ft.Text(
                                "Campanhas de doações", color='#FF5175', size=18, font_family="Verdana",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,  
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                    ),  
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=80,
                    border_radius=5,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.CHAT, color='#FF5175', size=30),
                            ft.Text(
                                "Chat tira dúvidas", color='#FF5175', size=18, font_family="Verdana",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,  
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                    ),                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=300,
                    height=80,
                    border_radius=5,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),              
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


    # Stack principal
    _stack_main = ft.Stack(
        controls=[

        ]
    )



    page.add(_stack_main)

if __name__ == '__main__':
    ft.app(target=main)        
            
        
        
    