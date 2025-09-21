import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# المجلد الأصلي مال PUBG Mobile
TARGET_FOLDER = "/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Content"

class RenameApp(App):
    def build(self):
        self.label = Label(text="المجلد:\n" + TARGET_FOLDER, font_size=18)

        btn_change = Button(text="تغيير", font_size=20, on_press=self.change_folder)
        btn_revert = Button(text="ارجاع", font_size=20, on_press=self.revert_folder)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(self.label)
        layout.add_widget(btn_change)
        layout.add_widget(btn_revert)

        return layout

    def change_folder(self, instance):
        global TARGET_FOLDER
        if os.path.exists(TARGET_FOLDER):
            new_name = TARGET_FOLDER + "1"
            try:
                os.rename(TARGET_FOLDER, new_name)
                TARGET_FOLDER = new_name
                self.label.text = "المجلد:\n" + TARGET_FOLDER
            except Exception as e:
                self.label.text = f"فشل التغيير:\n{e}"

    def revert_folder(self, instance):
        global TARGET_FOLDER
        if os.path.exists(TARGET_FOLDER) and TARGET_FOLDER.endswith("1"):
            new_name = TARGET_FOLDER[:-1]
            try:
                os.rename(TARGET_FOLDER, new_name)
                TARGET_FOLDER = new_name
                self.label.text = "المجلد:\n" + TARGET_FOLDER
            except Exception as e:
                self.label.text = f"فشل الإرجاع:\n{e}"


if __name__ == "__main__":
    RenameApp().run()