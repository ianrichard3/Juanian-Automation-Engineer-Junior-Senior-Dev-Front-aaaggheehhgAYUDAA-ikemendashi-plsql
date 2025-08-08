import flet as ft
from repeating_job import RepeatingJob
from screenshot import take_screenshot


job = RepeatingJob(5, take_screenshot, output_dir="paper")


def generic_button(text, width, height, on_click):
    return ft.OutlinedButton(
        text=text,
        width=width,
        height=height,
        on_click=on_click
    )


def header():
    title = ft.Text("RememberScreen", size=24, weight=ft.FontWeight.BOLD)
    return title



def main(page: ft.Page):
    page.title = "RememberScreen"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 30
    page.window_width = 420
    page.window_height = 520

    

    # Estado inicial: apagado
    is_on = ft.Ref[bool]()
    is_on.current = False

    def on_toggle(e):
        job.stop() if is_on.current else job.start()
        is_on.current = not is_on.current
        toggle_btn.text = "Turn off" if is_on.current else "Turn on"
        page.update()
        


    def on_settings(_):
        print("Settings pressed")

    btn_width = 260
    btn_height = 44



    toggle_btn = generic_button(text="Turn on",
                         width=btn_width,
                                height=btn_height,
                                 on_click=on_toggle)

    settings_btn = generic_button(
        text="Settings",
        width=btn_width,
        height=btn_height,
        on_click=on_settings
    )


    page.add(
        ft.Container(
            content=ft.Column(
                [
                    header(),
                    ft.Container(height=100),
                    toggle_btn,
                    ft.Container(height=20),
                    settings_btn,
                ],
                horizontal_alignment="center",
                alignment=ft.MainAxisAlignment.START,
            ),
            width=350,
            padding=20,
            border=ft.border.all(2, "#000"),
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
